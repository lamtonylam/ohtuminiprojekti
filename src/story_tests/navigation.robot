*** Settings ***
Resource  resource.robot
Suite Setup      Open And Configure Browser
Suite Teardown   Close Browser
Test Setup       Reset References

*** Test Cases ***
Navigate to Home Page
    Go To Starting Page
    Starting Page Should Be Open

Navigate to Form Page
    Go to Form Page
    Form Page Should Be Open