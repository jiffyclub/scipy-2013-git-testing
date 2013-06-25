# Local Version Control

## Example: Wolfman

My friend Lupine Wolfe worked hard on an important project all day. He finished
before dinner time, relieved to be ready for the deadline in the morning. The
sun set, the full moon rose, and in the morning Lupine awoke with no memory of
the previous evening. He sat down at his computer and discovered to his horror
that overnight, while transformed as a werewolf, he had replaced all of the code
with nonsense. But, Lupine breathed a sigh of relief, because he had been using
version control.  He was able to examine the record of his actions overnight and
execute one simple command that reverted the code to the state it was in before
the moon rose.

What would happen to your code on a full moon?

## git : What is Version Control ?

Very briefly, version control is a way to

- keep a backup of changing files
- store a history of those changes
- and manage merging of changes in versions with different change sets.

There are a lot of verson control systems. Wikipedia
provides both a nice vocabulary list and a fairly complete table of some
popular version control systems and their equivalent commands.

Today, we'll be using git. Git is an example of a distributed version
control system, distinct from centralized verson control systems. I'll
make the distinction clear later, but for now, the list below will
suffice.

Version Control System Tool Options

- **Distributed**
  - Decentralized CVS (dcvs)
  - mercurial (hg)
  - git (git)
  - bazaar (bzr)
- **Centralized**
  - concurrent versions system (cvs)
  - subversion (svn)

## git --help : Getting Help

The first thing I like to know about any tool is how to get help. From
the command line type

    $ man git

The manual entry for the git version control system will appear before
you. You may scroll through it using arrows, or you can search for
keywords by typing **/** followed by the search term. I'm interested in
help, so I type **/help** and then hit enter. It looks like the syntax
for getting help with git is **git --help**.

To exit the manual page, type q.

Let's see what happens when we type :

    $ git --help

Excellent, it gives a list of commands it is able to help with, as well
as their descriptions.

    $ git --help
    usage: git [--version] [--exec-path[=<path>]] [--html-path]
               [-p|--paginate|--no-pager] [--no-replace-objects]
               [--bare] [--git-dir=<path>] [--work-tree=<path>]
               [-c name=value] [--help]
               <command> [<args>]

    The most commonly used git commands are:
       add        Add file contents to the index
       bisect     Find by binary search the change that introduced a bug
       branch     List, create, or delete branches
       checkout   Checkout a branch or paths to the working tree
       clone      Clone a repository into a new directory
       commit     Record changes to the repository
       diff       Show changes between commits, commit and working tree, etc
       fetch      Download objects and refs from another repository
       grep       Print lines matching a pattern
       init       Create an empty git repository or reinitialize an existing one
       log        Show commit logs
       merge      Join two or more development histories together
       mv         Move or rename a file, a directory, or a symlink
       pull       Fetch from and merge with another repository or a local branch
       push       Update remote refs along with associated objects
       rebase     Forward-port local commits to the updated upstream head
       reset      Reset current HEAD to the specified state
       rm         Remove files from the working tree and from the index
       show       Show various types of objects
       status     Show the working tree status
       tag        Create, list, delete or verify a tag object signed with GPG

    See 'git help <command>' for more information on a specific command.

## git config : Control the behavior of git

     $ git config --global user.name "YOUR NAME"
     $ git config --global user.email "YOUR EMAIL"
     $ git config --global core.editor "nano"
     $ git config --global color.ui "auto"

## git init : Creating a Local Repository

To keep track of numerous versions of your work without saving numerous copies,
you can make a local **repository** for it on your computer.

What git does is to save
the first version, then for each subsequent version it records the difference
between the new version and the one before it. With this compact information,
git is able to recreate any version on demand by adding the changes to the
original in order up to the version of interest.

To create your own local (on your own machine) repository, you must
initialize the repository with the infrastructure git needs in order to
keep a record of things within the repsitory that you're concerned
about. The command to do this is **git init** .

