Feature: User can use header fucntionalities

  Scenario: User can surch Pet supplies department
    Given Open Amazon page
    When Select department by alias Pet supplies
    When Input text Cat tree
    When Click on the search button
    Then Verify Pet supplies department is selected

   Scenario: User see deals in Clothing Department
    Given Open Amazon page
    When Select department by alias Clothing, Shoes and Jewelry
    When Input text Onesy
    When Click on the search button
    #Then Verify Clothing, Shoes and Jewelry department is selected
    When Hover over New Arrivals
    Then Verify New Deals are displayed

