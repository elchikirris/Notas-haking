A digital ghost has breached my defenses, and my sensitive data has been stolen! 😱💻 Your mission is to uncover how this phantom intruder infiltrated my system and retrieve the hidden flag.To solve this challenge, you'll need to analyze the provided PCAP file and track down the attack method. The attacker has cleverly concealed his moves in well timely manner. Dive into the network traffic, apply the right filters and show off your forensic prowess and unmask the digital intruder!Find the PCAP file here [Network Traffic PCAP file](https://challenge-files.picoctf.net/c_verbal_sleep/b6fbb3a5560749f838cdc6db4950985767c4691db3a7b34a220e5654ee39e700/myNetworkTraffic.pcap) and try to get the flag.

----

```bash
hoomie_of_the_8th-picoctf@webshell:~$ ls     
README.txt  _flag.png.extracted  challenge.zip  flag.png  home  myNetworkTraffic.pcap  pico.flag.png  ukn_reality.jpg  unknown.zip
hoomie_of_the_8th-picoctf@webshell:~$ tshark -r myNetworkTraffic.pcap -Y "tcp.len==12 || tcp.len==4" -T fields -e frame.time -e tcp.segment_data | sort -k4 | awk '{print $6}'
63476c6a62304e5552673d3d
657a46305833633063773d3d
626e52666447673064413d3d
587a4d3063336c6664413d3d
596d68664e484a664d773d3d
4e6d5930595459324e673d3d
66513d3d
hoomie_of_the_8th-picoctf@webshell:~$ tshark -r myNetworkTraffic.pcap -Y "tcp.len==12 || tcp.len==4" -T fields -e frame.time -e tcp.segment_data | sort -k4 | awk '{print $6}' | xxd -p -r | base64 -d
picoCTF{1t_w4snt_th4t_34sy_tbh_4r_36f4a666}
```