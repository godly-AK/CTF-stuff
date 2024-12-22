# Challenge name

**Flag:** `picoCTF{n33d_a_lArg3r_e_606ce004}`

How you approached the challenge:

- step 1
since i had no cipher program , i tried it to put it in a tool called dcode rsa cipher

- step 2
that with given details gave me the flag but i still researched how did it do it

- step 3
well the hint was small e attack basically when the e is too small there is little difference between n and m
so we can directly cube root as e is 3 then we get flag in integer and now we need to convert ascii
- step4 w
  we will first convert hex then into byte array then into ascii
  '''
  hex_string = format(m_int, 'x')
message = bytearray.fromhex(hex_string).decode()
print("Message: {}".format(message))
  '''



What you learned through solving this challenge:

1. RSA
2. small e attack


References

- dcode
- copilot
- internet
