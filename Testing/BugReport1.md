# Bug Report 1: In to-do list sharing option, dropdown list for role selection breaks when accidentally typing something in it
**Authors:** *Kim Järvinen* & *Riki Järvinen*<br>
**Date:** *11.12.2025*

---

## 1. Summary
When sharing to-do list to another member and selecting role, if you accidentally type anything with your keyboard the whole dropdown menu breaks and you cannot
select a role. Application stores the latest selected role for the user, even if wanting to assign user with something else. 

---

## 2. Environment
- Application name: *Todo list application*
- Application type: *Web application*
- Application version: *0.0.1*
- Browser: *Brave 1.85.111*
- Browser: *Chrome 143.0.7499.109*
- Browser: *Edge 143.0.3650.75*

---

## 3. Preconditions
1. To-do list created
2. Roles existing for the application for users
3. Application has users

---

## 4. Steps to Reproduce
1. Login as any user
2. Create to-do list ("New todo list")
3. Locate to created to-do list
4. Locate 'Share' option and open it
5. Assign user to give role to
6. Select any role for the user
7. Press any character on keyboard
8. You should see dropdown menu cannot be opened

---

## 5. Expected Result
Text field should empty itself and allow user to use dropdown menu as intended.

---

## 6. Actual Behavior
When accidentally pressing a character on the keyboard, dropdown menu breaks and cannot be used unless UI is refreshed.

---

## 7. Reproducibility
When testing, it was reproduciable everytime with the given steps to reproduce. 

---

## 8. Severity & Priority
- Severity classification: *Low*
- Priority: *P3 (low)*
- Explanation: *The bug can harm usability of the application if user has habit of accidentally pressing buttons* 
---

## 9. Additional Notes
You need to be sure when selecting a role for the user and not accidentally typing anything on your keyboard. 