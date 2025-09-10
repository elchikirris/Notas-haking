Descripción
Run the Python script and convert the given number from decimal to binary to get the flag.

---
#Solución 
```
elchikirris-picoctf@webshell:~$ wget https://artifacts.picoctf.net/c/22/convertme.py
elchikirris-picoctf@webshell:~$ ls
Addadshashanammu      Addadshashanammu.zip.1  big-zip-files      code.py       convertme.py  file   files.zip  ltdis.sh  static                    static.ltdis.x86_64.txt  warm
Addadshashanammu.zip  README.txt              big-zip-files.zip  codebook.txt  enc_flag      files  flag       runme.py  static.ltdis.strings.txt  strings
elchikirris-picoctf@webshell:~$ python3 convertme.py 
If 25 is in decimal base, what is it in binary base?
Answer: 11001
That is correct! Here's your flag: picoCTF{4ll_y0ur_b4535_762f748e}
```


------
#Notas 
```python
numero = 25
print(bin(numero)[2:])  
```
y me dio el resultado

#referencias 
