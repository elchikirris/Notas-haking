Our flag printing service has started glitching!
Additional details will be available after launching your challenge instance.

----------
#Solución 

```
elchikirris-picoctf@webshell:~$ nc nc saturn.picoctf.net 49166
nc: port number invalid: saturn.picoctf.net
elchikirris-picoctf@webshell:~$ nc saturn.picoctf.net 49166
'picoCTF{gl17ch_m3_n07_' + chr(0x62) + chr(0x64) + chr(0x61) + chr(0x36) + chr(0x38) + chr(0x66) + chr(0x37) + chr(0x35) + '}'
^Z
[3]+  Stopped                 nc saturn.picoctf.net 49166
elchikirris-picoctf@webshell:~$ python
Python 3.10.12 (main, Feb  4 2025, 14:57:36) [GCC 11.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> 'picoCTF{gl17ch_m3_n07_' + chr(0x62) + chr(0x64) + chr(0x61) + chr(0x36) + chr(0x38) + chr(0x66) + chr(0x37) + chr(0x35) + '}'
'picoCTF{gl17ch_m3_n07_bda68f75}'
```

'picoCTF{gl17ch_m3_n07_bda68f75}'

-----
#Notas 
Pues no sabia que podiamos hacer varias caracteres en python, usando su interprete que es muuuy sencillo de utilizar 


#referencias 