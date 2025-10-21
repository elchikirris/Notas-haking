Download this disk image and find the flag.Note: if you are using the webshell, download and extract the disk image into `/tmp` not your home directory.

- [Download compressed disk image](https://artifacts.picoctf.net/c/212/disk.flag.img.gz)

------------------
#Solución 
``` bash
┌──(edgar㉿vbox)-[/tmp/...theshyhat]
└─$ ls
dds1-alpine.flag.img  disk.flag.img  disk.img  flag.txt.enc   
┌──(edgar㉿vbox)-[/tmp/...theshyhat]
└─$ openssl aes256 -salt -in flag.txt -out flag.txt.enc -k unbreakablepassword1234567
Can't open "flag.txt" for reading, No such file or directory
405740A0687F0000:error:80000002:system library:BIO_new_file:No such file or directory:../crypto/bio/bss_file.c:67:calling fopen(flag.txt, rb)
405740A0687F0000:error:10000080:BIO routines:BIO_new_file:no such file:../crypto/bio/bss_file.c:75: 
┌──(edgar㉿vbox)-[/tmp/...theshyhat]
└─$ openssl aes256 -d -salt  -in flag.txt.enc -out flag.txt -k unbreakablepassword1234567 
*** WARNING : deprecated key derivation used.
Using -iter or -pbkdf2 would be better.
bad decrypt
40F7846E817F0000:error:1C800064:Provider routines:ossl_cipher_unpadblock:bad decrypt:../providers/implementations/ciphers/ciphercommon_block.c:107:  
┌──(edgar㉿vbox)-[/tmp/...theshyhat]
└─$ cat flag.txt
picoCTF{h4un71ng_p457_0a710765} 
```
picoCTF{h4un71ng_p457_5113beab}

-------
#Notas 
#referencias 