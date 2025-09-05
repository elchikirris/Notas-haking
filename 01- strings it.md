Descripción
Can you find the flag in [file](https://jupiter.challenges.picoctf.org/static/5bd86036f013ac3b9c958499adf3e2e2/strings) without running it?

----------
#Solución 
Fui siguiendo los pasos y use el pip, para poder redirigir la salida  a un grep

```
elchikirris-picoctf@webshell:~$ wget https://jupiter.challenges.picoctf.org/static/5bd86036f013ac3b9c958499adf3e2e2/strings
--2025-09-04 02:50:36--  https://jupiter.challenges.picoctf.org/static/5bd86036f013ac3b9c958499adf3e2e2/strings
Resolving jupiter.challenges.picoctf.org (jupiter.challenges.picoctf.org)... 3.131.60.8
Connecting to jupiter.challenges.picoctf.org (jupiter.challenges.picoctf.org)|3.131.60.8|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 776032 (758K) [application/octet-stream]
Saving to: 'strings'

strings                                                   100%[==================================================================================================================================>] 757.84K  1.86MB/s    in 0.4s    

2025-09-04 02:50:36 (1.86 MB/s) - 'strings' saved [776032/776032]

elchikirris-picoctf@webshell:~$ ls
README.txt  file  flag  strings
elchikirris-picoctf@webshell:~$ strings string | grep pico 
strings: 'string': No such file
elchikirris-picoctf@webshell:~$ strings strings | grep pico
picoCTF{5tRIng5_1T_827aee91}
elchikirris-picoctf@webshell:~$ 
```


---------------
#Notas
grep= básicamente hace búsquedas

#referencias 