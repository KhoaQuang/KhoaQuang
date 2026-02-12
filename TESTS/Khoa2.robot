*** Settings ***
Library           Libraries.web_client_library.WebClientLibrary
Library           SeleniumLibrary
Variables         Recources/Variables.robot
Test Teardown     Run Keyword If Test Failed    Capture Page Screenshot

*** Variables ***
###############################################################################
${ADMIN}                Admin

###############################################################################
${BROWSER_CHROME}      chrome
${BROWSER_EDGE}        edge
${BROWSER_FIREFOX}     firefox

###############################################################################
&{CLIENT}
...    host=10.128.224.115
...    screenshot_dir=${CURDIR}${/}..${/}Screenshots

###############################################################################
${IVIEW_URL}           https://10.103.3.173/iview/views/index.jsf
${USERNAME}            admin
${PASSWORD}            AvayaMcspv_1234$
&{IVIEW}
...    iview_address=${iview_URL}
...    iview_username=${USERNAME}
...    iview_password=${PASSWORD}

*** Test Cases ***
IVIEW Web Client Smoke Test
    [Documentation]    Verify iView web client basic flow
    Create Web Client
    ...    user_key=${ADMIN} 
    ...    browser=${BROWSER_CHROME}
    ...    client=${CLIENT}
    ...    iview=&{IVIEW}
   
    Call Web Client Method    ${ADMIN}                 sign_in
    Call Web Client Method    ${ADMIN}                 open_settings
    Call Web Client Method    ${ADMIN}                 open_user_portal
    Call Web Client Method    ${ADMIN}                 option_custom_branding
    Call Web Client Method    ${ADMIN}                 enable_advanced_branding
    Sleep    5s
    Call Web Client Method    ${ADMIN}                 sign_out