## Project Overview
This test plan is for documenting the planning and testing of the e-commerce website automationteststore.com.It is a fake e-commerce website used to practice UI automation.What will be tested is the core user flow, as well as building automation skills. such as login, adding items to the cart, searching for items, selecting desired quantity of items, converting to the correct currency and checking out. This project is for my QA upskilling journey, and reflects my improvements in quality assurance. The tools used in this testing project are Selenium webdriver, Pytest, Pytest Html, Faker, and page object model(POM).
## Scope
In-scope: registering and logging in an account, searching for items, adding them to the cart, checking out, checking if an item is out of stock, checking boundary values and edge cases using equivalence partitioning.
Out-Of-Scope: Payment confirmation
## Test Objectives<!-- Check off test objectives once completed -->
Verify that the user:
- [] can register and login to an account on the website
- [] search up items in the store
- [] add items to the cart
- [] check if an item is out of stock
- [] check if you can buy an item that exceeds the available stock
- [] check if you can buy an iten that's less than it's minimum stock purchase
- [] convert the price of an item into different currencies
- [] checkout 
## Test Strategy
This project uses automated UI testing with Selenium and Pytest to validate core user flows. The strategy focuses on functional testing of key features such as login, search, booking, and checkout. Tests are written in modular Pytest format and executed locally with HTML reports generated via pytest-html.

## Test Environment
**Browser(s)**: Microsoft Edge Version 141.0.3537.99 (Official build) (64-bit),<br> Chrome Version 138.0.7204.184 (Official Build) (64-bit)
**Network conditions**: 3G, 4G, WIFI
**Operating System**: Windows 11
**Autonation Tools**: Pytest, Pytest-HTML, Selenium Webdriver
## Test Deliverables <!-- Add relevant documents as we progress -->
- Test Plan
- Test cases
- Selenium test scripts
- Test execution report
## Entry And Exit Criteria
### Entry:
- Test cases are written and to be executed
- Test plan is complete
- Project file structure is complete
- Functional requirements are understood and approved
- Test Environment is set up and stable
### Exit:
- All test cases have been executed
- All test scripts run smoothly
- Test metrics meet expected threshold 
- Evidence(screenshots, videos) of testing have been captured

## Tools And Frameworks
- Selenium Webdriver
- Pytest
- Pytest-HTML
- Faker
- Page Object Model(POM)
## Appendices<!-- Add links to other files and folders -->

### Glossary <!--This one is for explaining different types of testing -->
*Entry Criteria*: The conditions that must be met before testing begins<br>
*Exit Criteria*: The conditions that must be satisfied before testing can be considered complete.

### Author & Ownership<!--Remove if you find it cringe-->
This test plan is authored and maintained by Lerato Moloi. It reflects personal accountability, continuous learning, and a commitment to quality engineering.

Version: 1.0  
Date: 2025-10-29
