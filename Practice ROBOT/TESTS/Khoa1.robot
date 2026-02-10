*** Settings ***
Library         SeleniumLibrary
Library         Collections
Library         OperatingSystem        
Library         ../GUI/Khoa.py   

# Resource        ../CONFIG/UserKeyWords.robot

Test Teardown   Run Keyword If Test Failed    Close Browser

*** Variables ***
${url}              https://10.103.3.173/iview/views/index.jsf
${username}         admin
${password}         AvayaMcspv_1234$
${BROWSER}          None

*** Test Cases ***
Test Browser Automation
    [Setup]    Open Browser And Navigate To URL    ${url}
    Sign In    ${username}    ${password}
    Sign Out
    Close Browser

*** Keywords ***
Open Browser And Navigate To URL
    [Arguments]    ${url}
    Initialize Browser Automation
    Call Method    ${BROWSER}    launch_browser    ${url}

Sign In
    [Arguments]    ${username}    ${password}
    Call Method    ${BROWSER}    signin       ${username}    ${password}

Sign Out
    Call Method    ${BROWSER}    signout

Close Browser
    Run Keyword If    '${BROWSER}' != 'None'    Call Method    ${BROWSER}    close_browser

Initialize Browser Automation
    ${BROWSER} =    Evaluate    Khoa.Web()    modules=Khoa
    Set Global Variable    ${BROWSER}
    

