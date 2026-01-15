*** Settings ***
Library    Libraries.web_client_library

*** Keywords ***
Open User Portal
    Tab Settings
    Tab User Portal

Open Custom Branding Page
    Open User Portal
    Tab Custom Branding