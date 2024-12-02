*** Settings ***
Resource  resource.robot
Suite Setup      Open And Configure Browser
Suite Teardown   Close Browser
Test Setup       Reset References

*** Test Cases ***
Reference Table Is Visible To User
    Go To Starting Page
    Starting Page Should Be Open
    Table Should Be Visible

Reference Is Added To The Table After It Is Created
    Go To Form Page
    Form Page Should Be Open
    Set Reference_id  TestId
    Set Author  TestAuthor
    Set Title  TestTitle
    Set Booktitle  TestBooktitle
    Set Year  2024
    Click Button  create
    Starting Page Should Be Open
    Table Should Be Visible
    Table Should Contain Reference  TestId
    Table Should Contain Author  TestAuthor
    Table Should Contain Title  TestTitle
    Press Show More
    Table Should Contain Year  Year: 2024

*** Keywords *** 
Table Should Be Visible
    Element Should Be Visible  //Table

Table Should Contain Reference
    [Arguments]    ${reference_id}
    ${table_text}=    Get Text    //table
    Should Contain    ${table_text}    ${reference_id}

Table Should Contain Author
    [Arguments]    ${author}
    ${table_text}=    Get Text    //table
    Should Contain    ${table_text}    ${author}

Table Should Contain Title
    [Arguments]    ${title}
    ${table_text}=    Get Text    //table
    Should Contain    ${table_text}    ${title}

Table Should Contain Year
    [Arguments]    ${year}
    ${table_text}=    Get Text    //table
    Should Contain    ${table_text}    ${year}

Set Reference_id
    [Arguments]  ${reference_id}
    Input Text  reference_id  ${reference_id}

Set Author
    [Arguments]  ${author}
    Input Text  author  ${author}

Set Title
    [Arguments]  ${title}
    Input Text  title  ${title}

Set Booktitle
    [Arguments]  ${booktitle}
    Input Text  booktitle  ${booktitle}

Set Year
    [Arguments]  ${year}
    Input Text  year  ${year}

Press Show More
    Click Button    name=show_more_button

