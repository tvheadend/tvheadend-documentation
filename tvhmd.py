#!/usr/bin/env python3

"""
Tvheadend markdown utility
==========================

This utility does these jobs:

 - markdown to POT conversions for gettext
 - gettext's PO to markdown merges for translations

## Authors and License

Copyright (C) 2015 Jaroslav Kysela

License: WTFPL 2
"""

import os
import sys
import datetime
import textwrap
from mistune import Markdown, Renderer
import xml.parsers.expat

TOPDIR=os.path.dirname(os.path.realpath(sys.argv[0]))

#
# MD_Renderer
#

class Object:

  pass

class MD_Renderer(Renderer):

  def __init__(self, **kwargs):
    self.pot_blacklist = {}
    self.strings = {}
    self.pot = ''
    Renderer.__init__(self, **kwargs)
    self.cmd = ''
    if self.options.get('pot'):
      self.cmd = 'pot'
    elif self.options.get('lang_md'):
      self.cmd = 'lang-md'

  def translate_check(self, text):
    if not text:
      return False
    if text in self.pot_blacklist:
      return False
    if text.lstrip().rstrip() in [',', ',', ':', ';', '!', '(', ')', '{', '}']:
      return False
    if text[0] == '<':
      return False
    return True 

  def add_pot_text(self, text):
    if not self.translate_check(text):
      return
    if text in self.strings:
      return
    self.strings[text] = 1
    text = text.replace('\\', '\\\\')
    text = text.replace('"', '\\"')
    if text.find('\n') >= 0:
      w = textwrap.wrap(text, 76, drop_whitespace=False, break_long_words=False)
      w = '\nmsgid ""\n"' + '"\n"'.join(w) + '"\n'
      self.pot += w
    else:
      self.pot += '\nmsgid "' + text + '"\n'
    self.pot += 'msgstr ""\n'

  def do_translate(self, text):
    if not self.translate_check(text):
      return text
    if not text in self.strings:
      if text:
        print('UNTRANSLATED', repr(text))
      return text
    return '\n'.join(textwrap.wrap(self.strings[text], 76, break_long_words=False))

  def translate(self, text):
    if not text or not self.cmd:
      return text
    pref = ''
    suff = ''
    while text and text[0] in [' ', '\n']:
      pref += text[0]
      text = text[1:]
    while text and text[len(text)-1] in [' ', '\n']:
      suff = text[len(text)-1]
      text = text[:-1]
    if not text:
      return pref + suff

    r = ''
    for p in text.split():
      if p:
        r += ' ' + p
    text = r[1:]

    if self.cmd == 'pot':
      self.add_pot_text(text)
    elif self.cmd == 'lang-md':
      return pref + self.do_translate(text) + suff
    return pref + text + suff

  def get_block(text):
    type = text[0]
    p = text.find(':')
    if p <= 0:
      return ('', '', '')
    l = int(text[1:p])
    t = text[p+1:p+1+l]
    return (text[p+1+l:], type, t)

  def newline(self):
    return '\n'

  def text(self, text):
    return self.translate(text)

  def strikethrough(self, text):
    return text

  def linebreak(self):
    return '\n'

  def hrule(self):
    return '---\n'

  def header(self, text, level, raw=None):
    return '#'*(level+1) + text + '\n\n'

  def paragraph(self, text):
    return text + '\n\n'

  def list(self, text, ordered=True):
    r = ''
    while text:
      text, type, t = MD_Renderer.get_block(text)
      if type == 'l':
        r += (ordered and ('# ' + t) or ('* ' + t)) + '\n'
    return r

  def list_item(self, text):
    return 'l' + str(len(text)) + ':' + text

  def block_code(self, code, lang=None):
    return '```no-highlight\n' + code + '\n```\n'

  def block_quote(self, text):
    r = ''
    for line in text.splitlines():
      r += (line and '> ' or '') + line + '\n'
    return r

  def _emphasis(self, text, pref):
    return pref + text + pref + ' '

  def emphasis(self, text):
    return self._emphasis(text, '_')
    
  def double_emphasis(self, text):
    return self._emphasis(text, '__')

  def codespan(self, text):
    return '`' + text + '`'

  def autolink(self, link, is_email=False):
    return '<' + link + '>'

  def link(self, link, title, text, image=False):
    r = (image and '!' or '') + '[' + text + '](' + link + ')'
    if title:
      r += '"' + title + '"'
    return r

  def image(self, src, title, text):
    self.link(src, title, text, image=True)

  def table(self, header, body):
    hrows = []
    while header:
      header, type, t = MD_Renderer.get_block(header)
      if type == 'r':
        flags = {}
        cols = []
        while t:
          t, type2, t2 = MD_Renderer.get_block(t)
          if type2 == 'f':
            fl, v = t2.split('=')
            flags[fl] = v
          elif type2 == 'c':
            c = Object()
            c.flags = flags
            c.text = t2
            cols.append(c)
        hrows.append(cols)
    brows = []
    while body:
      body, type, t = MD_Renderer.get_block(body)
      if type == 'r':
        flags = {}
        cols = []
        while t:
          t, type2, t2 = MD_Renderer.get_block(t)
          if type2 == 'f':
            fl, v = t2.split('=')
            flags[fl] = v
          elif type2 == 'c':
            c = Object()
            c.flags = flags
            c.text = t2
            cols.append(c)
        brows.append(cols)
    colscount = 0
    colmax = [0] * 100
    for row in hrows + brows:
      colscount = max(len(row), colscount)
      i = 0
      for col in row:
        colmax[i] = max(len(col.text), colmax[i])
        i += 1
    r = ''
    for row in hrows:
      i = 0
      for col in row:
        if i > 0:
          r += ' | '
        r += col.text.ljust(colmax[i])
        i += 1
      r += '\n'
    for i in range(colscount):
      if i > 0:
        r += '-|-'
      r += '-'.ljust(colmax[i], '-')
    r += '\n'
    for row in brows:
      i = 0
      for col in row:
        if i > 0:
          r += ' | '
        r += col.text.ljust(colmax[i])
        i += 1
      r += '\n'
    return r

  def table_row(self, content):
    return 'r' + str(len(content)) + ':' + content

  def table_cell(self, content, **flags):
    content = content.replace('\n', ' ')
    r = ''
    for fl in flags:
      v = flags[fl]
      if type(v) == type(True):
        v = v and 1 or 0
      v = str(v) and str(v) or ''
      r += 'f' + str(len(fl) + 1 + len(v)) + ':' + fl + '=' + v
    return r + 'c' + str(len(content)) + ':' + content

  def footnote_ref(self, key, index):
    raise

  def footnote_item(self, key, text):
    raise
    
  def footnotes(self, text):
    raise

