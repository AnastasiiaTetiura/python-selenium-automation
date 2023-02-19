# Created by anastasiiatetiura at 2/18/23
Feature: Test Scenarios for Empty Cart verification

  Scenario: Empty cart is empty
    Given Go to Amazon page
    When Click on Cart icon
    Then Text Your cart is empty is displayed
