*** Settings ***
Library         Collections
Library         OperatingSystem
Test Teardown   Quit Browser

*** Variables ***
${URL}              https://10.103.3.58/iview/views/index.jsf
${USERNAME}         admin
${PASSWORD}         AvayaMcspv_1234$
${BROWSER}          chrome
&{CLIENT}           host=10.128.224.115    screenshot_dir=${CURDIR}${/}..${/}Screenshots
&{IVIEW}            iview_address=${URL}    iview_username=${USERNAME}    iview_password=${PASSWORD}

*** Test Cases ***
Simple Web Client Test
    [Setup]    Create Web Client
    Sign In
    Tab Settings
    Tab User Portal
    Tab Custom Branding
    Sign Out
    [Teardown]    Quit Browser

*** Keywords ***
Create Web Client
    Create Directory    ${CURDIR}${/}..${/}LOGS
    Evaluate    __import__('sys').path.append(r'E:\\Backupwin11\\Launch-auto')    sys
    ${wc}=    Evaluate    __import__('importlib').import_module('GUI.Web_function.Web_clients').Web_Clients('${BROWSER}', ${CLIENT}, ${IVIEW}, use_local_driver=True)    importlib
    Set Suite Variable    ${WEB_CLIENT}    ${wc}

Sign In
    ${wc}=    Get Variable Value    ${WEB_CLIENT}
    Run Keyword If    '${wc}' == 'None'    Fail    Browser instance not initialized
    Sleep    5
    Call Method    ${wc}    sign_in

Tab Settings
    ${wc}=    Get Variable Value    ${WEB_CLIENT}
    Run Keyword If    '${wc}' == 'None'    Fail    Browser instance not initialized
    Sleep    5
    Call Method    ${wc}    open_settings

Tab User Portal
    ${wc}=    Get Variable Value    ${WEB_CLIENT}
    Run Keyword If    '${wc}' == 'None'    Fail    Browser instance not initialized
    Sleep    5
    Call Method    ${wc}    open_user_portal

Tab Custom Branding
    ${wc}=    Get Variable Value    ${WEB_CLIENT}
    Run Keyword If    '${wc}' == 'None'    Fail    Browser instance not initialized
    Sleep    5
    Call Method    ${wc}    pressing_option_custom_branding
Sign Out
    ${wc}=    Get Variable Value    ${WEB_CLIENT}
    Run Keyword If    '${wc}' == 'None'    Fail    Browser instance not initialized
    Sleep    5
    Call Method    ${wc}    sign_out


Quit Browser
    ${wc}=    Get Variable Value    ${WEB_CLIENT}    None
    Run Keyword If    '${wc}' != 'None'    Call Method    ${wc}    quit