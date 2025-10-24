How about some hide and seek?Download this file [here](https://artifacts.picoctf.net/c_titan/5/unknown.zip).

------
#Solución 
picoCTF{ME74D47A_HIDD3N_4dabddcb}
```bash
hoomie_of_the_8th-picoctf@webshell:~$ ls
README.txt  _flag.png.extracted  challenge.zip  flag.png  home  pico.flag.png  unknown.zip
hoomie_of_the_8th-picoctf@webshell:~$ unzip unknown.zip 
Archive:  unknown.zip
  inflating: ukn_reality.jpg         
hoomie_of_the_8th-picoctf@webshell:~$ ls
README.txt  _flag.png.extracted  challenge.zip  flag.png  home  pico.flag.png  ukn_reality.jpg  unknown.zip
hoomie_of_the_8th-picoctf@webshell:~$ steghide extract -sf unknown.zip 
Enter passphrase: 
steghide: the file format of the file "unknown.zip" is not supported.
hoomie_of_the_8th-picoctf@webshell:~$ ls
README.txt  _flag.png.extracted  challenge.zip  flag.png  home  pico.flag.png  ukn_reality.jpg  unknown.zip
hoomie_of_the_8th-picoctf@webshell:~$ exiftool unknown.zip 
```




---------
#referencias 
https://gchq.github.io/CyberChef/#recipe=From_Base64('A-Za-z0-9%2B/%3D',true,false)&input=Y0dsamIwTlVSbnROUlRjMFJEUTNRVjlJU1VSRU0wNWZOR1JoWW1Sa1kySjlDZz09