*** Settings ***
Resource  resource.robot
Suite Setup      Open And Configure Browser
Suite Teardown   Close Browser
Test Setup       Reset References

*** Variables ***
${DOWNLOAD_DIR}    ${CURDIR}/download
${BIBTEX_FILE}    references.bib

*** Test Cases ***
Download Bibtex File
    Go To Form Page
    Form Page Should Be Open
    Set Reference_id  TestId
    Set Author  TestAuthor
    Set Title  TestTitle
    Set Booktitle  TestBooktitle
    Set Year  2024
    Click Button  create
    Starting Page Should Be Open
    Page Should Contain    TestId
    Page Should Contain    TestAuthor

    Go To Starting Page
    ${prefs}=    Create Dictionary
    ...    download.default_directory=${DOWNLOAD_DIR}
    ...    download.prompt_for_download=False
    ...    download.directory_upgrade=True
    ${options}=    Evaluate    sys.modules['selenium.webdriver'].ChromeOptions()    sys
    Call Method    ${options}    add_argument    --headless
    Call Method    ${options}    add_experimental_option    prefs    ${prefs}
    Open Browser   http://localhost:5001/    Chrome    options=${options} 
    Click Button  download
    Sleep  5s
    ${files}=    List Files In Directory  ${DOWNLOAD_DIR}
    Length Should Be  ${files}    1
    Should Contain    ${files}    ${BIBTEX_FILE}
    Remove Directory    ${DOWNLOAD_DIR}    recursive=true
