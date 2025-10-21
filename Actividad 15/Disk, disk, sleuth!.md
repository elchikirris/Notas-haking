Use `srch_strings` from the sleuthkit and some terminal-fu to find a flag in this disk image: [dds1-alpine.flag.img.gz](https://mercury.picoctf.net/static/4f3df7052b4121aff89af1a3f517afb1/dds1-alpine.flag.img.gz)

----------------------
#Solución 
``` bash
┌──(edgar㉿vbox)-[~/pico/forensic/Disk]
└─$ ls
dds1-alpine.flag.img.gz
┌──(edgar㉿vbox)-[~/pico/forensic/Disk]
└─$ gzip -d dds1-alpine.flag.img.gz                 
┌──(edgar㉿vbox)-[~/pico/forensic/Disk]
└─$ ls
dds1-alpine.flag.img   
┌──(edgar㉿vbox)-[~/pico/forensic/Disk]
└─$ srch_strings dds1-alpine.flag.img | grep "pico"
ffffffff81399ccf t pirq_pico_get
ffffffff81399cee t pirq_pico_set
ffffffff820adb46 t pico_router_probe
  SAY picoCTF{f0r3ns1c4t0r_n30phyt3_a011c142}
┌──(edgar㉿vbox)-[~/pico/forensic/Disk]
└─$ 
```
picoCTF{f0r3ns1c4t0r_n30phyt3_a011c142}

----------
#referencias 
#Notas 
