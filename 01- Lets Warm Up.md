
Descripción.
If I told you a word started with 0x70 in hexadecimal, what would it start with in ASCII?

Solución.  
Forma 1

P
picoCTF(p)

Forma 2
```
elchikirris-picoctf@webshell:~$ python
Python 3.10.12 (main, Feb  4 2025, 14:57:36) [GCC 11.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> int(0x70)
112
>>> chr(112)
'p'
>>> 
```

Notas
Siempre hay que poner la solución en el formato de la bandera, fui haciendo el trabajo junto con el profe

Referencias 
https://www.chileoffshore.com/es/toolkits/basic-conversion/hexa-to-ascii
