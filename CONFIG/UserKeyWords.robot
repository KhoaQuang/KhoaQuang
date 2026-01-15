*** Settings ***
Library     Collections
Library     OperatingSystem
Library     DataDriver    ${TRUE}    WITH NAME       user_profile

*** Keywords ***
GET
    [Arguments]  ${info}
    ${data}      ${info}
    [Return]  ${data}

SET PREFIX
    [Arguments]  ${prefix_number}
    ${data}      ${info}
    [Return]  ${data}
    # user_profile     ${prefix_number}

SET USER PROFILE
    [Arguments]  ${user_name}
    ${user_data}      ${user_name}
    [Return]  ${user_data}

