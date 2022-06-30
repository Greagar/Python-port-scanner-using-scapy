from scapy.all import *

startNumber = int(input("Enter start number :: "))
endNumber = int(input("Enter end number :: "))

targetIP = str(input("Enter target IP :: "))

ans, unans = sr(IP(dst=targetIP)/TCP(sport=666,dport=(startNumber,endNumber),flags="S"))

ans.summary(lfilter = lambda s,r: r.sprintf("%TCP.flags%") == "SA",prn=lambda s,r: r.sprintf("%TCP.sport% is open"))
