## Structure

1. Edit files in ./docs/ - all files specific to the application web interface are in ./docs/webui/

2. Any new files need to be added to ./mkdocs.yml, as that drives the index/ToC

3. Images for the web help pages are then in ./docs/webui/docresources/ and ./docs/webui/icons/. They're separated so
   they can be stripped out and bundled with the converted HTML help.

4. Other images are in ./docs/images/

## Workflow/Notes

The easiest way to preview changes is to run mkdocs serve from the root directory. That will give you a live preview
in your browser, so you can see what it all looks like before committing any changes.

Once you've made changes, simply add/commit them as you would with any other git workflow.

To rebuild the internationalised html pages, run 'make' from the root directory.

At the moment, there's a resync.sh shell script that builds the source (EN) site and syncs it to tvheadend.github.io. 
This isn't the right way to do it - instead, we should sync the output of make - so ./mkdocs/en/site as a default. 

##TO-DO

###Structure

We need to determine the structure of the internationalised pages, plus how we handle multiple application versions
(e.g. 4.0 and 4.2/master). It's perfectly feasible to push these to separate project github repositories  - see 
https://github.com/ProfYaffle, specifically, the ProfYaffle.gihub.io, en and fr repositories and how they appear as
https://profyaffle.github.io/, https://profyaffle.github.io/en/ and https://profyaffle.github.io/fr/.

It probably makes more sense, though, to push them to ./en/, ./cz/, and similar given the number of languages we've
collected on Transifex for the web UI. 

Whichever way we go, we will need some kind of version selector or landing page so you can toggle between them,
even if default redirects to ./en/. Have a look at the selector on readthedocs: https://docs.readthedocs.org/ 
and how it redirects to https://docs.readthedocs.org/en/latest/ with the selector in the lower left.

The mkdocs team is considering how to implement multi-version support. Their preference is to build directly from
git tags; currently, perexg has implemented inline tags (e.g. <tvhversion till="x.x"> and <tvhversion from="y.y">),
so we'll need to see how these play together. Ideally, mkdocs will have a language/version switcher which we can
point to the different locations irrespective of where they're physically hosted (either as subdrs in this structure or as a separate repo).

Ref: https://github.com/mkdocs/mkdocs/issues/617
Ref: https://github.com/mkdocs/mkdocs/issues/211
Ref: https://github.com/mkdocs/mkdocs/issues/193

###ToC/Theme

The other outstanding issue with mkdocs is the way it handles a large number of entries on the table of contents.

* On the readthedocs theme, you get an ever-growing list in the ToC. The intent is to implement a 'rollup' function of some
kind, as can be seen on the readthedocs pages above.

Ref: https://github.com/mkdocs/mkdocs/issues/588

* On the mkdocs theme, you don't get the same issue as the menus are cascading. However, it has different problems
if you have too many entries at the top level, so structure would need to be considered.

Ref: https://github.com/mkdocs/mkdocs/issues/210

###Sync

As above - we need to adjust resync.sh so it pushes the internationalied output, even if it's just the en pages at the moment.

More fundamentally, we need to have some way to push all of the internationalised pages at the same time, within whatever structure is created as above.
