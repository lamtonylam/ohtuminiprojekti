*** Settings ***
Resource  resource.robot
Suite Setup      Open And Configure Browser
Suite Teardown   Close Browser
Test Setup       Reset References

*** Test Cases ***
Create Inproceeding Reference With Required Fields
    Go To References Page
    Select Reference Type    inproceeding
    Set Inproceeding Required Fields    test_inproc    John Doe    Test Title    Test Booktitle    2023
    Scroll Down  1000
    Click Submit Button    create_inproceeding
    Starting Page Should Be Open
    Page Should Contain    test_inproc
    Page Should Contain    John Doe
    Page Should Contain    Test Title

Create Article Reference With Required Fields
    Go To References Page
    Select Reference Type    article
    Set Article Required Fields    test_article    Jane Smith    Test Article    Test Journal    2023
    Scroll Down  1000
    Click Submit Button    create_article
    Starting Page Should Be Open
    Page Should Contain    test_article
    Page Should Contain    Jane Smith
    Page Should Contain    Test Article

Create Book Reference With Required Fields
    Go To References Page
    Select Reference Type    book
    Set Book Required Fields    test_book    Robert Brown    2023    Test Book    Test Publisher    Test Address
    Scroll Down  1000
    Click Submit Button    create_book
    Starting Page Should Be Open
    Page Should Contain    test_book
    Page Should Contain    Robert Brown
    Page Should Contain    Test Book

*** Keywords ***
Go To References Page
    Go To    ${HOME_URL}/new_reference

Select Reference Type
    [Arguments]    ${type}
    Select From List By Value    id=type    ${type}

Set Inproceeding Required Fields
    [Arguments]    ${ref_id}    ${author}    ${title}    ${booktitle}    ${year}
    Input Text    id=inproceeding_reference_id    ${ref_id}
    Input Text    id=inproceeding_author    ${author}
    Input Text    id=inproceeding_title    ${title}
    Input Text    id=inproceeding_booktitle    ${booktitle}
    Input Text    id=inproceeding_year    ${year}

Set Article Required Fields
    [Arguments]    ${ref_id}    ${author}    ${title}    ${journal}    ${year}
    Input Text    id=article_reference_id    ${ref_id}
    Input Text    id=article_author    ${author}
    Input Text    id=article_title    ${title}
    Input Text    id=article_journal    ${journal}
    Input Text    id=article_year    ${year}

Set Book Required Fields
    [Arguments]    ${ref_id}    ${author}    ${year}    ${title}    ${publisher}    ${address}
    Input Text    id=book_reference_id    ${ref_id}
    Input Text    id=book_author    ${author}
    Input Text    id=book_year    ${year}
    Input Text    id=book_title    ${title}
    Input Text    id=book_publisher    ${publisher}
    Input Text    id=book_address    ${address}

Click Submit Button
    [Arguments]    ${button_id}
    Click Button     ${button_id}