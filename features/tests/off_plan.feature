
Feature: Off Plan Pagination

  Scenario: Open Off Plan page and go through pagination
    Given I open the Reelly site
    When I log in
    And I go to the Off-plan page
    And I go to the Secondary page
    And I go back to the Off-plan page
    Then I should be on the off plan page
    When I go to the final page using the pagination button
    And I go back to the first page using the pagination button
