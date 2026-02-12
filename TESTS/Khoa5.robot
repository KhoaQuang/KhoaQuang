*** Settings ***
Library           Libraries.web_client_library.WebClientLibrary
Library           SeleniumLibrary
# Variables         Recources/Variables.robot
# Suite Teardown    Quit All Browsers
Test Teardown     Run Keyword If Test Failed    Quit All Browsers

*** Variables ***
###############################################################################
${OWNER}                A
${USER}                 B

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

###############################################################################
&{PORTAL_USER_A}
...    portal_address=https://aawgott-svc-kvm.hcm.com/portal/tenants/default/
...    portal_username=khoa
...    portal_password=AvayaMcspv_1234$

&{PORTAL_USER_B}
...    portal_address=https://aawgott-svc-kvm.hcm.com/portal/tenants/default/
...    portal_username=khoa2
...    portal_password=RAPtor1234

###############################################################################
${MEETING_ID}          4602112
${MEETING_TOPIC}       Automation Test Meeting


*** Test Cases ***
User A starts meeting, User B joins
    [Documentation]    Verify test case: All user join meeting then Owner terminate meeting
    Create Web Client
    ...    user_key=${OWNER}
    ...    browser=${BROWSER_FIREFOX}
    ...    client=${CLIENT}
    ...    portal=&{PORTAL_USER_A}

    Call Web Client Method    ${OWNER}    sign_in_portal
    Call Web Client Method    ${OWNER}    verify_sign_in_portal        ${PORTAL_USER_A['portal_username']}
    Call Web Client Method    ${OWNER}    start_my_meeting
    Sleep    10s
    Call Web Client Method    ${OWNER}    verify_in_meeting            ${PORTAL_USER_A['portal_username']}

    Create Web Client
    ...    user_key=${USER}
    ...    browser=${BROWSER_CHROME}
    ...    client=${CLIENT}
    ...    portal=&{PORTAL_USER_B}

    Call Web Client Method    ${USER}     sign_in_portal
    Call Web Client Method    ${USER}     verify_sign_in_portal        ${PORTAL_USER_B['portal_username']}
    Call Web Client Method    ${USER}     join_meeting                 ${MEETING_ID}
    Sleep    10s
    Call Web Client Method    ${USER}     verify_in_meeting            ${PORTAL_USER_B['portal_username']}
    Sleep    10s
    Call Web Client Method    ${OWNER}    mute_all_participants
    Call Web Client Method    ${OWNER}    terminate_meeting
    Call Web Client Method    ${OWNER}    sign_out
    Call Web Client Method    ${USER}     sign_out

    Call Web Client Method    ${OWNER}    quit_browser
    Call Web Client Method    ${USER}     quit_browser
