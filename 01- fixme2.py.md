Fix the syntax error in the Python script to print the flag.

----------
#Solución 
``` bash
elchikirris-picoctf@webshell:~$ wget https://artifacts.picoctf.net/c/5/fixme2.py
2025-09-10 16:58:12 (360 MB/s) - 'fixme2.py' saved [1029/1029]

elchikirris-picoctf@webshell:~$ python3 fixme2.py 
  File "/home/elchikirris-picoctf/fixme2.py", line 22
    if flag = "":
       ^^^^^^^^^
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
elchikirris-picoctf@webshell:~$ nano fixme2.py 
elchikirris-picoctf@webshell:~$ python3 fixme2.py 
That is correct! Here's your flag: picoCTF{3qu4l1ty_n0t_4551gnm3nt_4863e11b}
```
picoCTF{3qu4l1ty_n0t_4551gnm3nt_4863e11b}

-----------
#Notas 
#referencias 