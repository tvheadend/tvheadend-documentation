##Markdown/Formatting Crib Sheet

Some notable items about how formatting is used on this particular site.

In general, **keep it simple**, especially if you're contributing to the
pages that get carried over into the web help. The simpler the formatting,
the cleaner the conversion, the less tidying up there is afterwards.

###References

* Markdown basics: <https://daringfireball.net/projects/markdown/syntax>

* Markdown test: <https://daringfireball.net/projects/markdown/dingus>

###Paragraphs Versus Definition Lists

Watch this one - indentation is key.

**This is paragraph formatting**
: with a subsequent explanation

    **This is paragraph formatting**
    : with a subsequent explanation

**This is definition list formatting**
:   with a subsequent explanation

    **This is definition list formatting**
    :   with a subsequent explanation

They may render the same here, but note the extra leading spaces in the 
second example: this means that they will convert differently for use in 
the web interface help. That in turn means your formatting will be all
over the place unless you handle the dl/dt/dd formatting in Tvheadend's CSS. 

Stick to paragraph formatting unless and until you have a need for 
definition lists.

### Lists

Mixed lists don't work without further python extensions. Be careful.

```markdown
1. First ordered list item
2. Another item
  * Unordered sub-list. 
1. Actual numbers don't matter, just that it's a number
  1. Ordered sub-list
4. And another item.

   You can't have have properly indented paragraphs within list items. 
   
* Unordered list can use asterisks
- Or minuses
+ Or pluses

Oh, and

77. Each numbered (ordered) list will restart from 1.
```

... produces:

1. First ordered list item
2. Another item
  * Unordered sub-list. 
1. Actual numbers don't matter, just that it's a number
  1. Ordered sub-list
4. And another item.

   You can't have have properly indented paragraphs within list items. 
   
* Unordered list can use asterisks
- Or minuses
+ Or pluses

Oh, and

77. Each numbered (ordered) list will restart from 1.

### Tables

Tables can be constructed as follows.

The markup code:

    First Header                | Second Header
    --------------------------- | -------------
    Content from cell 1         | Content from cell 2
    Content in the first column | Content in the second column

Will generate:

First Header                | Second Header
--------------------------- | -------------
Content from cell 1         | Content from cell 2
Content in the first column | Content in the second column

And if you don't want a header, you can leave it out - but the cells
remain in this theme, so I'd suggest you don't do this as it's ugly:

     | 
    --------------------------- | -------------
    Headless table cell 1       | Content from cell 2
    Content in the first column | Content in the second column

 | 
--------------------------- | -------------
Headless table cell 1       | Content from cell 2
Content in the first column | Content in the second column

We're using default heading/cell justification, so it's consistent throughout.

### Admonitions

Admonitions in markdown/mkdocs rely on a python extension, which works
well in the base guide but doesn't survive the pandoc translation to 
standalone HTML for the webUI.

For that reason, use HTML instead, and it'll survive conversion:

<div class="admonition note">
<p class="admonition-title">NOTE: This is a note</p>
    <p>This is an admonition - a note, warning, or other attention-grabber.</p> 
    <p>Note that you can't include markdown in HTML, so need to write it by hand</p>
    <p>HTML formatting includes <em>italic</em>, <strong>bold</strong>, 
    <em><strong>bold italic</strong></em>,<del>strikethrough</del>, 
    <u>underline</u>, and <kbd>keyboard</kbd></p>
    
    <p>You can include</p>
    
    <ul>
      <li>Unordered lists (aka. bullets)</li>
      <li>Bullets</li>
    </ul>

    <p>and</p>
    
    <ol>
      <li>Lists</li>
      <li>Lists</li>
      <li>Lists</li>
    </ol>

    <p>You can include tables, although you don't get all the formatting
    unless you hack the CSS:</p>
    
    <table>
    <thead>
        <tr class="header">
        <th align="left">First</th>
        <th align="left">Second</th>
        <th align="left">Third</th>
      </tr>
    </thead>
    <tbody>
      <tr class="odd">
        <td align="left">Cell 1</td>
        <td align="left">Cell 2</td>
        <td align="left">Cell 3</td>
      </tr>
      <tr class="even">
        <td align="left">Cell 1</td>
        <td align="left">Cell 2</td>
        <td align="left">Cell 3</td>
      </tr>
    </tbody>
    </table>

    <p>You can include <code>code</code></p>

    <p>Code blocks kind-of-work but needs more styling - they're not pretty:</p>
    
    <p><code>echo Hello $1\!
    echo
    echo Goodbye</code></p>
</div>

Code for all of the above:

```html
<div class="admonition note">
<p class="admonition-title">NOTE: This is a note</p>
    <p>This is an admonition - a note, warning, or other attention-grabber.</p> 
    <p>Note that you can't include markdown in HTML, so need to write it by hand</p>
    <p>HTML formatting includes <em>italic</em>, <strong>bold</strong>, 
    <em><strong>bold italic</strong></em>,<del>strikethrough</del>, 
    <u>underline</u>, and <kbd>keyboard</kbd></p>
    
    <p>You can include</p>
    
    <ul>
      <li>Unordered lists (aka. bullets)</li>
      <li>Bullets</li>
    </ul>

    <p>and</p>
    
    <ol>
      <li>Lists</li>
      <li>Lists</li>
      <li>Lists</li>
    </ol>

    <p>You can include tables, although you don't get all the formatting
    unless you hack the CSS:</p>
    
    <table>
    <thead>
        <tr class="header">
        <th align="left">First</th>
        <th align="left">Second</th>
        <th align="left">Third</th>
      </tr>
    </thead>
    <tbody>
      <tr class="odd">
        <td align="left">Cell 1</td>
        <td align="left">Cell 2</td>
        <td align="left">Cell 3</td>
      </tr>
      <tr class="even">
        <td align="left">Cell 1</td>
        <td align="left">Cell 2</td>
        <td align="left">Cell 3</td>
      </tr>
    </tbody>
    </table>

    <p>You can include <code>code</code></p>

    <p>Code blocks kind-of-work but needs more styling - they're not pretty:</p>
    
    <p><code>echo Hello $1\!
    echo
    echo Goodbye</code></p>
</div>
```

Other admonition types are defined and available:

    <div class="admonition tip">
    <p class="admonition-title">TIP: Sample title</p>
    <p>Sample text</p>
    </div>

<div class="admonition tip">
<p class="admonition-title">TIP: Sample title</p>
<p>Sample text</p>
</div>

    <div class="admonition warning">
    <p class="admonition-title">WARNING: Sample title</p>
    <p>Sample text</p>
    </div>

<div class="admonition warning">
<p class="admonition-title">WARNING: Sample title</p>
<p>Sample text</p>
</div>

    <div class="admonition danger">
    <p class="admonition-title">DANGER: Sample title</p>
    <p>Sample text</p>
    </div>

<div class="admonition danger">
<p class="admonition-title">DANGER: Sample title</p>
<p>Sample text</p>
</div>

###Other HTML

As a general rule, you can include any HTML in markdown if you need it. 
It does defeat the easy-to-write/easy-to-read object, though, so use only 
as necessary.
