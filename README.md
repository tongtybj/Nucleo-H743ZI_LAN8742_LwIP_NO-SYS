# TCP, UDP with nucleo

## requirement:

1. [STM32CubeMX](https://www.st.com/ja/development-tools/stm32cubemx.html), please use the version of **v5.0.1**, and the version of `STM32H7` is **v1.3.0**.
2. [Truestudio](https://www.st.com/ja/development-tools/truestudio.html), please use version of **9.3.0**, otherwise, the flash would fail.
3. [Nucleo-H743ZI](https://www.st.com/ja/evaluation-tools/nucleo-h743zi.html)

## compile:

1. build in Truestudio
2. flash to the Nucleo-H743ZI

### Generate from STM32CubeMX:
please check the MPU settings for ethernet DMA, based on following website:
- https://community.st.com/s/article/FAQ-Ethernet-not-working-on-STM32H7x3
- https://www.keshikan.net/gohantabeyo/?p=563
- http://nemuisan.blog.bai.ne.jp/?eid=215813
- https://www.st.com/content/ccc/resource/technical/document/application_note/group0/bc/2d/f7/bd/fb/3f/48/47/DM00272912/files/DM00272912.pdf/jcr:content/translations/en.DM00272912.pdf



## usage:

1. create a new Ethernet connection with static IP (192.168.25.xxx, xxx: except 238) in host PC.

2(a) [tag. tcp_ip](https://github.com/tongtybj/Nucleo-H743ZI_LAN8742_LwIP_NO-SYS/tree/tcp_ip): 

- perform UDP receive test:

```
$ python3 Scripts/socket_udp_receive.py
```

- perform TCP echo test:

```
$ python3 Scripts/socket_tcp_send.py
```

2(b) [tag. udp_polling](https://github.com/tongtybj/Nucleo-H743ZI_LAN8742_LwIP_NO-SYS/tree/udp_polling): 

- perform UDP echo test at 100Hz:
```
$ python3 Scripts/socket_udp_send.py
```
- calculate UDP echo speed at 1000Hz:
```
$ python3 Scripts/socket_udp_send2.py
```

2(c) [tag. udp_interrupt](https://github.com/tongtybj/Nucleo-H743ZI_LAN8742_LwIP_NO-SYS/tree/udp_interrupt): 

- perform UDP echo test at 100Hz:
```
$ python3 Scripts/socket_udp_send.py
```
- calculate UDP echo speed at 1000Hz:
```
$ python3 Scripts/socket_udp_send2.py
```
**note**: problem the interrupt may corrupt while simultaneously performing `ping` and these scripts. Can not figure out the reason. But at least, solely perform either `ping` or these scripts is OK. 