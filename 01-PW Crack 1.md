Can you crack the password to get the flag?Download the password checker [here](https://artifacts.picoctf.net/c/10/level1.py) and you'll need the encrypted [flag](https://artifacts.picoctf.net/c/10/level1.flag.txt.enc) in the same directory too.

----------
#Solución 
```bash
elchikirris-picoctf@webshell:~$ wget https://artifacts.picoctf.net/c/10/level1.py
2025-09-10 17:06:53 (252 MB/s) - 'level1.py.1' saved [876/876]

elchikirris-picoctf@webshell:~$ python3 level1.py 
Traceback (most recent call last):
  File "/home/elchikirris-picoctf/level1.py", line 13, in <module>
    flag_enc = open('level1.flag.txt.enc', 'rb').read()
FileNotFoundError: [Errno 2] No such file or directory: 'level1.flag.txt.enc'
elchikirris-picoctf@webshell:~$ wget https://artifacts.picoctf.net/c/10/level1.flag.txt.enc
elchikirris-picoctf@webshell:~$ python3 level1.py 
Please enter correct password for flag: 691d        
Welcome back... your flag, user:
picoCTF{545h_r1ng1ng_56891419}
```

----
#Notas 
#referencias 