class WEBUI_Renderer(Renderer):

  def replace_start(src, start, replacement):
    if src.startswith(start):
      return replacement + src[len(start):]
    return src

  def image(self, src, title, text):
    src = WEBUI_Renderer.replace_start(src, 'icons/', 'static/icons/')
    src = WEBUI_Renderer.replace_start(src, '../icons/', 'static/icons/')
    return Renderer.image(self, src, title, text)

#
# Utils
#

def argv_get(what):
  what = '--' + what
  for a in sys.argv:
    if a.startswith(what):
      a = a[len(what):]
      if a[0] == '=':
        return a[1:]
      else:
        return True
  return None

def read_blacklist():
  global TOPDIR
  fn = TOPDIR + "/iblacklist.txt"
  r = {}
  if os.path.exists(fn):
    f = open(fn)
    while 1:
      l = f.readline()
      if not l:
        break
      if l[0] == '#':
        continue
      r[l.lstrip().rstrip()] = 1
    f.close()
  return r

class UTC(datetime.tzinfo):
  def utcoffset(self, dt):
    return datetime.timedelta(0)
  def tzname(self, dt):
    return "UTC"
  def dst(self, dt):
    return datetime.timedelta(0)

#
#
#

class POT:

  def __call__(self, text):
    return self.to_pot(text)

  def to_pot(self, text):

    renderer = MD_Renderer(pot=1)
    renderer.pot_blacklist = read_blacklist()
    md = Markdown(renderer)
    md(text)

    header="""\
# Autogenerated POT file from markdown text.
#
#, fuzzy
msgid ""
msgstr ""
"Project-Id-Version: tvheadend\\n"
"Report-Msgid-Bugs-To: \\n"
"POT-Creation-Date: %{1}\\n"
"PO-Revision-Date: YEAR-MO-DA HO:MI+ZONE\\n"
"Last-Translator: FULL NAME <EMAIL@ADDRESS>\\n"
"Language-Team: LANGUAGE <LL@li.org>\\n"
"Language: \\n"
"MIME-Version: 1.0\\n"
"Content-Type: text/plain; charset=utf-8\\n"
"Content-Transfer-Encoding: 8bit\\n"
"""

    now = datetime.datetime.now(UTC())
    res = header.replace('%{1}', now.strftime("%F %R%z"))

    return res + renderer.pot

