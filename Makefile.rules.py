#!/usr/bin/env python

"""
Tvheadend makefile generation utility
=====================================

This utility does these jobs:

- create Makefile rules for tvh documentation project
   
## Authors and License
   
Copyright (C) 2015 Jaroslav Kysela
   
License: WTFPL 2
"""

import os
import sys

def argv_get(what):
  what = '--' + what
  for a in sys.argv:
    if a.startswith(what):
      a = a[len(what):]
      if a[0] == '=':
        return a[1:]
      else:
        return '1'
  return ''

def parse_langs(langs):
  l = langs.split(' ')
  r = []
  for o in l:
    o = o.lstrip().rstrip()
    if o:
      r.append(o)
  return r

def src_file(dn, fn, bn):
  return 'docs/' + (dn and dn + '/' or '') + fn

def pot_file(dn, fn, bn):
  return 'intl/' + (dn and dn + '/' or '') + fn + '/' + bn + '.pot'

def po_file(lang, dn, fn, bn):
  return 'intl/' + (dn and dn + '/' or '') + fn + '/' + bn + '.' + lang + '.po'

def md_file(lang, dn, fn, bn):
  return 'build/' + lang + '/' +  (dn and dn + '/' or '') + fn

def webui_file(lang, dn, fn, bn):
  return 'webui/' + lang + '/' +  (dn and dn + '/' or '') + bn + '.html'

def yml_po_file(lang):
  return 'intl/mkdocs/mkdocs.' + lang + '.po'

def site_base(lang):
  return 'mkdocs/' + lang

def site_file(lang):
  return site_base(lang) + '/site/index.html'

def do_pot(out, dn, fn, bn):
  out.write(pot_file(dn, fn, bn) + ': ' + src_file(dn, fn, bn) + '\n')
  out.write('\t$(call do_pot,$<,$@)\n\n')

def do_langs(out, langs, dn, fn, bn):
  for lang in langs:
    out.write(po_file(lang, dn, fn, bn) + ': ' + pot_file(dn, fn, bn) + '\n');
    out.write('\t$(call do_po,$<,$@,' + lang + ')\n\n')

def do_mds(out, langs, dn, fn, bn):
  for lang in langs:
    out.write(md_file(lang, dn, fn, bn) + ': ' + po_file(lang, dn, fn, bn) + \
              ' ' + src_file(dn, fn, bn) + '\n');
    out.write('\t$(call do_md,' + src_file(dn, fn, bn) + ',$@,' + lang + \
              ',' + po_file(lang, dn, fn, bn) + ')\n\n')

def do_webuis(out, langs, dn, fn, bn):
  for lang in langs:
    out.write(webui_file(lang, dn, fn, bn) + ': ' + md_file(lang, dn, fn, bn) + '\n')
    out.write('\t$(call do_webui,$<,$@,' + lang + ')\n\n')

def do_yml(out, src, dst):
  lang = dst.split('/')[1]
  out.write(dst + ': ' + src + ' ' + yml_po_file(lang) + '\n')
  out.write('\t$(call do_yml,' + src + ',$@,' + lang + ',' + yml_po_file(lang) + ')\n\n')
  out.write(yml_po_file(lang) + ': intl/mkdocs/mkdocs.pot\n')
  out.write('\t$(call do_po,$<,$@,' + lang + ')\n\n')
  out.write(site_file(lang) + ': ' + dst + ' ' + yml_po_file(lang) + '\n')
  out.write('\t$(call do_site,' + site_base(lang) + ',$@,' + lang + ')\n\n')

outfn = argv_get('out')
outfn = outfn and outfn or 'Makefile.rules'
langs = argv_get('langs')
langs = parse_langs(langs and langs or 'en cs')
mds = argv_get('mds').split()
ymls = argv_get('ymls').split()

out = open(outfn, 'w+')
for n in mds:
  if n.startswith('docs/'):
    rn = n[5:]
    dn, fn = os.path.split(rn)
    bn, en = os.path.splitext(fn)
    if en != '.md':
      continue
    do_pot(out, dn, fn, bn)
    do_langs(out, langs, dn, fn, bn)
    do_mds(out, langs, dn, fn, bn)
    do_webuis(out, langs, dn, fn, bn)
for n in ymls:
  if n.startswith('mkdocs/'):
    do_yml(out, 'mkdocs.yml', n)
out.close()
