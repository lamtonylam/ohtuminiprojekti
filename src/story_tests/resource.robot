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
    Page Should Contain  Create a new improceedings reference

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
