# Bug Report 2: In a to-do list, the created task gets unintentionally duplicated, if the associated to-do list is shared to more than one user
**Authors:** *Kim Järvinen* & *Riki Järvinen*<br>
**Date:** *10.12.2025*

---

## 1. Summary
The task created in the to-do list is unintentionally duplicated when the associated to-do list is shared with more than one user. The unintentionally duplicated tasks are not visible to users with permissions, and when one of the duplicates is deleted, all associated instances are deleted as well.

---

## 2. Environment
- Application name: *Todo list application*
- Application type: *Web application*
- Application version: *0.0.1*
- Browser: *Firefox 146.0*
- Operating system: *Windows 11 Home*

---

## 3. Preconditions
1. More than 2 existing users
2. A to-do list, which is shared to more than 1 user, by the owner
3. A task in the associated to-do list, which contains text

---

## 4. Steps to Reproduce
1. Login as any user
2. Create to-do list ("New todo list")
3. Share it with at least two users (roles don't matter)
4. Create new task ("New task")
5. Return to the main page ("My todo lists")
6. Select the to-do you created
7. You should see the created task duplicated

---

## 5. Expected Result
The created task should not be duplicated when navigating back to the same page after sharing the associated to-do list to more than one user.

---

## 6. Actual Behavior
The created task gets unintentionally duplicated when navigating back to the same page after sharing the associated to-do list to more than one user. The unintentionally duplicated tasks are only visible to the to-do list creator.

---

## 7. Attachments
A to-do list with a created task shared to 2 users:

![To-do list with created task shared to 2 users](./Images/BugReport2/1.png "To-do list with created task shared to 2 users")

The same to-do list when navigated back to the same page (see the duplicated task):

![The same to-do list when navigated back to the same page](./Images/BugReport2/2.png "The same to-do list when navigated back to the same page")

---

## 8. Reproducibility
Reproducible 100% when sharing a to-do list with two or more users.

---

## 9. Severity & Priority
- Severity classification: *Medium*
- Priority: *P2 (medium)*
- Explanation: *The bug doesn't seem to cause data leakage or security problems, but it may harm usability*

---

## 10. Additional Notes
Temporary workaround: *Do not share the to-do lists to more than one user*