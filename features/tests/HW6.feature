Feature: Home Work for Lesson 6

  Scenario: User can open and close Amazon Privacy Notice
    Given Navigate to Terms and Conditions page
    When Store original windows
    And Click on Amazon Privacy Notice link
    And Switch to the newly opened window
    Then Verify Amazon Privacy Notice page is opened
    And User can close new window and switch back to original
