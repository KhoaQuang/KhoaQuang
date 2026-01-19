*** Settings ***
Library    Libraries.web_client_library.WebClientLibrary
Suite Teardown    Safe Quit Browser

*** Variables ***
${BROWSER}        chrome
${iview_URL}      https://10.103.3.58/iview/views/index.jsf
${USERNAME}       admin
${PASSWORD}       AvayaMcspv_1234$
${Portal_URL}     https://aawgte-svc-kvm.hcm.com/portal/tenants/default/
${USERPORTAL}     khoa

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
...    portal_password=${PASSWORD}

*** Test Cases ***
Simple Web Client Test
    Create Web Client    ${BROWSER}    ${CLIENT}    ${IVIEW}    ${NONE}
    Call Web Client Method    sign_in
    Call Web Client Method    open_settings
    Call Web Client Method    open_user_portal
    Call Web Client Method    pressing_option_custom_branding
    Call Web Client Method    sign_out

Simple SWC Client Test
    Create Web Client    ${BROWSER}    ${CLIENT}    ${NONE}    ${PORTAL}
    Call Web Client Method    sign_in_portal
    Call Web Client Method    verify_sign_in_portal
    Call Web Client Method    verify_in_meeting
    Call Web Client Method    sign_out