# niteCTF
  ## Mumbo Dumbo
  - flag 'nite{C@TCHME!FY0UCAN}'
  - steps i did
    1. the question asked the user to be deceptive and at the same time not be caught by the bot
    2. since the bot was trying find the deception in my query , i started by simply asking what is the password and continued it till the bot gave me the password
  - incorrect ways: tried using inputing cmds in the query
  - what i learnt
    1. ways to deceive ai chatbot
 ## backtrack
  - flag 'nite{17:00_20February}'
  - steps i did
    1. first i tried to find i f there is any archive for train being late and i found out it is rare for trains to get late for more than 5 mins and if they do get late everyone aboard gets 
       a delay cert which they can show in their office as proof.
    2. on th official website only last 35 days are shown so i needed a way to go back in time , the wayback machine
    3. on wayback machine i pasted the link and start searching for 61 mins late train and i found it in February in a archive of march.

  ## la casa de papel
   - flag 'nite{El_Pr0f3_0f_Prec1s10n_Pl4ns}'
   - steps i did
     1. on observeing the code we can see that in order to surpass alice and get the secret text we need to provide the correct HMAC
     2. now the md5 fn return md5 encypted value in base64 encoded and pratice convo can allow us to get the base64 encoded value with msg we provide
     3. now in the alice fn the condition to get secret text is that we need to provide the hash which is base64 decoded of md5(secret,Bob)
     4. now what we need is to do base64 decoding on the value which pratice convo provides with "Bob"
     5. then we get the secret msg and then we put it into the  vault to get the flag
   - what i learnt : what is md5 encoding

  ## U ARe The detective
   - flag'nite{n0n_std_b4ud_r4t3s_ftw}'
   - step i did
     1. well i first researched what type of file it is and which software opens it
     2. it was a sigrok session file which can be opened with pulseview
     3. now after dwnlding it andopening the file, i needed to choose which decoder to use the question name is the ans UART
     4. now to choose the configuration , i set everthing to default except baud rate and data bits as nothing could be decoded with default
     5. after finding the smallest bit and then baud rate that is 4895000 and data bit set to 7 we get the correct flag
   - incorrect things i did : lots of hit and trials
   - what i learnt : how to use and pulse view to analyse a signal.sr(sigrok session file)
       
