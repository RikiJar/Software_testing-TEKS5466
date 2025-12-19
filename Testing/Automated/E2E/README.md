# Running the E2E Tests (Playwright)

These tests verify the Todo Manager frontend using **Playwright** and **pytest**.
They simulate real user behavior in the browser, including registration, login, logout, and todo list management.

The frontend application must be running locally at:

```
http://localhost
```

---

## Requirements

* Python 3.9+
* pip
* Node.js (required by Playwright)
* Running frontend application
* Running backend/API (used by the frontend)

---

## Setup

### 1. Create a virtual environment (optional)

```bash
python -m venv venv
```

Activate it:

**Linux / macOS**

```bash
source venv/bin/activate
```

**Windows**

```bash
venv\Scripts\activate
```

---

### 2. Install Python dependencies

```bash
pip install pytest playwright
```

---

### 3. Install Playwright browsers

Playwright requires browser binaries to be installed separately.

```bash
playwright install
```

This will install Chromium, Firefox, and WebKit.

---

## Test Files

The E2E test code is located in:

```
test_user_functionalibities.py
```

The following scenarios are covered:

* User registration
* User login and logout
* Creating a new todo list
* Deleting a todo list

Each test uses **randomized usernames and passwords** to ensure:

* No shared state between test runs
* No need for database cleanup
* Compatibility with systems that do not support user deletion

---

## Run the Tests

From the E2E tests root:

### Run all E2E tests

```bash
pytest
```

---

### Run with more verbose output

```bash
pytest -v
```

---

### Run a specific test file

```bash
pytest test_user_functionalibities.py
```

---

### Run a single test

```bash
pytest test_user_functionalibities.py::test_register
```

---

### Run tests in headed mode (see the browser)

```bash
pytest --headed
```

---

### Slow down execution for debugging

```bash
pytest --headed --slowmo 500
```

---

## Notes

* The frontend must be running before starting the tests
* The backend/API must also be running
* Tests generate unique users and todo lists automatically
* No database cleanup is required
* If a test fails:

  * Check that the frontend URL is correct
  * Verify that the backend is reachable
  * Review Playwright error output and screenshots (if enabled)

---

## Optional: Debugging Tips

* Use `page.pause()` inside a test to open Playwright Inspector
* Run tests with `--headed` to visually follow each step
* Ensure selectors remain stable when UI changes