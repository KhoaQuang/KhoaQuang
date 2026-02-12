*** Variables ***
${BROWSER}        chrome

&{CLIENT}
...    name=Khoa Test
...    env=staging

&{PORTAL_A}
...    address=https://portal.example.com
...    username=userA
...    password=passA

&{PORTAL_B}
...    address=https://portal.example.com
...    username=userB
...    password=passB
