NiftyStuff (Scripts/Utils)
==========================
A bunch of small useful(less) scripts and utils I wrote (and then used) over the time.

### BatchFileRename:
A python script renaming listed in 'rename.txt' files in the current folder. An example of 'rename.txt' included.

### StackOverflowVotes:
A python script for calculating votes distribution among all <a href="http://stackoverflow.com/">StackOverflow</a> questions (result of the testrun on 19-20.03.2013 and its visualization using Chart.js are included). What it does is:
* Downloads HTML of all question teasers on StackOverflow to the folder where the script is executed (damn right, ALL of them, appr. 14GB at the time of writing (read: 14GB traffic)).
* Parses all that data - exctracts all vote numbers.
* Counts the number of questions for each vote number and writes the result in 'result_votes_formatted.txt'.

Enjoy and contact <a href="https://twitter.com/qutebits">@qutebits</a>
