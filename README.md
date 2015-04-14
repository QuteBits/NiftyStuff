NiftyStuff (Scripts/Utils)
==========================
A bunch of small useful(less) scripts and utils I wrote (and then used) over the time.

### mongoJSON_to_parseJSON:
A python script converting a MongoDB JSON to a valid Parse.com JSON. An example of 'rename.txt' included.

### Batch_File_Rename:
A python script renaming listed in 'rename.txt' files in the current folder. An example of 'rename.txt' included.

### Stack_Overflow_Votes:
A python script for calculating votes distribution among all <a href="http://stackoverflow.com/">StackOverflow</a> questions (result of the testrun on 19-20.03.2013 is included). What it does is:
* Downloads HTML of all question teasers on StackOverflow to the folder where the script is executed (that's damn right, ALL of them, appr. 14GB at the time of writing).
* Parses all that data - exctracts all vote numbers.
* Counts the number of questions for each vote number and writes the result in 'result_votes_formatted.txt'.

Enjoy and contact <a href="https://twitter.com/qutebits">@qutebits</a>
