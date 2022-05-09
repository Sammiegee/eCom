Feature: Confirming that product categories can be selected by users

  Scenario: Success for browsing through product categories
     Given I navigate to the index page
      When I select a category
      Then I should be able to see products in that category
      Then I should be able to select a product