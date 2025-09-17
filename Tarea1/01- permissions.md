Can you read files in the root file?

Additional details will be available after launching your challenge instance.

--------------
#Solución 
``` Bash
ls
bin  boot  challenge  dev  etc  home  lib  lib32  lib64  libx32  media  mnt  opt  proc  root  run  sbin  srv  sys  tmp  usr  var
# cd root
# ls
# ls -la
total 12
drwx------ 1 root root   23 Aug  4  2023 .
drwxr-xr-x 1 root root   51 Sep 17 18:50 ..
-rw-r--r-- 1 root root 3106 Dec  5  2019 .bashrc
-rw-r--r-- 1 root root   35 Aug  4  2023 .flag.txt
-rw-r--r-- 1 root root  161 Dec  5  2019 .profile
# cat .flag.txt
picoCTF{uS1ng_v1m_3dit0r_1cee9dcb}
# Connection to saturn.picoctf.net closed by remote host.
Connection to saturn.picoctf.net closed.
elchikirris-picoctf@webshell:~$ 
```
Para llegar ahi tuve que buscar los permisos de root desde el super usuario

------------
#referencias 
https://gtfobins.github.io/gtfobins/vi

#Notas 
Este reto si me saco de mis casillas
