Descripción 
Can you make sense of this file?Download the file [here](https://artifacts.picoctf.net/c/473/enc_flag).

---
#Solución
```
elchikirris-picoctf@webshell:~$ wget https://artifacts.picoctf.net/c/473/enc_flag
--2025-09-05 02:11:56--  https://artifacts.picoctf.net/c/473/enc_flag
Resolving artifacts.picoctf.net (artifacts.picoctf.net)... 3.170.131.72, 3.170.131.33, 3.170.131.77, ...
Connecting to artifacts.picoctf.net (artifacts.picoctf.net)|3.170.131.72|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 349 [application/octet-stream]
Saving to: 'enc_flag'

enc_flag                                                          100%[=============================================================================================================================================================>]     349  --.-KB/s    in 0s      

2025-09-05 02:11:56 (223 MB/s) - 'enc_flag' saved [349/349]

elchikirris-picoctf@webshell:~$ ls
Addadshashanammu  Addadshashanammu.zip  Addadshashanammu.zip.1  README.txt  enc_flag  file  flag  ltdis.sh  static  static.ltdis.strings.txt  static.ltdis.x86_64.txt  strings  warm
elchikirris-picoctf@webshell:~$ cat enc_flag 
VmpGU1EyRXlUWGxTYmxKVVYwZFNWbGxyV21GV1JteDBUbFpPYWxKdFVsaFpWVlUxWVZaS1ZWWnVh
RmRXZWtab1dWWmtSMk5yTlZWWApiVVpUVm10d1VWZFdVa2RpYlZaWFZtNVdVZ3BpU0VKeldWUkNk
MlZXVlhoWGJYQk9VbFJXU0ZkcVRuTldaM0JZVWpGS2VWWkdaSGRXCk1sWnpWV3hhVm1KRk5XOVVW
VkpEVGxaYVdFMVhSbHBWV0VKVVZGWm9RMlZzV2tWUmJFNVNDbUpXV25wWmExSmhWMGRHZEdWRlZs
aGkKYlRrelZERldUMkpzUWxWTlJYTkxDZz09Cg==
```
picoCTF{base64_n3st3d_dic0d!n8_d0wnl04d3d_dfe803c6}
Usando cyberchef

---
#Notas 
#referencias 