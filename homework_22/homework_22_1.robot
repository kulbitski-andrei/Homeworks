*** Settings ***
Library  bank_robot.py
Library    BuiltIn
Suite Setup  Setup Suite Data

*** Variables ***
${HUNDRED}    100
${ZERO}    0
${YEARS_AMOUNT}    5


*** Test Cases ***

1. Positive Test Person Makes A Deposit
    [Documentation]    This test validates the Calculate Deposit Payouts function.
    [Tags]    positive    regression
    ${type}=    Evaluate    str(type(${HUNDRED}))
    ${type}=    Evaluate    str(type(${ZERO}))
    ${YEARS_AS_INT}=    Convert To Integer   ${YEARS_AMOUNT}
    ${result}=  Calculate Deposit Payouts    ${bank}    ${client1}    ${YEARS_AS_INT}
    ${expected_result}=    Set Variable    164.53
    Should Be Equal As Numbers    ${result}    ${expected_result}


2. Positive Test Person Makes A Deposit
    [Documentation]    This test validates return of ValueError when invalid Amount of years chosen (<= 0)
    [Tags]    negative    regression
    ${type}=    Evaluate    str(type(${HUNDRED}))
    ${type}=    Evaluate    str(type(${ZERO}))
    ${YEARS_AS_INT}=    Convert To Integer   ${ZERO}
    Run Keyword And Expect Error    *ValueError*    Calculate Deposit Payouts    ${bank}    ${client1}    ${YEARS_AS_INT}


*** Keywords ***
Create Bank Object
    [Arguments]    ${bank_name}    ${annual_rate}
    ${bank}=    Evaluate    bank_robot.Bank("${bank_name}", ${annual_rate})
    RETURN    ${bank}

Create Client Object
    [Arguments]    ${name}    ${money_amount}
    ${client}=    Evaluate    bank_robot.Client("${name}", ${money_amount})
    RETURN    ${client}

Calculate Deposit Payouts
    [Arguments]    ${bank}    ${client}    ${years}
    ${result}=    Call Method    ${bank}    deposit    ${client}    ${years}
    RETURN    ${result}

Setup Suite Data
    Convert To Number    ${HUNDRED}
    Convert To Number    ${ZERO}
    ${ANNUAL_RATE_AS_FLOAT}=    Convert To Number    0.10
    ${bank}=  Create Bank Object    BSB    ${ANNUAL_RATE_AS_FLOAT}
    ${client1}=  Create Client Object    Socrates    ${HUNDRED}
    ${client2}=  Create Client Object    Plato    ${HUNDRED}
    ${client3}=  Create Client Object    Aristotle    ${ZERO}
    Set Suite Variable  ${bank}
    Set Suite Variable  ${client1}
    Set Suite Variable  ${client2}
    Set Suite Variable  ${client3}
    Log To Console    ${HUNDRED}