Feature: Account registry


 Scenario: User is able to create a new account
   Given Number of accounts in registry equals: "0"
   When I create an account using name: "kurt", last name: "cobain", pesel: "79103075873"
   Then Number of accounts in registry equals: "1"
   Then Account with pesel "79103075873" exists in registry


 Scenario: User is able to create a second account
   Given Number of accounts in registry equals: "1"
   When I create an account using name: "john", last name: "lennon", pesel: "94012298328"
   Then Number of accounts in registry equals: "2"
   Then Account with pesel "94012298328" exists in registry


 Scenario: Admin user is able to save the account registry
   When I save the account registry
   Then Number of accounts in registry equals: "2"


 Scenario: User is able to delete already created account
   Given Account with pesel "79103075873" exists in registry
   When I delete account with pesel: "79103075873"
   Then Account with pesel "79103075873" does not exists in registry


 Scenario: User is able to update last name saved in account
   Given Account with pesel "94012298328" exists in registry
   When I update last name in account with pesel "94012298328" to "smith"
   Then Last name in account with pesel "94012298328" is "smith"


 Scenario: User is able to load account registry
   Given Number of accounts in registry equals: "1"
   When I load the account registry
   Then Number of accounts in registry equals: "2"
   And Account with pesel "79103075873" exists in registry
   And Account with pesel "94012298328" exists in registry


 Scenario: User is able to delete both accounts
   Given Account with pesel "79103075873" exists in registry
    And Account with pesel "94012298328" exists in registry
    When I delete account with pesel: "79103075873"
    And I delete account with pesel: "94012298328"
    Then Account with pesel "79103075873" does not exists in registry
    And Account with pesel "94012298328" does not exists in registry

  Scenario: cleanup
    Given Number of accounts in registry equals: "0"
    When I save the account registry
    Then Number of accounts in registry equals: "0"
