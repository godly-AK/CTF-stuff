# ARM assembly 1

**Flag:** `picoCTF{0000004d}`

How you approached the challenge:

- step 1
first i tried to understand what was happening in the code and tried all the cmds

- step 2
i understood that program was shifting 58(111010) by 2 to left(11101000) which makes it 232

- step 3
then the function will divide it by 3 which makes it 77

- step 4
now it will subtract the argument from 77
if 0 then win will be printed 
else lose
so the argument should be 77

What you learned through solving this challenge:

1. lsl w0, w1, w0:
    - Logical shift left: Shifts the bits in w1 to the left by the number of positions specified in w0
2. sdiv w0, w1, w0:
    - Signed division: Divides w1 by w0 and stores the result in w0.
3. sub w0, w1, w0 ;
    - subtract: w1-w0;

Other incorrect methods you tried:

- put the flag wrongly by only putting 4d and  not giving zeros 

References

- chatgpt to learn cmds
- video links provided
