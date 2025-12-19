# Test Plan
**Authors:** *Kim Järvinen* & *Riki Järvinen*<br>
**Date:** *5.12.2025*

---

## 1. Introduction
New application requires testing to ensure the application works as inteded to end user.
Purpose of testing is meant to cover user functional use cases for the application and to ensure
application responds with correct outputs.
Testing is applied by using API testing and End-to-End testing.

---

## 2. Environments
Operating system:
- Windows 11 Standard / Pro
Browsers used for testing (current version): 
- Firefox 146
- Chrome 143
- Edge 143
- Brave 1.85
  
---

## 3. Tools
Manual testing used to test out layouts functionalitibies with different setups.
Automation is used for testing. 
End-to-End testing tools provided by playwright are used to automate user inputs and checking outputs.
Github actions is used for continuous integration purposes.

---

## 4. In Scope
Testing is done to:
- API endpoints
- User functionalibities
    - Registering
    - Login
    - Creating / Deleting to-do list
    - Logout
- Site responsiveness by manual testing.
  
---

## 5. Out of Scope
Due to limitation of operating system applications used in MacOS cannot be tested (Safari etc.).
Potential security risks i.e. SQL injection, supply chain attacks, code injection.

---
