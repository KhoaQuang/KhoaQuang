*** Settings ***
Library    Libraries.web_client_library.WebClientLibrary
Suite Teardown    Safe Quit Browser

*** Variables ***
<<<<<<< Updated upstream:Practice ROBOT/TESTS/Khoa2.robot
${BROWSER}    edge
${URL}        https://10.103.3.173/iview/views/index.jsf
# ${web_title}        ${web_title}
${user_name}        Admin
${user_pass}        AvayaMcspv_1234$
=======
${BROWSER}    chrome
${URL}        https://10.103.3.58/iview/views/index.jsf
${USERNAME}   admin
${PASSWORD}   AvayaMcspv_1234$

&{CLIENT}
...    host=10.128.224.115
...    screenshot_dir=${CURDIR}${/}..${/}Screenshots

&{IVIEW}
...    iview_address=${URL}
...    iview_username=${USERNAME}
...    iview_password=${PASSWORD}
>>>>>>> Stashed changes:TESTS/Khoa2.robot

*** Test Cases ***
Simple Web Client Test
    Create Web Client    ${BROWSER}    ${CLIENT}    ${IVIEW}
    Call Web Client Method    sign_in
    Call Web Client Method    open_settings
    Call Web Client Method    open_user_portal
    Call Web Client Method    pressing_option_custom_branding
    Call Web Client Method    sign_out
    Call Web Client Method    quit