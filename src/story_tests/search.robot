*** Settings ***
Resource  resource.robot
Suite Setup      Open And Configure Browser
Suite Teardown   Close Browser
Test Setup       Reset References

*** Test Cases ***
Search Should Show Added Reference
    Create Book And Article Reference With Required Fields
    Go To Starting Page
    Input Text To Search bar  article
    Page Should Contain  Jane Smith

Search With Invalid String Should Not Show Any References
    Create Book And Article Reference With Required Fields
    Go To Starting Page
    Input Text To Search bar  a_random_string_of_characters
    No References Should Be Visible