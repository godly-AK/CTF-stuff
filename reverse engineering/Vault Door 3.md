# Vault Door 3

**Flag:** `picoCTF{jU5t_a_s1mpl3_an4gr4m_4_u_c79a21}`

How you approached the challenge:

- step 1

first i learn basic java 

- step 2

then understood the loop
`for (i=0; i<8; i++) {
            buffer[i] = password.charAt(i);// first 7 char of the final string is same as the input pass
        }
        for (; i<16; i++) {
            buffer[i] = password.charAt(23-i);// 15th index char in pass is inserted in 8th of buffer and 14 th in 9th ,so on
        }
        for (; i<32; i+=2) {
            buffer[i] = password.charAt(46-i);// even indices of pass from 16 th to 30th  are inserted in buffer in reverse position(16th into 30th)
        }
        for (i=31; i>=17; i-=2) {
            buffer[i] = password.charAt(i);// odd indices of pass from 31st to 17th is inserted in same position in buffer
        }`

- step 3

did these loops in reverse by making a table
and got 'jU5t_a_s1mpl3_an4gr4m_4_u_c79a21'

- terminal

Enter vault password: 
picoCTF{jU5t_a_s1mpl3_an4gr4m_4_u_c79a21}
Access granted.





What you learned through solving this challenge:

1. basic java

References

- friends(to learn java only)
- internet