### Exercise : Create a Local Repository

Step 1 : Initialize your repository.

    $ cd
    $ mkdir good_science
    $ cd good_science
    $ git init
    Initialized empty Git repository in /Users/swc/good_science/.git/

Step 2 : Browse the directory's hidden files to see what happened here.
Open directories, browse file contents. Learn what you can in a minute.

    $ ls -A
    .git
    $ cd .git
    $ ls -A
    HEAD        config      description hooks       info        objects     refs


## git add : Staging Files

For the git repository to know which files within this directory you
would like to keep track of, you must add them. First, you'll need to
create one, then we'll learn the **git add** command.

### Exercise : Add a File to Your Local Repository

Step 1 : Create a file to add to your repository.

    $ touch readme.rst

Step 2 : Inform git that you would like to keep track of future changes
in this file.

    $ git add readme.rst

## git status : Checking the Status of Your Local Copy

The files you've created on your machine are your local "working" copy.
The changes your make in this local copy aren't backed up online
automatically. Until you commit them, the changes you make are local
changes. When you change anything, your set of files becomes different
from the files in the official repository copy. To find out what's
different about them in the terminal, try:

    $ git status
    # On branch master
    #
    # Initial commit
    #
    # Changes to be committed:

    #   (use "git rm --cached <file>..." to unstage)
    #
    #       new file:   readme.rst
    #

The result above indicates that the current difference
between the repository HEAD (which, so far, is empty) and your
good\_science directory is this new readme.rst file.

## git commit : Saving a Snapshot

In order to save a snapshot of the current state (revision) of the
repository, we use the commit command. This command is always associated
with a message describing the changes since the last commit and
indicating their purpose. Informative commit messages will serve you
well someday, so make a habit of never committing changes without at
least a full sentence description.

**ADVICE: Commit often**

In the same way that it is wise to often save a document that you are
working on, so too is it wise to save numerous revisions of your code.
More frequent commits increase the granularity of your **undo** button.

There are no hard and fast rules, but good commits are atomic: they are the
smallest change that remains meaningful.

### Exercise : Commit Your Changes

Step 1 : Commit the staged changes of the file you've added to your repository.

    $ git commit
    [master (root-commit) 9ca8be0] This is my first commit.
    0 files changed
    create mode 100644 readme.rst

Step 2 : Add a commit message. Git will send you to your preferred text editor.
Create a message, then save and exit.

Step 3 : Admire your work.

    $ git status
    # On branch master
    nothing to commit (working directory clean)

Now, one revision is great, but lots are better.

So far, we've learned that the workflow should be :

- make changes
- git add the files you want to stage for a commit
- git commit those files
- fill out the message

### Exercise : Stage and Commit New Changes

Step 1 : Edit your readme file. It should say something like :


```

=========
Welcome
=========

This is my readme file.

```

Step 2 : Stage it for the snapshot (git add)

Step 3 : Commit the snapshot (git commit)

Step 4 : Add a meaningful commit message.

**Four steps is a lot of steps!!** Command line flags can cut this way down. Some
useful flags for git commit include  :

     -m : add a commit message from the command line
     -a : automatically stage files that have been modified or deleted
     -F : add a commit message from a file
     --status : include the output of git status in the commit message
     --amend : fix the commit message at the repository tip

**ADVICE: Write good commit messages**

## Exercise : Commit in One Step

