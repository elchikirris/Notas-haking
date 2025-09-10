Can you crack the password to get the flag?Download the password checker [here](https://artifacts.picoctf.net/c/13/level2.py) and you'll need the encrypted [flag](https://artifacts.picoctf.net/c/13/level2.flag.txt.enc) in the same directory too.

------
#Solución 
```bash
elchikirris-picoctf@webshell:~$ wget https://artifacts.picoctf.net/c/13/level2.py
2025-09-10 17:11:06 (56.1 MB/s) - 'level2.py' saved [914/914]

elchikirris-picoctf@webshell:~$ wget https://artifacts.picoctf.net/c/13/level2.flag.txt.enc
2025-09-10 17:11:19 (1.17 MB/s) - 'level2.flag.txt.enc' saved [31/31]

elchikirris-picoctf@webshell:~$ nano level2.py 
elchikirris-picoctf@webshell:~$ nano level2.py 
elchikirris-picoctf@webshell:~$ python3 level2.py 
Welcome back... your flag, user:
picoCTF{tr45h_51ng1ng_489dea9a}

```
picoCTF{tr45h_51ng1ng_489dea9a}

-----
#Notas 
#referencias 