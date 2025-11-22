For automated testing, there are three tasks: (1) design and write automated end-to-end tests, (2) design and write API tests, and (3) setup a continuous integration (CI) pipeline using GitHub Actions.

You are free to choose the framework (e.g. Robot Framework, Playwright, Cypress, Selenium etc.) for the end-to-end tests and API tests. However, make sure to add clear instructions in a specific README.md file on how to install all required dependencies for the tests and how to run the tests

The e2e tests should cover the authentication functionality, creating, viewing, editing and sharing todo lists and todo items. More specifically, at least four of the following user stories should be covered by the e2e tests:

As a user, I want to be able to register to the application
As a user, I want to be able to log in to the application
As a user, I want to be able to log out from the application
As a user, I want to be able to create and delete todo lists
As a todolist's owner, I want to be able to modify a todo list's name and description
As a todolist's owner, I want to be able to create and delete todo items in a todo list
As a todolist's owner, I want to be able to edit a todo item's description
As a todolist's owner, I want to be able to share a todo list with another user
As a shared todolist's recipient (e.g. editor), I want to be able to view a todo list that is shared with me, including the todo items
The API tests should cover at least five API endpoints of your own choosing in the backend API (the endpoints are found in the directory backend/src/controller/ and can be accessed also from http://localhost:4322/docs once the backend is running). Like with the e2e-tests, you are free to choose the tooling for the API tests, and should make sure to add clear instructions in a specific README.md file on how to install all the required dependencies for the tests and how to run the tests. You can also modify the existing backend project dependencies and code as needed for the API tests.

The CI should be implemented as a Github Actions workflow that executes the end-to-end tests on each push to a remote repository. For passing with merits, there should also be a workflow for running the API tests, at least one form of non-functional automated tests, and smoke tests (a selection of e2e-tests to run on every push) should be separated from the full e2e-test test suite (scheduled to run once a day). The non-functional tests could be, for example, performance tests, third-party vulnerability scanning, or some form of static code analysis.

Any failing end-to-end test or API test should be due to actual faults in the application, not due to faults in the tests or the test environment. In case some tests fail due to application faults, please document the faults in the test setup README.md files so that peer reviewers know what to expect.

Hint: the official documentation for Robot Framework, Playwright, and Cypress all contain their respective instructions for setting up a GitHub Actions workflow.

To test your workflows, create a private GitHub repository and copy the AUT repository contents into your private repository. This way your solution will not be visible to others. Do not use a public fork (or an otherwise public repository) for testing your GitHub Actions workflows!