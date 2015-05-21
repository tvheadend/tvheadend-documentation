##Scratchpad

## Cheat Sheet/Scratch pad to test readthedocs/mkdocs

### Tables

First Header | Second Header
------------ | -------------
Content from cell 1 | Content from cell 2
Content in the first column | Content in the second column

  | 
------------ | -------------
Headless table cell 1 | Content from cell 2
Content in the first column | Content in the second column

|First Header | Second Header|
|:------------ | -------------:|
|Content from cell 1 | Content from cell 2|
|Content in the first column | Content in the second column|

### Admonitions

roll-your-own admonitions (pandoc doesn't translate them properly):

<div class="admonition note">
<p class="admonition-title">NOTE: This is a note</p>
    <p>This is an admonition - here is <em>some</em> <strong>more</strong> <em><strong>text</strong></em>.
    <del>Strikethrough text</del>, <u>Underline</u>, <kbd>keyboard</kbd></p>
    <p>Can you include <code>code</code>?</p>
    
    <p>Can you include</p>
    
    <ul>
    <li>Bullets?</li>
    </ul>

    <p>and</p>
    
    <ol>
    <li>Lists?</li>
    <li>Lists?</li>
    <li>Lists?</li>
    </ol>

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

    
       
    Code blocks kind-of-work but needs more styling:
    
    <p><code>echo Hello $1\!
    echo
    echo Goodbye</code></p>
    
</div>

<div class="admonition tip">
<p class="admonition-title">TIP: Sample title</p>
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


### Text effects

<del>Strikethrough text.</del>, <u>Underline</u>, <kbd>keyboard</kbd>

Use <kbd>alt-f4</kbd> to close the window; press <kbd>Ctrl-Fn-F1</kbd><kbd>q</kbd> to quit.

"test" 'test2'

### Lists - mixing doesn't work without furhter python extensions

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
