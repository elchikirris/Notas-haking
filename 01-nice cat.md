There is a nice program that you can talk to by using this command in a shell: `$ nc mercury.picoctf.net 49039`, but it doesn't speak English...

----
#Solución 
La salida de la terminal y luego la hacemos en ascii
elchikirris-picoctf@webshell:~$ nc mercury.picoctf.net 49039
112 
105 
99 
111 
67 
84 
70 
123 
103 
48 
48 
100 
95 
107 
49 
116 
116 
121 
33 
95 
110 
49 
99 
51 
95 
107 
49 
116 
116 
121 
33 
95 
51 
100 
56 
52 
101 
100 
99 
56 
125 
10 
Usamos lo de arriba como entrada 

Y esto da de salida
picoCTF{g00d_k1tty!_n1c3_k1tty!_3d84edc8}

-------
#Notas 

#referencias 
https://gchq.github.io/CyberChef/#recipe=From_Decimal('Space',false)&input=MTEyIAoxMDUgCjk5IAoxMTEgCjY3IAo4NCAKNzAgCjEyMyAKMTAzIAo0OCAKNDggCjEwMCAKOTUgCjEwNyAKNDkgCjExNiAKMTE2IAoxMjEgCjMzIAo5NSAKMTEwIAo0OSAKOTkgCjUxIAo5NSAKMTA3IAo0OSAKMTE2IAoxMTYgCjEyMSAKMzMgCjk1IAo1MSAKMTAwIAo1NiAKNTIgCjEwMSAKMTAwIAo5OSAKNTYgCjEyNSAKMTAg