Step 1 : Edit your readme file to tell us whose it is. (This is Katy's readme...)

Step 2 : Add, Commit, and append your log Message with one command.


## git diff : Viewing the Differences

There are many diff tools.

If you have a favorite you can set your default git diff tool to execute
that one. Git, however, comes with its own diff system.

Let's recall the behavior of the diff command on the command line.
Choosing two files that are similar, the command :

    $ diff file1 file2

will output the lines that differ between the two files. This
information can be saved as what's known as a patch, but we won't go
deeply into that just now.

The only difference between the command line diff tool and git's diff
tool is that the git tool is aware of all of the revisions in your
repository, allowing each revision of each file to be treated as a full
file.

Thus, git diff will output the changes in your working directory that
are not yet staged for a commit. To see how this works, make a change in
your readme.rst file, but don't yet commit it.

    $ git diff

A summarized version of this output can be output with the --stat flag :

    $ git diff --stat

To see only the differences in a certain path, try:

    $ git diff HEAD -- [path]

To see what IS staged for commit
you can try :

    $ git diff --cached

## git log : Viewing the History

A log of the commit messages is kept by the repository and can be
reviewed with the log command.


    $ git log
    commit 2e728590b9e7c61b1c52e2c0a66b6273449f1bc3
    Author: Katy Huff <katyhuff@gmail.com>
    Date:   Fri Jun 21 18:21:35 2013 -0500

        Explained, this is Katy's readme.

    commit 9a01fdb93efd7c1e52f4da29aa5fa485131aed9b
    Author: Katy Huff <katyhuff@gmail.com>
    Date:   Fri Jun 21 18:20:50 2013 -0500

        Added a message.

    commit 9ca8be0222337f3a13a8e96ea9da8ab8fdb2a4e7
    Author: Katy Huff <katyhuff@gmail.com>
    Date:   Fri Jun 21 18:19:38 2013 -0500

        This is my first commit.

There are some useful flags for this command, such as

    -p
    -3
    --stat
    --oneline
    --graph
    --pretty=short/full/fuller/oneline
    --since=X.minutes/hours/days/weeks/months/years or YY-MM-DD-HH:MM
    --until=X.minutes/hours/days/weeks/months/years or YY-MM-DD-HH:MM
    --author=<pattern>

## git reset : Unstaging a Staged File

You can use git reset to unstage a staged file or to roll back a file or files to a previous revision.

If you added a file to the staging area that you didn't mean to add, you can use reset to take it out of staging.

    git reset filename     (opposite of 'git add filename')

## git reset : Return to a previous revision

If you want to return the repository to a previous version, use reset with the commit number :

    git reset [<mode>] [<commit>]

Reset has some useful mode flags.

    --soft : leaves the contents of your files and repository index alone, but resets repository head
    --mixed : resets the index and repository head, but not the contents of your files
    --hard : returns the contents of all files and the repository index to the commit specified

## git checkout : Discarding unstaged modifications

    git checkout -- filename

Note, git checkout has other purposes, which we'll see soon.

### Exercise :

Step 1 : Create 5 files in your directory with one line of content in each file.

Step 2 : Commit the files to the repository.

Step 3 : Change 2 of the 5 files and commit them.

Step 4 : Undo the changes in step 3)

Step 5 : Print out the last entry in the log.

## git revert : Discard revisions

Much like git reset --hard , but with more permanence, git revert is a helpful
tool when you **really** want to erase history, for example, if you've
accidentally committed something with private or proprietary information.

    git revert <commit>


## git rm : Removing a File

   git rm filename   (Removes a file from the repository)

## git branch : Listing, Creating, and Deleting Branches

Branches are parallel instances of a repository that can be edited and
version controlled in parallel. They are useful for pursuing various
implementations experimentally or maintaining a stable core while
developing separate sections of a code base.

Without an argument, the **branch** command lists the branches that
exist in your repository.

    $ git branch
    * master

The master branch is created when the repository is initialized. With an
argument, the **branch** command creates a new branch with the given
name.

    $ git branch experimental
    $ git branch
    * master
      experimental

To delete a branch, use the **-d** flag.

    $ git branch -d experimental
    $ git branch
    * master

## git checkout : Switching Between Branches, Abandoning Local Changes

The **git checkout** command allows context switching between branches
as well as abandoning local changes.

