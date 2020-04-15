# ProblemSolving

I write code in main.cpp and usually I use the other files. But sometimes I get a wrong answer and if I can't find a test case that makes my code fail I'll use the files in the help directory. 

How to use:
Write code in main.cpp
Get a solution that you're sure works and place it in ans.cpp
Write a small test case generator in test.py. Usually is like 5-10 lines.
Then you're done.
Run the tester.sh script and it will keep echoing numbers as long as your main.cpp is correct. Once a different solution is produced the tester exits, outputs the test case and both answers.

Some minor things:
I like to keep thing clean in the help directory so there's a tiny clean.sh script that you can run when you're done.

One other thing:
There's a compile script called sc which will catch index out of bounds errors and integer overflows and issue errors on warnings, and does some sanitizing. It helps me catch stupid mistakes, but it also make code runner slower so there a my normal compile command is the one called "c".

All scripts can be run from a terminal like this:
change directory to correct place
./scriptname # this might require you to change execution permissions - a simple 'chmod' will fix this
or
bash scriptname
