# Playwright Automation Framework: E2E UI Testing

This repository contains a production-grade UI automation framework built with Python and Playwright. It demonstrates scalable testing architecture designed to handle complex system interactions, validate operational reliability, and provide deep observability in CI/CD environments.

## 🏗️ Architecture Highlights

*   **Page Object Model (POM):** UI interactions are strictly separated from test assertions to ensure the codebase remains maintainable and resilient to frontend changes.
*   **Authentication State Bypass:** Leverages Playwright's browser context to capture and inject session state (`storage_state`), bypassing repetitive login flows and reducing test execution time.
*   **Secret Management:** Environment variables are strictly managed via `python-dotenv` locally and GitHub Secrets in CI/CD, ensuring zero credentials are leaked into version control.
*   **Network Fault Injection:** Utilizes Playwright's network interception (`page.route`) to simulate backend/CDN outages (e.g., forcing 500 Internal Server Errors) to validate frontend fault tolerance.
*   **Data-Driven Testing:** Uses `pytest.mark.parametrize` to rigorously validate multiple edge cases and error states within a single, DRY test function.
*   **Hermetic Execution:** Browsers and dependencies are strictly sandboxed within a virtual environment, eliminating global-state conflicts and mimicking isolated container constraints.

## 🚀 CI/CD & Observability

This framework is fully integrated with **GitHub Actions** for continuous integration.

*   **Automated Execution:** Tests run automatically on an Ubuntu Linux runner for every push and pull request to the `main` branch.
*   **HTML Reporting:** Automatically generates and attaches a standalone `pytest-html` dashboard as a downloadable artifact for every pipeline run.
*   **Trace Generation:** If a test fails in the cloud, Playwright Trace Viewer artifacts (containing DOM snapshots, network requests, and console logs) are automatically captured and uploaded for offline debugging.

## 🛠️ Tech Stack

*   **Language:** Python 3
*   **Framework:** Pytest
*   **Automation Engine:** Playwright Sync API
*   **Reporting:** pytest-html

## 💻 Quick Start Setup

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/yourusername/playwright-e2e-framework.git](https://github.com/yourusername/playwright-e2e-framework.git)
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
    source venv/bin/activate  # On Windows use: .\venv\Scripts\activate
    ```

4.  **Install dependencies and isolated browsers:**
    ```bash
    pip install pytest pytest-playwright pytest-html python-dotenv
    
    # Windows CMD users run this first to ensure local installation:
    # set PLAYWRIGHT_BROWSERS_PATH=0
    playwright install
    ```

5.  **Run the test suite with Reporting and Traces:**
    ```bash
    pytest --html=report.html --self-contained-html --tracing=retain-on-failure
    ```
