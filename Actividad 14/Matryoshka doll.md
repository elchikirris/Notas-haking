Matryoshka dolls are a set of wooden dolls of decreasing size placed one inside another. What's the final one? Image: [this](https://mercury.picoctf.net/static/2978e1270538613cd8181c7b0dabe9bd/dolls.jpg)

--------------
```bash
┌──(edgar㉿vbox)-[~/…/_2_c.jpg.extracted/base_images/_3_c.jpg.extracted/base_images]
└─$ ls
4_c.jpg  _4_c.jpg.extracted                
┌──(edgar㉿vbox)-[~/…/_2_c.jpg.extracted/base_images/_3_c.jpg.extracted/base_images]
└─$ cd _4_c.jpg.extracted                 
┌──(edgar㉿vbox)-[~/…/base_images/_3_c.jpg.extracted/base_images/_4_c.jpg.extracted]
└─$ ls                   
136DA.zip  flag.txt    
┌──(edgar㉿vbox)-[~/…/base_images/_3_c.jpg.extracted/base_images/_4_c.jpg.extracted]
└─$ cat flag.txt 
picoCTF{4cf7ac000c3fb0fa96fb92722ffb2a32} 
```

Solo fue hacerle binwalk hasta que nos diera la bandera
