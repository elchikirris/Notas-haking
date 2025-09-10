Can you crack the password to get the flag?Download the password checker [here](https://artifacts.picoctf.net/c/16/level3.py) and you'll need the encrypted [flag](https://artifacts.picoctf.net/c/16/level3.flag.txt.enc) and the [hash](https://artifacts.picoctf.net/c/16/level3.hash.bin) in the same directory too.There are 7 potential passwords with 1 being correct. You can find these by examining the password checker script.

------
#Solución 
```bash
elchikirris-picoctf@webshell:~$ wget https://artifacts.picoctf.net/c/16/level3.py
elchikirris-picoctf@webshell:~$ wget https://artifacts.picoctf.net/c/16/level3.flag.txt.enc
elchikirris-picoctf@webshell:~$ wget https://artifacts.picoctf.net/c/16/level3.hash.bin
elchikirris-picoctf@webshell:~$ nano level3.py
elchikirris-picoctf@webshell:~$ python3 level3.py 
~fo=M[J)c;9:Qi`c`h=<iP>0>8>37?q
{>52H&fcc5T1:le0g3d?;`d<2g+
.o7iR}32an`870aeh9Yfdn1fgg6)
|=g=OB)a`1:S2hcb35<k
                    60<c635dy
-<d=A)0a2:3kc326<:
50mb53dez
|:`<OE(ag6;S5obb42=k
                    11<d125c~
picoCTF{m45h_fl1ng1ng_2b072a90}

```


------
#Notas 
#referencias 