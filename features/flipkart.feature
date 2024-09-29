Feature: Flipkart Speakers Price Shorting Assertions
  Scenario: Verify speakers by price sorting low to high
    Given I Launch Chrome browser
    When Open Flipkart homepage
    And Click on Speakers and hover to soundbar
    And Click on soundbar
    Then Click on price low to high
    Then items price must sort low to high