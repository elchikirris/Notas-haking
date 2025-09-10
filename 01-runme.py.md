Descripción 
Run the `runme.py` script to get the flag. Download the script with your browser or with `wget` in the webshell.[Download runme.py Python script](https://artifacts.picoctf.net/c/34/runme.py)

---------
#Solución 
```
elchikirris-picoctf@webshell:~$ wget https://artifacts.picoctf.net/c/34/runme.py
--2025-09-10 16:32:32--  https://artifacts.picoctf.net/c/34/runme.py
Resolving artifacts.picoctf.net (artifacts.picoctf.net)... 3.170.131.77, 3.170.131.72, 3.170.131.33, ...
Connecting to artifacts.picoctf.net (artifacts.picoctf.net)|3.170.131.77|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 270 [application/octet-stream]
Saving to: 'runme.py'

runme.py                                                  100%[==================================================================================================================================>]     270  --.-KB/s    in 0s      

2025-09-10 16:32:32 (18.7 MB/s) - 'runme.py' saved [270/270]
elchikirris-picoctf@webshell:~$ python3 runme.py 
picoCTF{run_s4n1ty_run}
```
picoCTF{run_s4n1ty_run}

----------
#Notas 
python3, sirve para poder correr archivos de python 

#referencias 
