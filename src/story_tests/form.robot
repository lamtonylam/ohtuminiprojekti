*** Settings ***
Resource  resource.robot
Suite Setup      Open And Configure Browser
Suite Teardown   Close Browser
Test Setup       Reset References

*** Test Cases ***

Add a New Reference Successfully
    Go To Form Page
    Form Page Should Be Open
    Set Reference_id  TestId
    Set Author  TestAuthor
    Set Title  TestTitle
    Set Booktitle  TestBooktitle
    Set Year  2024
    Scroll Down  1000
    Submit Form
    Starting Page Should Be Open
    Page Should Contain    TestId
    Page Should Contain    TestAuthor

Adding a new reference without required fields fails
    Go To Form Page
    Form Page Should Be Open
    Set Reference_id  TestId
    Set Author  TestAuthor
    Set Title  TestTitle
    Set Booktitle  TestBooktitle
    Set Editor  TestEditor
    Scroll Down  1000
    Submit Form
    Go To Starting Page

*** Keywords ***

Submit Form
    Click Button  Create
