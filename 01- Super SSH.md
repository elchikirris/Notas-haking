Descripción
Using a Secure Shell (SSH) is going to be pretty important.Can you `ssh` as `ctf-player` to `titan.picoctf.net` at port `55155` to get the flag?

-----------
#Solución 
```
elchikirris-picoctf@webshell:~$ ssh  ctf-player@titan.picoctf.net -p 55155
The authenticity of host '[titan.picoctf.net]:55155 ([3.139.174.234]:55155)' can't be established.
ED25519 key fingerprint is SHA256:4S9EbTSSRZm32I+cdM5TyzthpQryv5kudRP9PIKT7XQ.
This key is not known by any other names
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '[titan.picoctf.net]:55155' (ED25519) to the list of known hosts.
ctf-player@titan.picoctf.net's password: 
Welcome ctf-player, here's your flag: picoCTF{s3cur3_c0nn3ct10n_65a7a106}
Connection to titan.picoctf.net closed.
```
picoCTF{s3cur3_c0nn3ct10n_65a7a106}

----------
#Notas 


#referencias 
