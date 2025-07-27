# ✅ Test Documentation – Todo App QA Challenge

## 1. Introduction

This test documentation describes the test strategy used to validate the core functionality of a full-stack Todo application (React + Node.js). The test suite ensures that both the frontend and backend components behave as expected across critical user scenarios.

---

## 2. What is Being Tested

| Component | Test Focus |
|----------|------------|
| **UI (React)** | User login, form inputs, todo creation via interface |
| **API (Express)** | Login, GET/POST todos |
| **Integration** | Confirm UI actions trigger backend updates |

---

## 3. Test Coverage Areas

### ✅ UI Tests (Selenium + Pytest)
- Valid login test
- Invalid login scenario (error handling)
- Todo creation from UI
- UI feedback on successful submission

### ✅ API Tests (Postman + Newman)
- `POST /login` – User authentication with correct/incorrect credentials
- `POST /todos` – Creation of todo items
- `GET /todos` – Retrieval of user todos
- ⛔ `PUT /todos/:id` and `DELETE /todos/:id` – Not implemented in current app, marked as limitation

---

## 4. Tools Used

| Tool | Purpose | Reason |
|------|---------|--------|
| **Selenium (Python)** | UI test automation | Simulates real user behavior in browser |
| **Pytest** | Test runner for Selenium | Pythonic and concise |
| **Postman** | API test design | Visual creation + scripting |
| **Newman** | Postman CLI runner | Integrates easily with CI/CD |
| **dotenv** | Env var handling | Keeps credentials/configs secure and reusable |

---

## 5. How to Run the Tests

### 🔧 Prerequisites

Install required packages:
```bash
pip install -r tests/requirements.txt
```

Ensure `.env_test` file contains:
```env
URL=http://localhost:5173/login?redirect=%2Ftodo
VALID_EMAIL=john@example.com
VALID_PASSWORD=Password123
INVALID_EMAIL=wrong@example.com
INVALID_PASSWORD=WrongPass123
```

### 🧪 Run UI Tests (Selenium)

```bash
cd tests/selenium_tests
pytest
```

> Headless mode is used for CI/CD; no GUI needed.

### 📡 Run API Tests (Newman)

```bash
cd tests/api_tests
newman run todo-tests.postman_collection.json -e todo-env.postman_environment.json
```

---

## 6. Assumptions and Limitations

- The backend lacks support for PUT and DELETE routes; these are noted and excluded from test execution.
- No database reset between test runs; some tests may produce duplicate data or require manual cleanup.
- UI tests rely on specific element selectors; major UI refactors may require locator updates.

---

## 7. Directory Structure

```
project-root/
├── ...                  # React + Node app
├── tests/
│   ├── api_tests/
│   │   ├── todo-tests.postman_collection.json
│   │   └── todo-env.postman_environment.json
│   └── selenium_tests/
│       ├── tests/
│       │   ├── login_test.py
│       │   └── crud_test.py
│       └── utils/
│           └── base_test.py
|           └── .env_test
|           └── chromedriver.exe
├── todo_app_test_plan.md
└── requirements.txt
```

---

## 8. Brief Summary of My Approach

To provide thorough quality assurance, I applied a hybrid testing approach:

- UI tests validate user journeys in-browser using Selenium.
- API tests verify core backend endpoints with Postman + Newman.
- Tests are CI-ready, headless-compatible, and use `.env` variables for flexibility.

This ensures confidence in both system behavior and user experience.