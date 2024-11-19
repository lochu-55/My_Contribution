Feature: bank transactions
  tests pertaining to banking transactions like withdrawal deposit

  Scenario: withdrawal of money
    Given the account balance is 100
    When the account holder withdraws 30
    Then the account balance should be 70

  Scenario: removal of items from set
    Given the set of 3 fruits
    When the remove a fruit from the set
    Then the set will have 2 fruits


