Feature: Transfers

  Scenario: Incoming transfer
    Given a personal account with the balance of 0
    When an incoming transfer of 100 is credited
    Then the balance should be 100

  Scenario: Incoming transfer with a negative amount
    Given a personal account with the balance of 0
    When an incoming transfer of -100 is credited
    Then the balance should be 0

  Scenario: Outgoing transfer with insufficient balance
    Given a personal account with the balance of 50
    When an outgoing transfer of 100 is initiated
    Then the balance should be 50

  Scenario: Series of transfers
    Given a personal account with the balance of 0
    When incoming transfers of 100 and 120 are credited, and an outgoing transfer of 50 is initiated
    Then the balance should be 170

  Scenario: Express personal account transfer
    Given a personal account with the balance of 100
    When an express outgoing transfer of 50 is initiated
    Then the balance should be 49

  Scenario: Outgoing transfer with a promo code
    Given a personal account with promo code "PROM_123"
    When an outgoing transfer of 20 is initiated
    Then the balance should be 30