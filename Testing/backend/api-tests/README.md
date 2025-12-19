# Running the API Tests

These tests check the Todo Lists API using Python and pytest.

The API must be running locally at:

```
http://localhost:4322/api
```

---

## Requirements

* Python 3.9+
* pip
* Running API server

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

### 2. Install dependencies

```bash
pip install pytest requests
```

---

## Test Files

The API test code is located in:

```
test_todo_lists.py
```

The following tests are covered:

* Create a new user for each test
* Get an access token
* Call the Todo List endpoints using that token

(7 different endpoints are being tested here.)

---

## Run the Tests

From the API tests root:

### Run all tests

```bash
pytest
```

### Run with more output

```bash
pytest -v
```

### Run one test file

```bash
pytest test_todo_lists.py
```

### Run a single test

```bash
pytest test_todo_lists.py::test_create_todo_list
```

---

## Notes

* The API must be running before starting the tests
* Each test creates its own data
* No database cleanup is required
* If a test fails:

  * Check that the backend URL is correct
  * Verify that the backend is reachable
  * Review test error outputs