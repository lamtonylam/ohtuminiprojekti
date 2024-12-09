*** Settings ***
Library  SeleniumLibrary
Library    OperatingSystem

*** Variables ***
${SERVER}     localhost:5001
${DELAY}      0.5 seconds
${HOME_URL}   http://${SERVER}
${RESET_URL}  http://${SERVER}/reset_db
${FORM_URL}   http://${SERVER}/new_reference
${PREVIEW_URL}    http://${SERVER}/preview
${BROWSER}    chrome
${HEADLESS}   false

*** Keywords ***
Open And Configure Browser
    IF  $BROWSER == 'chrome'
        ${options}  Evaluate  sys.modules['selenium.webdriver'].ChromeOptions()  sys
    ELSE IF  $BROWSER == 'firefox'
        ${options}  Evaluate  sys.modules['selenium.webdriver'].FirefoxOptions()  sys
    END
    IF  $HEADLESS == 'true'
        Set Selenium Speed  0
        Call Method  ${options}  add_argument  --headless
    ELSE
        Set Selenium Speed  ${DELAY}
    END
    Open Browser  browser=${BROWSER}  options=${options}
    Set Window Size  1920  1080

Reset References
    Go To  ${RESET_URL}

Go To Starting Page
    Go To  ${HOME_URL}

Go To Form Page
    Go To  ${FORM_URL}

Go To Preview Page
    Go To  ${PREVIEW_URL}

Starting Page Should Be Open
    Title Should Be  References Management App

Form Page Should Be Open
    Page Should Contain  Create a new reference

Preview Page Should Be Open
    Page Should Contain  Preview
#??? page doesent contain anythin for now

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

Set Editor
    [Arguments]  ${editor}
    Input Text  editor  ${editor}

Scroll Down
    [Arguments]  ${scroll_height}=1000
    Execute Javascript  window.scrollBy(0, ${scroll_height})

Go To References Page
    Go To    ${HOME_URL}/new_reference

Select Reference Type
    [Arguments]    ${type}
    Select From List By Value    id=type    ${type}

Set Inproceeding Required Fields
    [Arguments]        ${author}    ${title}    ${booktitle}    ${year}
    Input Text    id=inproceeding_author    ${author}
    Input Text    id=inproceeding_title    ${title}
    Input Text    id=inproceeding_booktitle    ${booktitle}
    Input Text    id=inproceeding_year    ${year}

Set Article Required Fields
    [Arguments]    ${author}    ${title}    ${journal}    ${year}
    Input Text    id=article_author    ${author}
    Input Text    id=article_title    ${title}
    Input Text    id=article_journal    ${journal}
    Input Text    id=article_year    ${year}

Set Book Required Fields
    [Arguments]       ${author}    ${year}    ${title}    ${publisher}    ${address}
    Input Text    id=book_author    ${author}
    Input Text    id=book_year    ${year}
    Input Text    id=book_title    ${title}
    Input Text    id=book_publisher    ${publisher}
    Input Text    id=book_address    ${address}

Click Submit Button
    [Arguments]    ${button_id}
    Click Button     ${button_id}
 

    