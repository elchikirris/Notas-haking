Why search for the flag when I can make a bookmarklet to print it for me?Browse [here](http://titan.picoctf.net:51678/), and find the flag!


--------------------
```JAVA
        javascript:(function() {
            var encryptedFlag = "àÒÆÞ¦È¬ëÙ£ÖÓÚåÛÑ¢ÕÓË¨ËÓ§Èí";
            var key = "picoctf";
            var decryptedFlag = "";
            for (var i = 0; i < encryptedFlag.length; i++) {
                decryptedFlag += String.fromCharCode((encryptedFlag.charCodeAt(i) - key.charCodeAt(i % key.length) + 256) % 256);
            }
            alert(decryptedFlag);
        })();
```
Despues de poner eso en la consola me dio la bandera
picoCTF{p@g3_turn3r_e8b2d43b}