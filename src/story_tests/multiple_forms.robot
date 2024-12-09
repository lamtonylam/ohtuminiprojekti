*** Settings ***
Resource  resource.robot
Suite Setup      Open And Configure Browser
Suite Teardown   Close Browser
Test Setup       Reset References

*** Test Cases ***
Create Inproceeding Reference With Required Fields
    Go To References Page
    Select Reference Type    inproceeding
    Set Inproceeding Required Fields    John Doe    Test Title    Test Booktitle    2023
    Scroll Down  1000
    Click Submit Button    create_inproceeding
    Starting Page Should Be Open
    Page Should Contain    John Doe
    Page Should Contain    Test Title

Create Article Reference With Required Fields
    Go To References Page
    Select Reference Type    article
    Set Article Required Fields      Jane Smith    Test Article    Test Journal    2023
    Scroll Down  1000
    Click Submit Button    create_article
    Starting Page Should Be Open
    Page Should Contain    Jane Smith
    Page Should Contain    Test Article

Create Book Reference With Required Fields
    Go To References Page
    Select Reference Type    book
    Set Book Required Fields      Robert Brown    2023    Test Book    Test Publisher    Test Address
    Scroll Down  1000
    Click Submit Button    create_book
    Starting Page Should Be Open
    Page Should Contain    Robert Brown
    Page Should Contain    Test Book

