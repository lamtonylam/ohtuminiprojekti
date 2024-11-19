*** Settings ***
Resource  resource.robot
Suite Setup      Open And Configure Browser
Suite Teardown   Close Browser
Test Setup       Reset Todos

*** Test Cases ***

Add a New Reference Successfully
    Go To Form Page
    Form Page Should Be Open
    Set Reference_id  TestId
    Set Author  TestAuthor
    Set Title  TestTitle
    Set Booktitle  TestBooktitle
    Set Year  2024
    Submit Form
    Starting Page Should Be Open
    Page Should Contain  Title: TestTitle, author: TestAuthor

*** Keywords ***

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
    Input Text  year    ${year}

Submit Form
    Click Button  create