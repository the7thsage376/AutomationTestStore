# Automation Test Store Test Cases

---
## Test Case template:
**Preconditions**:<br>
**Steps To Reproduce**:
**Expected Result**:<br>
**Actual Result**:
**Environment used**: Microsoft Edge, Chrome
**Status**: To be executed<br>
**Evidence**:![alt text](relative/path/to/screenshot)

## User Account management:

### Fr-001: Verifying if user can register an account <br>

**Preconditions**:<br> <!-- Use faker for fake test data -->
User is on the registration page of the website
**Steps To Reproduce**:
1. Enter credentials(name,surname, email,number)
2. Enter your address
3. Enter login details(login name, password)

**Expected Result**: New user account is registered<br>
**Actual Result**: New user account is successfully created<br>
**Environment used**: Microsoft Edge
**Status**: Passed <br>
**Evidence**:![User registration screenshot](Selenium/Screenshots/registration.png)

<!-- Use this template for future test cases -->

### Fr-002: Verify if user is able to login to account
**Preconditions**: User is on the "login or register" tab<br>
**Steps To Reproduce**:
1. Click on "Returning customer"
2. Enter your login name and password
3. Click on the "Login" button
**Expected Result**: User is logged into account<br>
**Actual Result**: User successfully logged in
**Environment used**: Microsoft Edge
**Status**: Passed<br>
**Evidence**:![login screenshot](Selenium/Screenshots/login.png)

### Fr-003: Verify if user able to logout of the account
**Preconditions**:<br>
User is logged into their account
**Steps To Reproduce**:
1. Click on the "logoff" button
**Expected Result**:User is logged out of the account<br>
**Actual Result**: User successfully logged out of the account
**Environment used**: Microsoft Edge
**Status**: Passed <br>
**Evidence**:![logout screenshot](Selenium/Screenshots/logout.png)

---

## Product search and discovery:

### Fr-004: Verify is user is able to search for items in stock
**Preconditions**: User is logged in to account<br>
**Steps To Reproduce**:
1. Search for an item on the "search" bar
2. Click Enter after writing item
3. Verify if item is in stock
**Expected Result**: Desired item is displayed and in stock<br>
**Actual Result**: Desired item is in stock and dispayed on screen
**Environment used**: Microsoft Edge
**Status**: Passed<br>
**Evidence**:![Search Bar Screenshot](Selenium/Screenshots/searchbar.png)

### Fr-005: Verify if user is able to filter items in stock
**Preconditions**:<br>
**Steps To Reproduce**:
**Expected Result**:<br>
**Actual Result**:
**Environment used**: Microsoft Edge, Chrome
**Status**: To be executed<br>
**Evidence**:![alt text](relative/path/to/screenshot)


## Cart Operation

### FR-006: Verify if user is able to add or remove items in cart
**Preconditions**:<br>
**Steps To Reproduce**:
**Expected Result**:<br>
**Actual Result**:
**Environment used**: Microsoft Edge, Chrome
**Status**: To be executed<br>
**Evidence**:![alt text](relative/path/to/screenshot)

### Fr-007: Verify if user is able to select desired amount of item in stock
**Preconditions**:<br>
**Steps To Reproduce**:
**Expected Result**:<br>
**Actual Result**:
**Environment used**: Microsoft Edge, Chrome
**Status**: To be executed<br>
**Evidence**:![alt text](relative/path/to/screenshot)


## Stock Validation

### Fr-008: Verify if user can detect when an item is out of stock <!-- User better wording for this -->
**Preconditions**:<br>
**Steps To Reproduce**:
**Expected Result**:<br>
**Actual Result**:
**Environment used**: Microsoft Edge, Chrome
**Status**: To be executed<br>
**Evidence**:![alt text](relative/path/to/screenshot)

### Fr-009: Verify if user is not able to select stock that exceeds the max limit per customer
**Preconditions**:<br>
**Steps To Reproduce**:
**Expected Result**:<br>
**Actual Result**:
**Environment used**: Microsoft Edge, Chrome
**Status**: To be executed<br>
**Evidence**:![alt text](relative/path/to/screenshot)

### Fr-010: Verify if user can select stock that's below the min limit per customer
**Preconditions**:<br>
**Steps To Reproduce**:
**Expected Result**:<br>
**Actual Result**:
**Environment used**: Microsoft Edge, Chrome
**Status**: To be executed<br>
**Evidence**:![alt text](relative/path/to/screenshot)


## Currency Conversion

### Fr-011: Verify if user is able to switch between currencies
**Preconditions**:<br>
**Steps To Reproduce**:
**Expected Result**:<br>
**Actual Result**:
**Environment used**: Microsoft Edge, Chrome
**Status**: To be executed<br>
**Evidence**:![alt text](relative/path/to/screenshot)

### Fr-012: Verify if price of item is changed when currency is changed <!-- Change wording -->
**Preconditions**:<br>
**Steps To Reproduce**:
**Expected Result**:<br>
**Actual Result**:
**Environment used**: Microsoft Edge, Chrome
**Status**: To be executed<br>
**Evidence**:![alt text](relative/path/to/screenshot)

## Checkout Process

### Fr-013: Verify if user can review items in cart
**Preconditions**:<br>
**Steps To Reproduce**:
**Expected Result**:<br>
**Actual Result**:
**Environment used**: Microsoft Edge, Chrome
**Status**: To be executed<br>
**Evidence**:![alt text](relative/path/to/screenshot)

### Fr-014: Verify if user can enter their address for item delivery
**Preconditions**:<br>
**Steps To Reproduce**:
**Expected Result**:<br>
**Actual Result**:
**Environment used**: Microsoft Edge, Chrome
**Status**: To be executed<br>
**Evidence**:![alt text](relative/path/to/screenshot)

### Fr-015: Verify if user is able to checkout
**Preconditions**:<br>
**Steps To Reproduce**:
**Expected Result**:<br>
**Actual Result**:
**Environment used**: Microsoft Edge, Chrome
**Status**: To be executed<br>
**Evidence**:![alt text](relative/path/to/screenshot)

 ## Input Validation

 ### Fr-016: 

