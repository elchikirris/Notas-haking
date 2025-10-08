Connect to this PostgreSQL server and find the flag!`psql -h saturn.picoctf.net -p 59355 -U postgres pico`Password is `postgres`

---------------
#Solución 
Despues de poner los comandos que nos da al poner la instancia, nos damos cuenta que podemos correr sentencias sql 
Solo puse 
```
select * from flags;
```
y me dio la bandera en una de las columnas.


picoCTF{L3arN_S0m3_5qL_t0d4Y_21c94904}



------------
#Notas 
#referencias 