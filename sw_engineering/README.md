First
=====

* Form groups of 4 or 5.
* Pick someone in the group on whose repo you will work.
* Have that person add everyone else as collaborators on the repo.
* Within each group, split into two subgroups.

Building a Library of Code you Trust
====================================

If I handed you some code, would you trust it? Do you trust your own code?
Today you're going to learn how to write tests for your software so you can
be confident it does what you expect it to.

We've got a bunch of field observation data that looks something like this:

    2011-04-22 21:06 Grizzly 36
    2011-04-23 14:12 Elk 25
    2011-04-23 10:24 Elk 26
    2011-04-23 20:08 Wolverine 31
    2011-04-23 18:46 Muskox 20

There's a date, time, animal type, and number seen (yes, grizzlies come in
herds now). Our goal today is to write a command line script that will show the
average number of a certain animal seen per sighting in a certain data file.
For example, for the data above and the input "Elk" our script would show 25.5.

Of course, there are many other kinds of analysis we could do with data like
this, so we should do what we can to write code that doesn't make assumptions
about how it will be used.

I've already written the script part of this, see
[mean_animals.py](./mean_animals.py). What we need to write today is the
library code the script calls.

Demo
----

* First, let's look at the `read_animals` function, and then write a test
    for it. We'll use the [animals.txt](./animals.txt) file for testing because
    it contains a manageable number of entries.

Exercises
---------

1. Now that the `read_animals` function works we can write one for calculating
    the mean of some numbers. In each group pick one sub-group to write the
    function and the other will write tests for it. (You'll swtich in the
    next exercise.) See if you can write an un-breakable function, or see if
    you can break what your teammates are writing!

    Once you're done writing the function or tests, commit and push your work
    to the group repo. When everyone is done you can pull the results and
    see how you did!

2. Repeat the above for the `filter_animals_by_kind` function, but switch
    roles from last time so the other half of your group gets to write some
    tests.

With those functions written we should be able to use the command line script.
Does it work?
