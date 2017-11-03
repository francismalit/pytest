*** Settings ***
Library math.py

*** Test Cases ***
TC1
    ${result}=  Add  10  2
    Log to console  ${result}
    ${result}=  Subract  10  2
    Log to console  ${result}
    ${result}=  Multiply  10  2
    Log to console  ${result}
    ${result}=  Divide  10  2
    Log to console  ${result}
    ${result}=  Square  10  2
    Log to console  ${result}
    Provided precondition
    When action
    Then check expectations


*** Keywords ***
Provided precondition
    Setup system under test