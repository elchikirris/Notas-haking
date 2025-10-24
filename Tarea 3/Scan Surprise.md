I've gotten bored of handing out flags as text. Wouldn't it be cool if they were an image instead?You can download the challenge files here:

- [challenge.zip](https://artifacts.picoctf.net/c_atlas/16/challenge.zip)

Additional details will be available after launching your challenge instance

------------
#Solución 
picoCTF{p33k_@_b00_7843f77c}

``` bash
hoomie_of_the_8th-picoctf@webshell:~$ ls
README.txt  _flag.png.extracted  challenge.zip  flag.png  home  pico.flag.png
hoomie_of_the_8th-picoctf@webshell:~$ cd home/
hoomie_of_the_8th-picoctf@webshell:~/home$ ls
ctf-player
hoomie_of_the_8th-picoctf@webshell:~/home$ cd ctf-player/
hoomie_of_the_8th-picoctf@webshell:~/home/ctf-player$ ls
drop-in
hoomie_of_the_8th-picoctf@webshell:~/home/ctf-player$ cd drop-in/
hoomie_of_the_8th-picoctf@webshell:~/home/ctf-player/drop-in$ ls
flag.png
hoomie_of_the_8th-picoctf@webshell:~/home/ctf-player/drop-in$ zs flag.png 
-bash: zs: command not found
hoomie_of_the_8th-picoctf@webshell:~/home/ctf-player/drop-in$ sz flag.png 
```