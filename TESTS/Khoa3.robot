*** Settings ***
Library           SeleniumLibrary
Library           Collections
Library           String
Library           BuiltIn

*** Variables ***
${BROWSER}        chrome
${iview_URL}      https://10.103.3.173/iview/views/index.jsf
${USERNAME}       admin
${PASSWORD}       AvayaMcspv_1234$
${Portal_URL}     https://aawgott-svc-kvm.hcm.com:443/portal
${USERPORTAL}     khoa
${MEETINGID}      5602112

*** Test Cases ***
Test IVIEW Variables Configuration
    [Documentation]    Verify iView configuration variables are set correctly
    Should Not Be Empty        ${iview_URL}
    Should Contain             ${iview_URL}    iview
    Should Not Be Empty        ${USERNAME}
    Should Not Be Empty        ${PASSWORD}

Test Portal Variables Configuration
    [Documentation]    Verify Portal configuration variables are set correctly
    Should Not Be Empty        ${Portal_URL}
    Should Contain             ${Portal_URL}    portal
    Should Not Be Empty        ${USERPORTAL}
    Should Not Be Empty        ${MEETINGID}

Test Browser Configuration
    [Documentation]    Verify browser type is set
    Should Not Be Empty    ${BROWSER}
    Should Be Equal    ${BROWSER}    chrome

Test Client Dictionary Structure
    [Documentation]    Verify client configuration has required keys
    ${client_dict}=    Create Dictionary    host=10.128.224.115    screenshot_dir=/Screenshots
    Dictionary Should Contain Key    ${client_dict}    host
    Dictionary Should Contain Key    ${client_dict}    screenshot_dir

Test IVIEW Dictionary Structure
    [Documentation]    Verify iView configuration has required keys
    ${iview_dict}=    Create Dictionary    iview_address=${iview_URL}    iview_username=${USERNAME}    iview_password=${PASSWORD}
    Dictionary Should Contain Key    ${iview_dict}    iview_address
    Dictionary Should Contain Key    ${iview_dict}    iview_username
    Dictionary Should Contain Key    ${iview_dict}    iview_password

Test Portal Dictionary Structure
    [Documentation]    Verify Portal configuration has required keys
    ${portal_dict}=    Create Dictionary    portal_address=${Portal_URL}    portal_username=${USERPORTAL}    portal_password=${PASSWORD}
    Dictionary Should Contain Key    ${portal_dict}    portal_address
    Dictionary Should Contain Key    ${portal_dict}    portal_username
    Dictionary Should Contain Key    ${portal_dict}    portal_password

Test Meeting ID Format
    [Documentation]    Verify meeting ID is numeric
    Should Match Regexp    ${MEETINGID}    ^[0-9]+$

Test URL Format Validation
    [Documentation]    Verify URLs are valid format
    Should Match Regexp    ${iview_URL}    ^https://
    Should Match Regexp    ${Portal_URL}    ^https://