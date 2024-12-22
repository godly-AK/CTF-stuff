# Custom Encryption

**Flag:** `picoCTF{custom_d2cr0pt6d_019c831c}`

How you approached the challenge:

- step 1
on the first look on encryption program we can see that ascii char in integer is getting multiplied by key(35) and 311
now to get original char we can reverse this 
```
original_char = chr(num // (key * 311))
```

- step 2
now we get semi encrypted text to convert this into flag we need to know about XOR
that is for plaintext , ciphertext , key
p xor k is c
c xor k is p
p xor c is k
so first we will the key
for this since we know some part of flag that is 'picoCTF{' we will get some part or the whole real key as the key is nothing but a jumbled "trudeau"

- step 3
  which gives the output "aedurtu" at the start now when put this at the place key we get the flag



What you learned through solving this challenge:

1. XOR encryption


References

- dcode
- internet
- copilot
