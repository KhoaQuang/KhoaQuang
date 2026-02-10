*** Settings ***
Library    Libraries.web_client_library.WebClientLibrary

*** Variables ***
${BROWSER} 
&{CLIENT}
&{IVIEW}

*** Keywords ***
Open User Portal
    Create Web Client    ${BROWSER}    ${CLIENT}    ${IVIEW}    ${NONE}
    Call Web Client Method                   Tab Settings
    Call Web Client Method                  Open User Portal

Open Custom Branding Page
    Call Web Client Method                 Open User Portal    
    Call Web Client Method                 Option Custom Branding           