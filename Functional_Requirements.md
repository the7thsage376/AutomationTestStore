# Functional Requirements of Automation Test Store
---
<!-- FR categories -->

## User Account management: <!-- Automation Heavy -->

**Fr-001**: User is able to register an account <br>
**Fr-002**: User is able to login to account <br>
**Fr-003**: User is able to logout

---
## Product search and discovery:

**Fr-004**: User is able to search for items in stock <!-- Learn how to automate scrolling through a website -->
**Fr-005**: User is able to filter items in stock
**Fr-006**: , and browse items<

---

## Cart Operations: <!--Automation heavy -->

**Fr-007**: User is able to add and remove items from cart <br>
**Fr-008**: User is able to select the desired amount of the item

---

## Stock Validation:

**Fr-009**: User is able to detect when an item is out of stock <br>
**Fr-010**: User is not able to select stock that exceeds the maximum amount per customer. <br>
**Fr-011**: User is not able to select stock that is below the minium amount per customer.

---
## Currency Conversion:

**Fr-012**: User is able to switch between available currencies <br>
**Fr-013**: User is able to see the price of the item updated after currency conversion.

---
## Checkout Process:

**Fr-014**: User is able to review items in cart <br>
**Fr-015**: User is able to enter their address for item delivery <br>
**Fr-016**: User is able to checkout

---
## Input Validation<!-- Automation heavy -->
<!-- For Pytest, learn how to write the expected error message into report file -->

**FR-017**: Website throws an error when login name and password are invalid<!-- Pytest must read the error line in assertions --> <br>
**FR-018**: Website throws and error message when login name and password provided are greater than 50 characters<br>
**Fr-019**: Website throws an error message when login name and password are less than 8 characters<br>
**FR-020**:  Website throws an error message when login name and password are empty<br>
**FR-021**: Website throws an error message when the email format is in the incorrect format(e.g no "@" symbol)

---
## Boundary-Value-Testing<!-- Automation heavy -->
<!-- Find out what the actual character limit is-->
**FR-022**: website will accept login name and password inputs that are exactly 8 characters<br>
**FR-023**: Website will accept login name and password inputs that are exactly 50 characters<br>
**FR-024**: website will reject login name and password inputs that are exactly 7 or 51 characters long, and throw an error

