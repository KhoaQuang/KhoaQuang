*** Settings ***
Library           Libraries.web_client_library.WebClientLibrary
Library           SeleniumLibrary
Suite Teardown    Safe Quit Browser
Test Teardown     Run Keyword If Test Failed    Capture Page Screenshot
Test Template     Portal Join Meeting Test

*** Variables ***
${BROWSER}            chrome
${iview_URL}          https://10.103.3.58/iview/views/index.jsf
${USERNAME}           admin
${PASSWORD}           AvayaMcspv_1234$
${Portal_URL}         https://aawgte-svc-kvm.hcm.com/portal/tenants/default/
${USERPORTAL}         khoa
${PASSWORDPORTAL}     AvayaMcspv_1234$
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

*** Keywords ***

Portal Join Meeting Test
    [Arguments]    ${MEETINGID}
    [Documentation]    Sign in portal and join meeting successfully
    Create Web Client    ${BROWSER}    ${CLIENT}    ${NONE}    ${PORTAL}
    Call Web Client Method    sign_in_portal
    Call Web Client Method    verify_sign_in_portal        ${USERPORTAL}
    Call Web Client Method    join_meeting                 ${MEETINGID}
    Sleep    10s
    Call Web Client Method    verify_in_meeting            ${USERPORTAL}
    Call Web Client Method    terminate_meeting
    Call Web Client Method    sign_out

*** Test Cases ***
Portal Join Meeting Test Run 1     ${MEETINGID}
Portal Join Meeting Test Run 2     ${MEETINGID}  
Portal Join Meeting Test Run 3     6032145
Portal Join Meeting Test Run 4     ${MEETINGID}
Portal Join Meeting Test Run 5     ${MEETINGID}
Portal Join Meeting Test Run 6     ${MEETINGID}
Portal Join Meeting Test Run 7     ${MEETINGID}
Portal Join Meeting Test Run 8     ${MEETINGID}
Portal Join Meeting Test Run 9     ${MEETINGID}
Portal Join Meeting Test Run 10    ${MEETINGID}
Portal Join Meeting Test Run 11    ${MEETINGID}
Portal Join Meeting Test Run 12     ${MEETINGID}
Portal Join Meeting Test Run 13     ${MEETINGID}
Portal Join Meeting Test Run 14     ${MEETINGID}
Portal Join Meeting Test Run 15     ${MEETINGID}    
Portal Join Meeting Test Run 16     ${MEETINGID}
Portal Join Meeting Test Run 17     ${MEETINGID}
Portal Join Meeting Test Run 18     ${MEETINGID}
Portal Join Meeting Test Run 19     ${MEETINGID}
Portal Join Meeting Test Run 20     ${MEETINGID}


