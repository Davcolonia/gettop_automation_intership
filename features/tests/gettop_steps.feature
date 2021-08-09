# Created by HDL32DA01 at 8/5/2021
#Clicking on Cart icon opens Empty Cart page if no products were added
#Hovering over empty cart icon shows "No products in the cart." message
#Add product to cart, verify that price in top nav menu is correct
#Add products to cart, verify that amount of items shown in top nav menu are correct
#Add products to cart, hover over cart icon, verify correct products and subtotal shown
#Add products to cart, hover over cart icon, verify user can click on "View Cart" and is taken to cart page
#Add products to cart, hover over cart icon, verify user can click on "Checkout" and is taken to checkout page
#Add a product to cart, hover over cart icon, verify user can remove a product



Feature: Verify cart in Gettop

    Scenario: Clicking on Cart icon opens Empty Cart page if no products were added
      Given Open Gettop store
      When User clicks on cart icon
      Then Your cart is currently empty. is displayed


  Scenario: Hovering on Cart icon shows No products in the cart if no products were added
    Given Open Gettop store
    When User hovers cart icon
    Then No products in the cart is shown

  Scenario: Add product to cart, verify that price in top nav menu is correct
    Given Go to product ipad
    When Click on the Add to cart button in bottom
    Then Verify price $329.00 in the nav menu
    And Verify 1 item in the nav menu
    And Verify dropdown price $329.00
    And Verify expected product

   Scenario: After adding items, verify user can click on "View Cart" and is taken to cart page
    Given Go to product ipad
    When Click on the Add to cart button in bottom
     And click on view cart
     Then Verify items in cart page

Scenario: After adding items, verify user can click on "Checkout" and is taken to checkout
    Given Go to product ipad
    When Click on the Add to cart button in bottom
     And click on checkout
     Then Verify checkout page

  Scenario: After adding items, verify user can remove items
    Given Go to product ipad
    When Click on the Add to cart button in bottom
     And click on remove items
     Then Verify no items
