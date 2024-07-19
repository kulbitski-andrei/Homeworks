*** Settings ***
Library  library_robot.py
Library    BuiltIn
Suite Setup  Setup Suite Data


*** Variables ***
${BOOK_TITLE}     Test Book
${BOOK_AUTHOR}    Test Author
${BOOK_PAGES}     123
${BOOK_ISBN}      978-3-16-148410-0
${READER_NAME}    Test Reader
${READER_NAME_2}  Another Reader


*** Test Cases ***

1. Take Book When Not Reserved Or Taken
    [Documentation]    Check successful taking of a book that is not reserved or taken by anyone
    [Tags]    positive    take_book    regression
    ${result}=  Take Book    ${reader1}    ${book}
    Log Book Status    ${book}
    Should Be True    ${result}
    Should Be Equal    ${book.status}    Taken
    Should Be Equal    ${book.taken_by}    ${reader1.name}
    Should Be Equal    ${book.reserved_by}   ${None}
    Reset Book Status    ${book}
    Log Book Status    ${book}

2. Take Book When Reserved By Current Reader
    [Documentation]    Check successful taking of a book that user reserved
    [Tags]    positive    take_book    regression
    ${result1}=  Reserve Book     ${reader1}    ${book}
    Should Be True    ${result1}
    ${result2}=  Take Book    ${reader1}    ${book}
    Log Book Status    ${book}
    Should Be True    ${result2}
    Should Be Equal    ${book.status}    Taken
    Should Be Equal    ${book.taken_by}    ${reader1.name}
    Should Be Equal    ${book.reserved_by}   ${None}
    Reset Book Status    ${book}
    Log Book Status    ${book}

3. Take Book When Reserved By Other Reader
    [Documentation]    Check error when trying to take a book reserved by other user
    [Tags]    negative    take_book    regression
    ${result}=  Reserve Book    ${reader1}    ${book}
    Should Be True    ${result}
    ${result2}=  Take Book    ${reader2}    ${book}
    Log Book Status    ${book}
    Should Not Be True    ${result2}
    Should Be Equal    ${book.status}    Reserved
    Should Be Equal    ${book.taken_by}    ${None}
    Should Be Equal    ${book.reserved_by}    ${reader1.name}
    Reset Book Status    ${book}
    Log Book Status    ${book}

4. Take Book When Already Taken
    [Documentation]    Check error when trying to take a book taken by other user
    [Tags]    negative    take_book    regression
    ${result1}=  Take Book    ${reader1}    ${book}
    Should Be True    ${result1}
    ${result2}=  Take Book    ${reader2}    ${book}
    Log Book Status    ${book}
    Should Not Be True    ${result2}
    Should Be Equal    ${book.status}    Taken
    Should Be Equal    ${book.taken_by}    ${reader1.name}
    Should Not Be Equal    ${book.taken_by}    ${reader2.name}
    Reset Book Status    ${book}
    Log Book Status    ${book}

5. Reserve Book When Not Reserved Or Taken
    [Documentation]    Check successful reservation of a book that is not reserved or taken by anyone
    [Tags]    positive    reserve_book    regression
    ${result}=  Reserve Book    ${reader1}    ${book}
    Log Book Status    ${book}
    Should Be True    ${result}
    Should Be Equal    ${book.status}    Reserved
    Should Be Equal    ${book.taken_by}    ${None}
    Should Be Equal    ${book.reserved_by}   ${reader1.name}
    Reset Book Status    ${book}
    Log Book Status    ${book}

6. Reserve Book When Already Reserved
    [Documentation]    Check error when trying to reserve an already reserved book
    [Tags]    negative    reserve_book    regression
    ${result1}=  Reserve Book    ${reader1}    ${book}
    Should Be True    ${result1}
    ${result2}=  Reserve Book    ${reader2}    ${book}
    Log Book Status    ${book}
    Should Not Be True    ${result2}
    Should Be Equal    ${book.status}    Reserved
    Should Be Equal    ${book.taken_by}    ${None}
    Should Be Equal    ${book.reserved_by}    ${reader1.name}
    Reset Book Status    ${book}
    Log Book Status    ${book}

