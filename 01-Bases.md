What does this `bDNhcm5fdGgzX3IwcDM1` mean? I think it has something to do with bases.
-----------------------------------------------------------------------------------------------------------------------------------------------------------------
#Solución 
Usando cyberchef

Entrada= bDNhcm5fdGgzX3IwcDM1
Recipe= Base64

Salida= l3arn_th3_r0p35
PicoCTF{l3arn_th3_r0p35}

Python 
```
Import base64
base64.b64decode('bDNhcm5fdGgzX3IwcDM1').decode()
```

-----------------------------------------------------------------------------------------------------------------
#referencias 
 https://gchq.github.io/CyberChef/
#Notas 
Aprendí como decodificar un texto de base64

