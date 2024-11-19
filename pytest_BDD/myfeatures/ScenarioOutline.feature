Feature :Scenario outlines

  Scenario Outline: scene outline test
    Given there are <start> cucumbers
    When I deposit <deposit> cucumbers
    And I withdraw <withdraw> cucumbers
    Then I should have <final> cucumbers


    Examples:
      |start|deposit|withdraw|final|
      |12   |5      |7       |10   |
      |10   |5      |20      |-8   |
      |20   |5      |20      |5   |
