*** Settings ***
Resource  resource.robot
Suite Setup      Open And Configure Browser
Suite Teardown   Close Browser
Test Setup       Reset References

*** Test Cases ***

Delete a Reference
    Go To References Page
    Select Reference Type    inproceeding
    Set Inproceeding Required Fields    John Doe    Test Title    Test Booktitle    2023
    Scroll Down  1000
    Click Submit Button    create_inproceeding
    Starting Page Should Be Open
    Page Should Contain    John Doe
    Page Should Contain    Test Title
    Click Element    name=delete
    Handle Alert
    Reference Has Been Deleted
    
*** Keywords ***

Reference Has Been Deleted
    Page Should Not Contain    John Doe