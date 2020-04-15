# by far the coolest thing here
# compile my main.cpp
# compile model answer I get off the internet or a slow brute force solution I can write
# run test case generator and redirect output to a file called input haha
# run both programs and compare their outputs together
# is no diff, pun intended, is found keep generating random test cases
# is a difference is found output it in the terminal for convenience

g++ ../main.cpp -o main.out
g++ ans.cpp -o ans.out

for (( c=1; ; c++ ))
do  
    echo $c
    python3 test.py $c > input
    ./main.out < input > outme
    ./ans.out  < input > outans
    diff outme outans || break
done
clear
printf '****************************************************\n'
printf '#################################\ntestcase : '
cat input
printf '#################################\n\n'
printf '\nmy answer :\n'
cat outme

printf '\n\n\nmodel answer:\n'
cat outans
printf '\n****************************************************\n'