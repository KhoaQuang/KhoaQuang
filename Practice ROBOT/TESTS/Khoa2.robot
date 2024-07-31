*** Settings ***
Library         SeleniumLibrary

*** Variables ***
${BROWSER}    edge
${URL}        https://10.103.3.173/iview/views/index.jsf
# ${web_title}        ${web_title}
${user_name}        Admin
${user_pass}        AvayaMcspv_1234$

*** Test Cases ***
Khoa2
    Open Browser  ${URL}    ${BROWSER}
    Maximize Browser Window 
    Sleep    5
    Input Text    //*[@id="loginForm:username"]    ${user_name}
    Input Password    //*[@id="loginForm:password"]    ${user_pass}
    Click Element    //*[@id="loginForm:submitText"]
    Sleep    5
    Click Element    //*[@id="topForm:topRepeat:7:topLink"]
    Close Browser
    