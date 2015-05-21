##Updating the Documentation 1st June 2015

The documentation is written in markdown, and then converted in two 
directions to create both this User Guide and the on-line help files
that are bundled with the application.

Broadly:

1. Install dependencies ([mkdocs](http://www.mkdocs.org/), 
[pandoc](http://pandoc.org/installing.html) and 
[git](https://help.github.com/articles/set-up-git/))

2. Clone the [documentation repository](https://github.com/ProfYaffle/tvheadend-documentation)

3. Make changes locally. Pay close attention to formatting and syntax - 
use the live reload function (`mkdocs serve`) to preview them.

4. When you're happy, push the changes to your remote repository and open 
a pull request

Command sequence (this presumes Linux, but Windows is very similar):

* `cd ~/tvheadend-documentation`
* `git add -A` (presumes to add everything)
* `git commit -m "Summary of changes"`
* `git push`

... and then open the PR on github

To update and resync, someone (me, probably!) needs to:

1. Merge the changes
2. Pull the latest revisions from the repository
3. Convert the webui files: `./convert.sh docs/webui <target_directory>`

To merge the webui files into tvheadend, copy them into `<your tvheadend clone>/docs/html`, 
push them to your remote repository and open a PR to merge them into master.

4. Convert all files: `mkdocs build --clean`
5. Copy the contents of the resultant `site` directory to gihub pages (**Note**: 
this step will become unecessary if and when readthedocs starts autobuilding correctly)

To publish the entire User Guide to gihub, 

* `cd ~/github.io`
* `cp -r ~/tvheadend-documentation/site/* .`
* `git add -A` (presumes to add everything)
* `git commit -m "Resync"` (or whatever your commit message is)
* `git push`

####Other references

* Readthedocs: <https://tvheadend.readthedocs.org/en/stable/>

* Markdown basics: <https://daringfireball.net/projects/markdown/syntax>

* Markdown test: <https://daringfireball.net/projects/markdown/dingus>
