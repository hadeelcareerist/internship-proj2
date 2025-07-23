
Feature: Off Plan Pagination

  Scenario: Open Off Plan page and go through pagination
    Given I open the Reelly site
    When I log in
    And I click on the off plan menu
    Then I should be on the off plan page
    When I go to the final page using the pagination button
    And I go back to the first page using the pagination button
    Then I close the browser