To switch between branches, try

    $ git branch newbranch
    $ git checkout newbranch
    $ git branch

How can you tell we've switched between branches? When we used the
branch command before there was an asterisk next to the master branch.
That's because the asterisk indicates which branch you're currently in.

## git merge : Merging Branches

At some point, the experimental branch may be ready to become part of
the core or two testing branches may be ready to be combined for further
integration testing. The method for combining the changes in two
parallel branches is the **merge** command.

### Exercise : Create Two Branches

Step 1 : Create two new branches and list them

    $ git branch us
    $ git branch texas

Step 2 : Add files describing each entity. In the us branch, include at least a
file called president. For texas, of
course, you'll need a file called governor. You'll probably also want one called flower.

    $ git checkout us
    Switched to branch 'us'
    $ touch president
    $ git add presdient
    $ git commit -am "Added president to the us branch."
    $ git checkout texas
    Switched to branch 'texas'
    $ touch flower
    $ git add flower
    $ git commit -am "Added bluebonnets to the texas branch."

Step 3 : Merge the two branches into the core

    $ git checkout us
    Switched to branch 'us'
    $ git merge texas
    Merge made by recursive.
     0 files changed, 0 insertions(+), 0 deletions(-)
      create mode 100644 flower
    $ git checkout master
    Switched to branch 'master'
    $ git merge us
    Updating 1863aef..ce7e4b5
    Fast-forward
     0 files changed, 0 insertions(+), 0 deletions(-)
     create mode 100644 president
     create mode 100644 flower

## Dealing with Conflicts

We notice that the national anthem isn't there, so we add a file called
national_anthem to the us branch.

    $ git checkout us
    $ touch national_anthem
    $ git add national_anthem
    $ git commit -am "Added star spangled banner to the us branch."

Next, of course, we put on our Wranglers and Stetsons and do the same for the
Texas branch.

    $ git checkout texas
    $ touch national_anthem
    $ git add national_anthem
    $ git commit -am "Added Texas, Our Texas to the texas branch."

If we merge them? What happens?

## git clone : Copying a Repository

There are a lot of open source code development projects are kept in
repositories online and the best way to acquire and keep up to date with those is to
'clone' them with git.

When you clone the Original repository, the one that is created on your
local machine is a copy, and will behave as a fully fledged local
repository locally. However, with the right configuration, it will be
able to pull changes from collaborators to your local machine and push
your changes to the Original repository. We'll get to that soon, but for
now, let's just clone the repository from GitHub so that you have a local copy
that can be kept up to date.

### Exercise : Cloning a Repository from GitHub

Step 1 : Pick any repository you like. There are many cool projects
hosted on github. Take a few minutes here, and pick a piece of code.

Step 2 : Clone it. If you didn't find anything cool, you can chose the
"instructional" Spoon-Knife repository:

    $ git clone git@github.com/octocat/Spoon-Knife.git
    Cloning into Spoon-Knife...
    remote: Counting objects: 24, done.
    remote: Compressing objects: 100% (21/21), done.
    remote: Total 24 (delta 7), reused 17 (delta 1)
    Receiving objects: 100% (24/24), 74.36 KiB, done.
    Resolving deltas: 100% (7/7), done.

Step 3 : You should see many files download themselves onto your
machine. Let's make sure it worked. Change directories to the source
code and list the contents.

    $ cd Spoon-Knife
    $ ls

## git pull : Pulling updates from the Original Repository

Updating your repository is like voting. You should update early and
often especially if you intend to contribute back to the upstream
repository and particularly before you make or commit any changes. This
will ensure you're working with the most up-to-date version of the
repository. Updating won't overwrite any changes you've made locally
without asking, so don't get nervous. When in doubt, update.

    $ git pull
    Already up-to-date.

Since we just pulled the repository down, we will be up to date unless
there has been a commit by someone else to the Original repository in
the meantime.

## Resources

[git book](http://git-scm.com/book)
