# Saucedemo Playwright E2E Automation

![CI](https://github.com/ernestoalbarez/saucedemo-playwright-e2e/actions/workflows/ci.yml/badge.svg)

## Overview

This repository provides a **professional, enterprise-ready automation
framework** for building end-to-end tests using **Playwright with
Python**.

It demonstrates modern **SDET architecture patterns** including:

-   Page Object Model (POM)
-   Flow orchestration
-   Test fixtures
-   Static typing
-   CI integration
-   Professional reporting

The goal is to serve as both:

-   A **production-ready automation template**
-   A **reference architecture for scalable test automation frameworks**

------------------------------------------------------------------------

# Key Features

## Scalable Architecture

Clear separation between:

-   Tests
-   Page Objects
-   Locators
-   Configuration
-   Utilities

This allows large test suites to grow without becoming difficult to
maintain.

------------------------------------------------------------------------

## Advanced SDET Patterns

### Flow Pattern

Encapsulates complex user journeys into reusable flows.

Example:

``` python
checkout_flow.complete_purchase("sauce-labs-backpack")
```

This keeps tests short and business-oriented.

------------------------------------------------------------------------

### Fluent Page Objects

Page objects return themselves or the next page, enabling **method
chaining**.

Example:

``` python
login_page.open().login("standard_user", "secret_sauce")
```

------------------------------------------------------------------------

### Test DSL

Tests read closer to **business intent** than UI implementation.

Example:

``` python
inventory.add_to_cart("sauce-labs-backpack")
inventory.open_cart()
cart.checkout()
```

------------------------------------------------------------------------

## Professional Reporting

The framework integrates **Allure Reporting** providing:

-   Interactive reports
-   Step visualization
-   Screenshot attachments
-   Failure diagnostics

Screenshots are automatically captured when tests fail.

------------------------------------------------------------------------

## Static Type Safety

The project uses **mypy (strict mode)** to enforce static typing across
the entire codebase.

Benefits include:

-   Early error detection
-   Better IDE autocompletion
-   Improved maintainability

------------------------------------------------------------------------

## Code Quality Tooling

  Tool         Purpose
  ------------ -----------------------
  Ruff         Linting
  Black        Code formatting
  mypy         Static typing
  pre-commit   Local code validation

These tools run both locally and in CI.

------------------------------------------------------------------------

## CI/CD Integration

The repository includes **GitHub Actions** which automatically:

-   Installs dependencies
-   Runs linting and formatting
-   Executes type checking
-   Runs the full test suite
-   Publishes Allure artifacts

------------------------------------------------------------------------

# Project Structure

    .
    ├── .github/workflows/      # CI/CD pipelines
    ├── config/                 # Environment configuration
    │   ├── settings.py
    │   └── test_users.py
    │
    ├── locators/               # UI selectors
    │
    ├── pages/                  # Page Object implementations
    │   ├── base_page.py
    │   ├── login_page.py
    │   ├── inventory_page.py
    │   ├── cart_page.py
    │   ├── checkout_step_one_page.py
    │   ├── checkout_step_two_page.py
    │   └── checkout_complete_page.py
    │
    ├── tests/                  # Test suites
    │   ├── test_cart.py
    │   ├── test_checkout.py
    │   └── test_checkout_e2e_flow.py
    │
    ├── utils/                  # Browser utilities
    │
    ├── screenshots/            # Failure screenshots
    ├── allure-results/         # Allure raw results
    │
    ├── pytest.ini
    ├── pyproject.toml
    └── README.md

------------------------------------------------------------------------

# Getting Started

## Prerequisites

-   Python **3.11+**
-   Playwright browsers
-   Allure CLI

Install Allure on Ubuntu:

``` bash
sudo apt install allure
```

------------------------------------------------------------------------

# Installation

## Clone the repository

``` bash
git clone git@github.com:ernestoalbarez/saucedemo-playwright-e2e.git
cd saucedemo-playwright-e2e
```

------------------------------------------------------------------------

## Create virtual environment

Ubuntu / Linux:

``` bash
python3 -m venv .venv
source .venv/bin/activate
```

Windows:

``` bash
python -m venv .venv
.venv\Scripts\activate
```

------------------------------------------------------------------------

## Install dependencies

``` bash
pip install -r requirements-dev.txt
playwright install --with-deps
```

------------------------------------------------------------------------

## Install pre-commit hooks

``` bash
pre-commit install
```

------------------------------------------------------------------------

# Running Tests

## Run all tests

``` bash
pytest
```

------------------------------------------------------------------------

## Run with environment variable

``` bash
ENV=staging pytest
```

------------------------------------------------------------------------

## Run in a specific browser

``` bash
BROWSER=firefox pytest
```

Supported browsers:

-   chromium
-   firefox
-   webkit

------------------------------------------------------------------------

## Run a single test file

``` bash
pytest tests/test_checkout.py
```

------------------------------------------------------------------------

# Allure Reporting

Run tests to generate results:

``` bash
pytest
```

Results will appear in:

    allure-results/

------------------------------------------------------------------------

## Open interactive report

``` bash
allure serve allure-results
```

------------------------------------------------------------------------

## Generate static report

``` bash
allure generate allure-results --clean -o allure-report
```

------------------------------------------------------------------------

# Test Fixtures

Important fixtures:

  Fixture               Purpose
  --------------------- ---------------------------------
  browser               Launch browser once per session
  context               New browser context per test
  page                  Fresh Playwright page
  logged_in_inventory   Logged-in user fixture
  cart_page             Cart page object

Example:

``` python
def test_checkout(logged_in_inventory: InventoryPage):
    logged_in_inventory.add_to_cart("sauce-labs-backpack")
```

------------------------------------------------------------------------

# Configuration

Environment variables control framework behavior.

  Variable     Description      Default
  ------------ ---------------- ----------
  ENV          Environment      local
  BROWSER      Browser engine   chromium
  HEADLESS     Headless mode    true
  TIMEOUT_MS   Timeout          30000

Example:

``` bash
BROWSER=firefox HEADLESS=false pytest
```

------------------------------------------------------------------------

# Design Principles

### Typed Everything

All functions include type hints to reduce runtime errors.

### Locator Isolation

Selectors live in `locators/` to isolate UI changes.

### Test Simplicity

Tests express **business intent** rather than UI details.

### Clean Fixtures

Reusable fixtures reduce duplication.

### Deterministic Automation

Relies on Playwright auto-waiting instead of hard sleeps.

------------------------------------------------------------------------

# Future Improvements

Potential improvements:

-   Parallel execution with pytest-xdist
-   Visual regression testing
-   API testing integration
-   Playwright trace attachments
-   Test data factories

------------------------------------------------------------------------

# License

This project is licensed under the **MIT License**.
