# Hospital Management System - Test Automation Suite

## Overview

A comprehensive Playwright-based test automation framework designed to validate the functionality of a hospital management system. This project implements the Page Object Model (POM) design pattern to ensure maintainability, scalability, and code reusability. The test suite covers critical workflows including user authentication, dashboard navigation, and patient management operations.

**Application Under Test:** https://qahackeru3.netlify.app/

## Tech Stack

- **Language:** Python 3.8+
- **Test Framework:** Pytest
- **Browser Automation:** Playwright (Sync API)
- **Design Pattern:** Page Object Model (POM)
- **Test Type:** Smoke/E2E Testing

## Project Structure

```
playwright-project/
├── conftest.py                  # Pytest configuration and shared fixtures
├── pages/                       # Page Object Model classes
│   ├── __init__.py
│   ├── a_login_page.py         # Login page interactions
│   ├── b_dashboard_page.py     # Dashboard page interactions
│   └── c_add_patient_page.py   # Patient management interactions
├── tests/                       # Test files
│   └── smoke_test.py           # Smoke test suite
├── .gitignore                   # Git ignore rules
└── README.md                    # This file
```

## Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager
- Git

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd playwright-project
   ```

2. **Create a virtual environment**
   ```bash
   # On Windows
   python -m venv venv
   venv\Scripts\activate

   # On macOS/Linux
   python -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install playwright pytest
   ```

4. **Install Playwright browsers**
   ```bash
   playwright install
   ```

## Running Tests

### Run All Tests
```bash
pytest tests/
```

### Run Specific Test File
```bash
pytest tests/smoke_test.py
```

### Run Specific Test Case
```bash
pytest tests/smoke_test.py::test_smoke
```

### Run Tests with Verbose Output
```bash
pytest -v tests/
```

### Run Tests with Detailed Output and Logging
```bash
pytest -vv -s tests/
```

### Run Tests in Parallel (requires pytest-xdist)
```bash
pip install pytest-xdist
pytest -n auto tests/
```

## Test Coverage

### Smoke Test Suite (`smoke_test.py`)

The smoke test validates end-to-end workflows:

1. **test_smoke** - Full workflow test
   - User authentication with credentials (staff_id: `nurse_admin`, password: `clinical2026`)
   - Dashboard tab navigation (Patients, Laboratory, Pharmacy)
   - Patient addition workflow
   - Patient data entry and search functionality

2. **test_visual_url** - URL validation test
   - Verifies the application URL is accessible

3. **test_logout_btn** - UI element visibility test
   - Confirms logout button is visible on the page

4. **patient_text** - Data container validation test
   - Validates patient data is present in the data container

## Page Object Model

The project follows the Page Object Model pattern for maintainability and reusability:

### LoginPage (`a_login_page.py`)
- **Purpose:** Encapsulates login page interactions
- **Key Methods:**
  - `login(staff_id, password)` - Authenticates user with credentials

### DashboardPage (`b_dashboard_page.py`)
- **Purpose:** Manages dashboard page interactions
- **Key Methods:**
  - `click_all_tabs()` - Navigates through all dashboard tabs
  - `add_patient()` - Initiates patient addition workflow

### AddPatientPage (`c_add_patient_page.py`)
- **Purpose:** Handles patient management operations
- **Key Methods:**
  - `fill_patient_details(patient_id, patient_name, category, status, assigned_doctor, Ward)` - Fills patient form with details
  - `search_patient(patient_id)` - Searches for a patient by ID

## Environment Configuration

### Fixtures (conftest.py)

The `conftest.py` file provides shared pytest fixtures:

- **hospital_url** - Initializes browser, navigates to the application, and returns the page object for use in tests

```python
@pytest.fixture
def hospital_url(page):
    page.goto("https://qahackeru3.netlify.app/")
    return page
```

## Test Credentials

- **Staff ID:** `nurse_admin`
- **Password:** `clinical2026`
- **Role:** Nurse Admin

*Note: These credentials are for testing purposes only.*

## Development Notes

### Best Practices Implemented

- **Page Object Model:** Separation of test logic from page interactions
- **Fixture-Based Setup:** Shared configuration via pytest fixtures
- **Clear Naming:** Descriptive page and method names for readability
- **Locator Strategy:** XPath and CSS selectors for robust element identification

### Future Enhancements

- Add explicit waits and error handling
- Implement custom exceptions for better error reporting
- Add test data parameterization
- Integrate with CI/CD pipeline
- Add screenshot/video capture on failures
- Generate HTML test reports

## Troubleshooting

### Playwright Browsers Not Found
```bash
playwright install
```

### Import Errors
Ensure your virtual environment is activated and dependencies are installed:
```bash
pip install -r requirements.txt
```

### Element Not Found Errors
- Check if the application is running at the correct URL
- Verify CSS selectors/XPath expressions match current application structure
- Use `page.pause()` in tests to debug locator issues interactively

## CI/CD Integration

This project can be integrated with CI/CD pipelines (GitHub Actions, GitLab CI, Jenkins, etc.):

```yaml
# Example: GitHub Actions
- name: Install Playwright
  run: playwright install

- name: Run Tests
  run: pytest tests/
```

## Contributing

1. Follow the Page Object Model pattern for new pages
2. Use descriptive naming conventions
3. Add appropriate waits and error handling
4. Update this README for significant changes
5. Maintain test independence - tests should not depend on execution order

## License

[Add your license information here]

## Contact

[Add contact information if needed]
