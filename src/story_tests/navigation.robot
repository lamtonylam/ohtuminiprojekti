*** Settings ***
Resource  resource.robot
Suite Setup      Open And Configure Browser
Suite Teardown   Close Browser
Test Setup       Reset References

*** Test Cases ***
Navigate to Home Page From Form Page
    Go To Form Page
    Click Element  id=button_to_homepage
    Starting Page Should Be Open

Navigate to Form Page From Home Page
    Go To Starting Page
    Click Element  id=button_to_reference
    Form Page Should Be Open

Navigate to Preview Page From Home Page
    Go To Starting Page
    Click Element  id=button_to_preview
    Preview Page Should Be Open

Navigate to Home Page From Preview Page
    Go To Preview Page
    Click Element  id=link_to_homepage
    Starting Page Should Be Open