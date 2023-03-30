Feature: Test Scenarios for Empty Cart verification

  Scenario: Empty cart is empty
    Given Go to Amazon page
    When Click on Cart icon
    Then Text "Your Amazon cart is empty" is displayed

  Scenario: User can see text Sign In
    Given Open Amazon page
    When Click on Orders button
    Then Page Sing In is open






