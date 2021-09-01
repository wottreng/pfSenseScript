#!/usr/bin/python3
import os
import requests
import urllib3
urllib3.disable_warnings() #due to https session on lan having local token
# -----------------
staticIPofDevice = "1.2.3.4"
pfsenseRouterIP = "1.2.3.1"
userName = ""
passWord = ""
# ------------------

session = requests.session()
a = session.get(f'https://{pfsenseRouterIP}/', verify=False)
csrfToken = a.text.split("name='__csrf_magic' value=\"")[1].split('\" />')[0]
data = {'__csrf_magic': csrfToken,
        'usernamefld': userName,
        'passwordfld': passWord,
        'login': 'Sign In'}
# main page
b = session.post(f'https://{pfsenseRouterIP}/index.php', data=data, allow_redirects=True)
c = session.get(f'https://{pfsenseRouterIP}/status_dhcp_leases.php')
deviceStatus = c.text.split(f'<td>{staticIPofDevice}</td>')[1].split("<td>static</td>")[0]
if "online" in deviceStatus:
    print("[*] device on LAN [*]")
else: print("[*] device NOT on LAN [*]")
del session
