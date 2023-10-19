*** Settings ***
Library    SeleniumLibrary
Library    Collections
Library    String


*** Test Cases ***
Run Python Script from Command Prompt
    Open Browser    https://www.gturesults.in/Default.aspx?ext=archive    Chrome
    Maximize Browser Window
