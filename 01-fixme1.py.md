Descripción
Fix the syntax error in this Python script to print the flag.[Download Python script](https://artifacts.picoctf.net/c/27/fixme1.py)


------
#Solución 
```
elchikirris-picoctf@webshell:~$ wget https://artifacts.picoctf.net/c/27/fixme1.py
--2025-09-10 16:51:47--  https://artifacts.picoctf.net/c/27/fixme1.py
2025-09-10 16:51:47 (530 MB/s) - 'fixme1.py' saved [837/837]

elchikirris-picoctf@webshell:~$ python fixme1.py 
  File "/home/elchikirris-picoctf/fixme1.py", line 20
    print('That is correct! Here\'s your flag: ' + flag)
IndentationError: unexpected indent
elchikirris-picoctf@webshell:~$ nano fixme1.py 
elchikirris-picoctf@webshell:~$ python fixme1.py 
That is correct! Here's your flag: picoCTF{1nd3nt1ty_cr1515_182342f7}
elchikirris-picoctf@webshell:~$ 

```
picoCTF{1nd3nt1ty_cr1515_182342f7}

-------------------
#Notas 
nano. Es un editor de texto, ahi podemos editar programas por ejemplo de python 
#referencias 