7. Reserve Book When Already Taken
    [Documentation]    Check error when trying to reserve a book taken by other user
    [Tags]    negative    reserve_book    regression
    ${result1}=  Take Book    ${reader1}    ${book}
    Should Be True    ${result1}
    ${result2}=  Reserve Book    ${reader2}    ${book}
    Log Book Status    ${book}
    Should Not Be True    ${result2}
    Should Be Equal    ${book.status}    Taken
    Should Be Equal    ${book.taken_by}    ${reader1.name}
    Should Be Equal    ${book.reserved_by}   ${None}
    Reset Book Status    ${book}
    Log Book Status    ${book}

8. Return Book Reader Have
    [Documentation]    Check successful returning of a book that is taken by the current user
    [Tags]    positive    return_book    regression
    ${result1}=  Take Book    ${reader1}    ${book}
    Should Be True    ${result1}
    ${result2}=  Return Book    ${reader1}    ${book}
    Log Book Status    ${book}
    Should Be True    ${result1}
    Should Be Equal    ${book.status}    Available
    Should Be Equal    ${book.taken_by}    ${None}
    Should Be Equal    ${book.reserved_by}    ${None}
    Reset Book Status    ${book}
    Log Book Status    ${book}

9. Return Book Reader Do Not Have
    [Documentation]    Check error returning of a book that is not taken by the current user
    [Tags]    negative    return_book    regression
    ${result1}=  Return Book    ${reader1}    ${book}
    Log To Console    RESULT IS ${result1}
    Should Not Be True    ${result1}
    ${result2}=  Reserve Book    ${reader1}    ${book}
    Should Be True    ${result2}
    ${result3}=  Return Book    ${reader1}    ${book}
    Log Book Status    ${book}
    Should Not Be True    ${result3}
    Should Be Equal    ${book.status}    Reserved
    Should Be Equal    ${book.taken_by}    ${None}
    Should Be Equal    ${book.reserved_by}    ${reader1.name}
    Reset Book Status    ${book}
    Log Book Status    ${book}


*** Keywords ***

Create Reader Object
    [Arguments]    ${name}
    ${reader}=    Evaluate    library_robot.Reader("${name}")
    RETURN    ${reader}

Create Book Object
    [Arguments]    ${title}    ${author}    ${pages}    ${isbn}
    ${book}=    Evaluate    library_robot.Book("${title}", "${author}", ${pages}, "${isbn}")
    RETURN    ${book}

Reserve Book
    [Arguments]    ${reader}    ${book}
    ${result}=    Call Method    ${reader}    reserve_book    ${book}
    RETURN    ${result}

Take Book
    [Arguments]    ${reader}    ${book}
    ${result}=    Call Method    ${reader}    take_book    ${book}
    RETURN    ${result}

Return Book
    [Arguments]    ${reader}    ${book}
    ${result}=    Call Method    ${reader}    return_book    ${book}
    RETURN    ${result}

Log Book Status
    [Arguments]    ${book}
    Log To Console    Book status: ${book.status}, Reserved by: ${book.reserved_by}, Taken by ${book.taken_by}

Reset Book Status
    [Arguments]    ${book}
    Call Method    ${book}    reset_status

Setup Suite Data
    ${reader1}=  Create Reader Object    ${READER_NAME}
    ${reader2}=  Create Reader Object    ${READER_NAME_2}
    ${book}=    Create Book Object    ${BOOK_TITLE}    ${BOOK_AUTHOR}    ${BOOK_PAGES}    ${BOOK_ISBN}
    Set Suite Variable  ${book}
    Set Suite Variable  ${reader1}
    Set Suite Variable  ${reader2}
