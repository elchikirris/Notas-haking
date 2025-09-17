My team has been working very hard on new features for our flag printing program! I wonder how they'll work together?

--------
#Solución 
```bash
elchikirris-picoctf@webshell:~$ cd drop-in/
elchikirris-picoctf@webshell:~/drop-in$ ls
flag.py  message.py  message.txt
elchikirris-picoctf@webshell:~/drop-in$ git branch -a

[1]+  Stopped                 git branch -a
elchikirris-picoctf@webshell:~/drop-in$ git checkout feature/part-1
Switched to branch 'feature/part-1'
elchikirris-picoctf@webshell:~/drop-in$ cat flag.py 
print("Printing the flag...")
print("picoCTF{t3@mw0rk_", end='')elchikirris-picoctf@webshell:~/drop-in$ git checkout feature/part-2
Switched to branch 'feature/part-2'
elchikirris-picoctf@webshell:~/drop-in$ cat flag.py 
print("Printing the flag...")

print("m@k3s_th3_dr3@m_", end='')elchikirris-picoctf@webshell:~/drop-in$ git checkout feature/part-3
Switched to branch 'feature/part-3'
elchikirris-picoctf@webshell:~/drop-in$ cat flag.py 
print("Printing the flag...")

print("w0rk_7ae8dd33}")
elchikirris-picoctf@webshell:~/drop-in$ 

```


picoCTF{t3@mw0rk_m@k3s_th3_dr3@m_w0rk_7ae8dd33}

-----------
#Notas 
Me hace recordar varias cosas de git, por ejemplo lo de las ramas, eso no me acordaba en lo mas mínimo 
#referencias 