class PO:

  def __init__(self):
    self.strings = {}

  def __call__(self, text, po):
    return self.internationalize(text, po)

  def po_str(text):
    text = text.lstrip().rstrip()
    if not text:
      return ''
    if text[0] != '"' and text[-1] != '"':
      raise ValueError('Wrong text: %s' % text)
    text = text[1:-1]
    if not text:
      return ''
    r = ''
    l = len(text)
    i = 0
    while i < l:
      c = text[i]
      if c == '\\':
        i += 1
        if i >= l:
          continue
        c = text[i]
        if c == 'n':
          c = '\n'
        elif c == 'r':
          c = '\r'
        elif c == 't':
          c = '\t'
      r += c
      i += 1
    return r

  def po_modify(out, str):
    str = PO.po_str(str)
    return out + str

  def po_finish(self, msgid, msgstr):
    if msgid and not msgstr:
      msgstr = msgid
    if msgid:
      self.strings[msgid] = msgstr

  def po_parse(self, text):
    msgid = ''
    msgstr = ''
    msgidflag = False
    for line in text.splitlines():
      line = line.lstrip().rstrip()
      if line and line[0] == '#':
        continue
      if not line:
        self.po_finish(msgid, msgstr)
        msgid = ''
        msgstr = ''
      if line.startswith('msgid '):
        msgid = PO.po_modify(msgid, line[6:])
        msgidflag = True
      elif line.startswith('msgstr '):
        msgstr = PO.po_modify(msgstr, line[7:])
        msgidflag = False
      elif msgidflag:
        msgid = PO.po_modify(msgid, line)
      else:
        msgstr = PO.po_modify(msgstr, line)
    self.po_finish(msgid, msgstr)

  def internationalize(self, text, po):

    po = self.po_parse(po)
    renderer = MD_Renderer(lang_md=1)
    renderer.strings = self.strings
    renderer.pot_blacklist = read_blacklist()
    md = Markdown(renderer)
    output = md(text)
    
    return output

class HTML:

  def __call__(self, text):
    return self.html(text)

  def html(self, text):

    renderer = WEBUI_Renderer(use_xhtml=1)
    md = Markdown(renderer)
    output = md(text)

    hdr = '<!-- Do not edit! Automatically created file: https://github.com/tvheadend/tvheadend-documentation -->\n'
    now = datetime.datetime.now(UTC())
    hdr += '<!-- Build date: ' + now.strftime("%F %R %z") + ' -->\n'

    return hdr + '<div class="hts-doc-text">\n' + output + '</div>\n'

#
#
#

f = open(argv_get('in'))
text = f.read(1024*1024)
f.close()

format = argv_get('format') or 'pot'
if format == 'pot':
  result = POT()(text)
elif format == 'lang-md':
  f = open(argv_get('po'))
  po = f.read(1024*1024)
  f.close()
  result = PO()(text, po)
elif format == 'lang-html':
  result = HTML()(text)
else:
  raise

ofn = argv_get('out')
if not ofn:
  sys.stdout.write(result)
else:
  p = os.path.dirname(os.path.realpath(ofn))
  if not os.path.exists(p):
    os.makedirs(p)
  open(ofn, "w+").write(result)
