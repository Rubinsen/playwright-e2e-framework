# Playwright Automation Framework: E2E UI Testing

This repository contains a production-grade UI automation framework built with Python and Playwright. It demonstrates scalable testing architecture designed to handle complex system interactions and validate operational reliability.

## 🏗️ Architecture Highlights

*   **Page Object Model (POM):** UI interactions are strictly separated from test assertions to ensure the codebase remains maintainable and resilient to frontend changes.
*   **Authentication State Bypass:** Leverages Playwright's browser context to capture and inject session state (`storage_state`), bypassing repetitive login flows and reducing test execution time by up to 60%.
*   **Data-Driven Testing:** Utilizes `pytest.mark.parametrize` to rigorously validate multiple edge cases and error states within a single, DRY test function.
*   **Hermetic Execution:** Browsers and dependencies are strictly sandboxed within a virtual environment, mimicking isolated CI/CD constraints.

## 🛠️ Tech Stack

*   **Language:** Python 3
*   **Framework:** Pytest
*   **Automation Engine:** Playwright Sync API

## 🚀 Quick Start Setup

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/rubinsen/playwright-e2e-framework.git](https://github.com/rubinsen/playwright-e2e-framework.git)
    cd mobileye_automation
    ```
2.  **Create and activate the virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use: .\venv\Scripts\activate
    ```
3.  **Install dependencies and isolated browsers:**
    ```bash
    pip install pytest-playwright
    playwright install
    ```
4.  **Run the test suite:**
    ```bash
    pytest --headed
    ```