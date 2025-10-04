# root me writeups
## HTTP source
- we inspect the site
- we will find a a comment having the password for login
- and then we are done
## HTTP IP bypass
- the site says our ip is not right ,thus we need to enter credentials to enter
- thus we put this site on burpsuite
- then we will use the request header 'X-Forwarded-For' to spoof our IP
- also from the ref. text , we will try common private addr, the correct one is '10.0.0.0'
- in burpsuite we can enter this header manually or use match and replace , which does this automatically
- thus when we reload the site ,we get the password
## HTTP User Agent
- well as the title suggest , we will use the header 'User-Agent' to impersonate as admin
- basically this header tell which user is requestinf the request
- so when we add this to the request 'User-Agent: admin' we get the password
## HTTP Open redirecting
- well in this chall, we are supposed to open/request another site other than the given ones
- when we look at the the request , we can see two parts u and h
- u is the url link obv, the h can be found when we try reuqesting another url , the site shows up incorrect hash
- since we know now h is a hash, we can try the hash in hash identifier(search google for it)
- the hash h is md5 hash,and is basically the hash of u
- so we wiil write google.com in u and wirte the md5 hash of 'google.com' in h
- thus we solve the chall
## HTTP Directory Indexing
-  well this chall is basically a vuln in which we can access admin dir just by appending /admin to the url
-  so when we do this we see some directory , and to go these dir we will append /dir_name to url
-  and thus after goning through all and getting rickrolled(kinda), the password is in /admin/backup/admin.txt
