# Test Plan: AutomationTestStore UI Automation

## Project Overview
This test plan documents the planning and execution of automated UI testing for [automationteststore.com](https://automationteststore.com), a mock e-commerce website used for QA practice. The focus is on validating core user flows such as login, item search, cart management, currency conversion, and checkout — while building automation skills and showcasing QA strategy.

This project is part of my QA upskilling journey and reflects growth in test design, automation, and reporting. Tools used include Selenium WebDriver, Pytest, Pytest-HTML, Faker, and the Page Object Model (POM) design pattern.

---

## Scope

**In-Scope:**
- User registration and login
- Searching for items
- Adding items to the cart
- Checking out
- Detecting out-of-stock items
- Validating boundary and edge cases using equivalence partitioning and boundary value analysis

**Out-of-Scope:**
- Payment confirmation and backend transaction validation

---

## Test Objectives

Verify that the user can:
- [x] Register and log in to an account
- [ ] Search for items in the store
- [ ] Add items to the cart
- [ ] Detect when an item is out of stock
- [ ] Attempt to purchase more than available stock
- [ ] Attempt to purchase less than the minimum allowed quantity
- [ ] Convert item prices into different currencies
- [ ] Complete the checkout process

---

## Test Strategy

This project uses automated UI testing with Selenium and Pytest to validate functional flows. Tests are modular, maintainable, and structured using Pytest fixtures and the Page Object Model. Execution is local, with HTML reports generated via `pytest-html` for visibility and traceability.

---

## Test Environment

- **Browsers**:  
  - Microsoft Edge Version 141.0.3537.99 (64-bit)  
  - Chrome Version 138.0.7204.184 (64-bit)

- **Operating System**: Windows 11  
- **Network Conditions**: 3G, 4G, Wi-Fi  
- **Automation Tools**: Selenium WebDriver, Pytest, Pytest-HTML, Faker

---

## Test Deliverables

- Test Plan  
- Test Cases  
- Selenium Test Scripts  
- Test Execution Report (HTML)
- Screenshots

---

## Entry and Exit Criteria

### Entry Criteria
- Functional requirements are understood and approved
- Test plan and test cases are complete
- Project structure is finalized
- Test environment is stable

### Exit Criteria
- All test cases executed
- All scripts run without critical errors
- Test metrics meet defined thresholds
- Screenshots or videos captured as evidence

---

## Tools and Frameworks

- Selenium WebDriver  
- Pytest  
- Pytest-HTML  
- Faker  
- Page Object Model (POM)

---

## Appendices

### Glossary
- **Entry Criteria**: Conditions required before testing begins  
- **Exit Criteria**: Conditions required before testing is considered complete

### Author & Ownership
This test plan is authored and maintained by **Lerato Moloi**. It reflects personal accountability, continuous learning, and a commitment to quality engineering.

**Version**: 2.0  
**Date**: 2025-10-30