# Playwright Automation Framework: E2E UI Testing

This repository contains a production-grade UI automation framework built with Python and Playwright. It demonstrates scalable testing architecture designed to handle complex system interactions, validate operational reliability, and provide deep observability in CI/CD environments.

## 🏗️ Architecture Highlights

*   **Hybrid State Seeding:** Bypasses standard UI flows via direct memory/localStorage injection to instantly seed application state, drastically reducing test execution time and flakiness.
*   **Parallel Execution:** Leverages `pytest-xdist` to distribute test execution across multiple CPU cores, optimizing compute resources for massive scalability.
*   **Code Quality Enforcement:** Integrated Git `pre-commit` hooks and the `Ruff` linter act as localized gatekeepers, enforcing strict formatting and static analysis standards before any code reaches version control.
*   **Page Object Model (POM):** UI interactions are strictly separated from test assertions to ensure the codebase remains maintainable and resilient to frontend changes.
*   **Authentication State Bypass:** Leverages Playwright's browser context to capture and inject session state (`storage_state`), bypassing repetitive login flows.
*   **Secret Management:** Environment variables are strictly managed via `python-dotenv` locally and GitHub Secrets in CI/CD.
*   **Network Fault Injection:** Utilizes Playwright's network interception (`page.route`) to simulate backend/CDN outages to validate frontend fault tolerance.

## 🚀 CI/CD & Observability

This framework is fully integrated with **GitHub Actions** for continuous integration.

*   **Automated Concurrent Execution:** Tests run automatically in parallel on an Ubuntu Linux runner for every push to the `main` branch.
*   **HTML Reporting:** Automatically generates and attaches a standalone `pytest-html` dashboard as a downloadable artifact.
*   **Trace Generation:** If a test fails in the cloud, Playwright Trace Viewer artifacts (containing DOM snapshots, network requests, and console logs) are automatically captured and uploaded for offline debugging.

## 🛠️ Tech Stack

*   **Language:** Python 3
*   **Framework:** Pytest
*   **Automation Engine:** Playwright Sync API
*   **Concurrency:** pytest-xdist
*   **Linting:** Ruff & pre-commit

## 💻 Quick Start Setup

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/rubinsen/playwright-e2e-framework.git](https://github.com/rubinsen/playwright-e2e-framework.git)
    cd playwright-e2e-framework
    ```

2.  **Set up Secure Credentials:**
    Create a `.env` file in the root directory and add the following dummy credentials:
    ```text
    VALID_USERNAME=standard_user
    VALID_PASSWORD=secret_sauce
    ```

3.  **Create and activate the virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # Windows: .\venv\Scripts\activate
    ```

4.  **Install dependencies and isolated browsers:**
    ```bash
    pip install pytest pytest-playwright pytest-html python-dotenv pytest-xdist pre-commit ruff
    
    # Windows CMD users run this first to ensure local installation:
    # set PLAYWRIGHT_BROWSERS_PATH=0
    playwright install
    ```

5.  **Install the Git Hooks:**
    ```bash
    pre-commit install
    ```

6.  **Run the test suite concurrently with Reporting and Traces:**
    ```bash
    pytest -n auto --html=report.html --self-contained-html --tracing=retain-on-failure
    ```