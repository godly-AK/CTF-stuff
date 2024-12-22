# GDB baby step 3

**Flag:** `picoCTF{0x6bc96222}`

How you approached the challenge:

- step 1
we will do load the file in gdb and since we need to understand when the elf file is loading our value we will use `layout asm` cmd

- step 2
  we can see the value is stored at -0x4(%rbp) and then eax registers are stored and then rbp is popped

-step 4
 so we will first break main,run and break at pop rbp 
- step 5
  then we continue and then we use x/4xb $rbp-4(this is the to point addr in gdb it basically means the same thing) to get the four bytes and the flag

What you learned through solving this challenge:

1. how to see disassmbled code
2. a bit of assembly code

Other incorrect methods you tried:

- tried using break at exactly when value was assinged didn't took the whole process in consideration


References

- internet
- copilot
  
