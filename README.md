# RebootPort 2i
A Reboot Script which uses Selenium written in Python to reboot your Telekom Speedport 2i Router
## Introduction
The [Speedport Entry 2](https://de.wikipedia.org/wiki/Speedport) is an entry level modem/router produced by "**Deutsche Telekom**".  
_This device is quite bad and its **performances tend to degrade over time**._  

The **most common solution** to this problem is made of several steps:
- Stand up
- Reach the **Speedport Entry 2**
- Pull the plug
- Wait few seconds
- Plug it back again
- Get back to what we were doing

Although this solution proved to be quite effective, it turned out to be also quite _**annoying**_.  
For this reason, the "**RebootPort**" project was born :)

## How to use
There are different ways to use the **RebootPort** tool.  
The next paragraphs describe the possible uses.

### Manual reboot
The simplest way to use the **RebootPort** tools is to manually run the [**reboot.py**](reboot.py) python script ( make sure to have python installed ) everytime we start noticing the first signs of slowness in the network.
It's important to specify the correct **device password** for our **Speedport** router in the script, so that it will be able to succesfully login and reboot our beloved router. 

Unfortunately, this solution can be used only before the network becomes so slow to be actually unusable.
In this case, only 2 possibilities are left:
- Stand up and follow the "**most common solution**" steps written above
- Ask someone to perform the "**most common solution**" steps above

The real (*dirty*) solution would be preventing the performance degradation by daily rebooting the router.

### Auto daily reboot
If in your network there's an always alive and connected linux device or windows computer, you could use it to periodically run the **reboot.py** python script and automatically reboot the router.
