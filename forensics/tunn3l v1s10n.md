# tunn3l v1s10n

**Flag:** `picoCTF{qu1t3_a_v13w_2020}`

How you approached the challenge:

- step 1
first i learned no. of ways to identify a file
the one i used was hexadecimal signature of file
which basically means seeing the first few bytes of files and then comparing them to a llist to see which file it is 

- step 2
here the given file was bmp image (also tunn3l v1s10n file is also a bmp image file  )
when opened with photos it wasn't opening which means it was corrupted
on seeing it in the hex editor we see "ba d0" in two places in the header
on further research and comparing it normal bmp image the correct hex was 36 00 and 28 00

- step 3
now we can see the image but it is not the whole as the image has weird dimensions(1134x306)
then by replacing the hexes in the header which stored dim of image to (1134x850)(used trial and error to find it)
we can see the whole image which contains the flag



What you learned through solving this challenge:

1. how to identiify file using hex signatures
2. how to edit hex headeer to change its properties


Other incorrect methods you tried:

- tried to many online file file type detector
- tried to convert into some other form

References

- internet
- wikipedia
