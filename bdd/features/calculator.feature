# -- FILE: features/calculator.feature
Feature: Calculator
  As a user a user
  I want to be able to add numbers
  So that I can calculate the sum

  Scenario: Add two numbers
    Given I have entered 5 into the calculator
    And I have entered 10 into the calculator
    When I press add
    Then the result should be 15 on the screen




