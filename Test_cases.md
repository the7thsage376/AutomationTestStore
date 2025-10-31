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

### Fr-001: Verifyng if user can register an account <br>

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

### Fr-004: Verify if user is able 
