# Python-port-scanner-using-scapy

### What the script is for?
You can use the script to scan devices on a network to see **open ports**. 
This can be used to gain crucial information of a network. 

**DISCLAIMER ONLY USE THIS SCRIPT ON DEVICES YOU OWN OR HAVE PERMISSION TO SCAN**

### What you need to run the script

To run the code you will need **python** and **scapy** installed. 

### How it works
How the script works in more depth

```python
# First we import scapy
from scapy.all import *
```

```python
# Here we have an input to get the start port number
startNumber = int(input("Enter start number :: "))
# On this line we are geting the end port number
endNumber = int(input("Enter end number :: "))

# targetIP is the ip address of the machine we whant to scan
targetIP = str(input("Enter target IP :: "))
```

```python
# This is the code that sends all the SYN packets 
# We start by giving the destination IP (dst=targetIP) next we specify the protocol TCP and source port.
# In the end we specify the destination port dport=(startNumber,endNumber) and flags="S"
ans, unans = sr(IP(dst=targetIP)/TCP(sport=666,dport=(startNumber,endNumber),flags="S"))
```

```python
# This code line will filter out and display the ports that were open
ans.summary(lfilter = lambda s,r: r.sprintf("%TCP.flags%") == "SA",prn=lambda s,r: r.sprintf("%TCP.sport% is open"))
```

