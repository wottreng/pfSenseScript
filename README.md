# pfSense Script To Check if Device is on LAN
how it works:
* it creates a new session to log into your pfsense server
* opens DHCP page and finds device IP address
* checks if device is active 
* deletes session

How to use:
* fill in blocks:
```
staticIPofDevice = "1.2.3.4" // static ip of device you want to check
pfsenseRouterIP = "1.2.3.1" // static ip of pfsense server
userName = "" // pfsense login username
passWord = "" // pfsense login password
```
* run script

 ### Cheers  🍺 
