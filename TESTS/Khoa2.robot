*** Settings ***
Library           Libraries.web_client_library.WebClientLibrary
Library           SeleniumLibrary
Suite Teardown    Safe Quit Browser
Test Teardown     Run Keyword If Test Failed    Capture Page Screenshot

*** Variables ***
${BROWSER}            chrome
${iview_URL}          https://10.103.3.58/iview/views/index.jsf
${USERNAME}           admin
${PASSWORD}           AvayaMcspv_1234$
${Portal_URL}         https://aawgfed-kvm.hcm.com/portal/tenants/default/
${USERPORTAL}         khoa
${PASSWORDPORTAL}     Avaya_123$Avaya
${MEETINGID}          6001509

&{CLIENT}
...    host=10.128.224.115
...    screenshot_dir=${CURDIR}${/}..${/}Screenshots

&{IVIEW}
...    iview_address=${iview_URL}
...    iview_username=${USERNAME}
...    iview_password=${PASSWORD}

&{PORTAL}
...    portal_address=${Portal_URL}
...    portal_username=${USERPORTAL}
...    portal_password=${PASSWORDPORTAL}

*** Test Cases ***
IVIEW Web Client Smoke Test
    [Documentation]    Verify iView web client basic flow
    Create Web Client    ${BROWSER}    ${CLIENT}    ${IVIEW}    ${NONE}
    Call Web Client Method    sign_in
    Call Web Client Method    open_settings
    Call Web Client Method    open_user_portal
    Call Web Client Method    option_custom_branding
    Call Web Client Method    enable_advanced_branding
    Sleep    5s
    Call Web Client Method    sign_out

Portal Join Meeting Test
    [Documentation]    Sign in portal and join meeting successfully
    Create Web Client    ${BROWSER}    ${CLIENT}    ${NONE}    ${PORTAL}
    Call Web Client Method    sign_in_portal
    Call Web Client Method    verify_sign_in_portal        ${USERPORTAL}
    Call Web Client Method    start_my_meeting           
    Sleep    10s
    Call Web Client Method    verify_in_meeting            ${USERPORTAL}
    Call Web Client Method    terminate_meeting
    Call Web Client Method    sign_out