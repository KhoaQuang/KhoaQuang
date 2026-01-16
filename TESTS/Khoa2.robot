*** Settings ***
Library    Libraries.web_client_library.WebClientLibrary
Suite Teardown    Safe Quit Browser

*** Variables ***
${BROWSER}    chrome
${iview_URL}        https://10.103.3.58/iview/views/index.jsf
${USERNAME}   admin
${PASSWORD}   AvayaMcspv_1234$

&{CLIENT}
...    host=10.128.224.115
...    screenshot_dir=${CURDIR}${/}..${/}Screenshots

&{IVIEW}
...    iview_address=${iview_URL}
...    iview_username=${USERNAME}
...    iview_password=${PASSWORD}

&{PORTAL}
...    portal_address=https://aawgmt-svc-kvm.hcm.com/portal/tenants/dc1/

*** Test Cases ***
Simple Web Client Test
    Create Web Client    ${BROWSER}    ${CLIENT}    ${IVIEW}
    Call Web Client Method    sign_in
    Call Web Client Method    open_settings
    Call Web Client Method    open_user_portal
    Call Web Client Method    pressing_option_custom_branding
    Call Web Client Method    sign_out