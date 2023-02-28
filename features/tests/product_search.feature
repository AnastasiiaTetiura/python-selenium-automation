# Created by Svetlana at 4/4/19
Feature: Test Scenarios for Search functionality

  Scenario: User can search for a product
    Given Open Google page
    When Input Monitor into search field
    And Click on search icon
    Then Product results for Monitor are shown


  Scenario: Add an item to the cart
    Given Go to Amazon page
    When Input text teapot
    When Click on the search button
    And Click on the first item
    And Click Add to Cart button
    When Click on Cart icon
    Then Verify has 1 item


  Scenario: Best Sellers page has 5 links
    Given Go to Amazon page
    When Select hamburger manu
    And Select Best Sellers in dropdown
    Then Verify header has {5} links

