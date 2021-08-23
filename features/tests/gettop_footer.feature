# Created by HDL32DA01 at 8/17/2021
Feature: Verify footer links on Gettop
  # Enter feature description here

  Scenario: Footer shows Best Selling, Latest, Top Rated categories
    Given Open Gettop store
    Then Verify 3 Best Selling, Latest, Top Rated categories

  Scenario: Products in the footer have price, name, star rating
    Given Open Gettop store
    Then Verify price option in footer
    And Verify name option in footer
    And Verify star rating option in footer

 Scenario: User sees Copyright 2021 shown in footer
    Given Open Gettop store
    Then Verify Copyright 2021 © Gettop in footer

  Scenario: Footer has button to go back to top
    Given Open Gettop store
    Then Verify button to go back to top

  Scenario: Footer has working links to all product categories
      Given Open Gettop store
      When User can click footer link for iphone
      And User can click footer link for mac
      And User can click footer link for ipad
      And User can click footer link for watch
      And User can click footer link for accessories