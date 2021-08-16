# Created by HDL32DA01 at 8/15/2021
Feature:  User can sort by rating
  # Enter feature description here

  Scenario: User can sort by rating
    Given Open Gettop product page
      When User clicks sort by price
      And User can click through pages
      Then url opens with pages sorted by Rating
