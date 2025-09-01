Can you find the flag in [file](https://jupiter.challenges.picoctf.org/static/515f19f3612bfd97cd3f0c0ba32bd864/file)? This would be really tedious to look through manually, something tells me there is a better way.

--------------------------------------------------------------------------------------------------------
#Solución 
Hacemos el get del file que nos pide el reto
```
elchikirris-picoctf@webshell:~$ man grep
elchikirris-picoctf@webshell:~$ wget https://jupiter.challenges.picoctf.org/static/515f19f3612bfd97cd3f0c0ba32bd864/file
--2025-09-01 17:08:05--  https://jupiter.challenges.picoctf.org/static/515f19f3612bfd97cd3f0c0ba32bd864/file
Resolving jupiter.challenges.picoctf.org (jupiter.challenges.picoctf.org)... 3.131.60.8
Connecting to jupiter.challenges.picoctf.org (jupiter.challenges.picoctf.org)|3.131.60.8|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 14551 (14K) [application/octet-stream]
Saving to: 'file'

file                                                      100%[==================================================================================================================================>]  14.21K  --.-KB/s    in 0s      

2025-09-01 17:08:06 (463 MB/s) - 'file' saved [14551/14551]

elchikirris-picoctf@webshell:~$ ls
README.txt  file
```
Hacemos una busqueda desde terminal 

```
elchikirris-picoctf@webshell:~$ wc file 
    6   315 14551 file
elchikirris-picoctf@webshell:~$ grep 'picoCTF' file
picoCTF{grep_is_good_to_find_things_5af9d829}
elchikirris-picoctf@webshell:~$ 
```

 respuesta =picoCTF{grep_is_good_to_find_things_5af9d829}

----------------------------------------------------------------------------------------------------------------------
#Notas 
wc- es para contar los caracteres de un archivo 
file - determina el tipo de archivo 
