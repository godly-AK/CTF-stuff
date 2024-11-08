# Trivial File transfer protocol

**Flag:** `picoCTF{h1dd3n_1n_pLa1n_51GHT_18375919}`

How you approached the challenge:

- step 1
first i learned about how tftp works

- step 2
used wireshark to open the file
used tftp.type to see the tftp packets
and then downloaded them by export objects then tftp

- step 3
decoded plan and instructions using ROTI13

- step 4
then installed program.deb on wsl 
but got error which hinted this program is part steghide
also steghide is used to hide bmp files which was also there

- step 5
install steghide 
then learned how to use it 
from plan got the hint that password must be DUEDILLIGENCE

- step 6
tried with all 3 bmp files and the 3rd file gave the flag which simply cat
```
godlyinsane@AKPC:~$ steghide extract -sf ./picture1.bmp -p DUEDILIGENCE
steghide: could not extract any data with that passphrase!
godlyinsane@AKPC:~$ steghide extract -sf ./picture2.bmp -p DUEDILIGENCE
steghide: could not extract any data with that passphrase!
godlyinsane@AKPC:~$ steghide extract -sf ./picture3.bmp -p DUEDILIGENCE
wrote extracted data to "flag.txt".
godlyinsane@AKPC:~$ cat flag.txt
picoCTF{h1dd3n_1n_pLa1n_51GHT_18375919}
```

What you learned through solving this challenge:

1. TFTP
2. wireshark
3. steghide

References

- google
- copilot