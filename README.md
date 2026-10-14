# Playwright Python Test Automation – SauceDemo

!\[Playwright CI](https://github.com/<your-username>/playwright-saucedemo-automation/actions/workflows/ci.yml/badge.svg)

End-to-end UI test automation framework built with **Python**, **Playwright** and **pytest**,
tested against the public demo shop [saucedemo.com](https://www.saucedemo.com), with a
**GitHub Actions CI/CD pipeline**.

## Highlights

* **Page Object Model** for maintainable, reusable test code
* **Cross-browser** execution: Chromium, Firefox, WebKit (CI matrix)
* **Parametrized tests** and **pytest markers** (`smoke`, `regression`)
* **HTML report**, screenshots and Playwright **traces** on failure
* **CI/CD**: lint (Ruff) → tests on 3 browsers → artifacts; runs on push, PR, and nightly schedule

## Project structure

```
├── pages/                 # Page objects (login, inventory, cart, checkout)
├── tests/                 # Test suites + shared fixtures (conftest.py)
├── .github/workflows/     # CI pipeline
├── pytest.ini             # Config, markers, report options
└── requirements.txt
```

Test coverage
12 test scenarios run on Chromium, Firefox and WebKit in CI, giving 36 test executions in the Allure report.
---

|Area|Scenarios|
|-|-|
|Login|valid login, locked-out user, invalid credentials (parametrized), logout|
|Inventory|product count, price sorting (asc/desc), cart badge|
|Checkout|full purchase flow, form validation|

## Run locally

```bash
python -m venv .venv \&\& source .venv/bin/activate   # Windows: .venv\\Scripts\\activate
pip install -r requirements.txt
playwright install

pytest                          # all tests, headless Chromium
pytest -m smoke                 # smoke only
pytest --browser firefox        # other browser
pytest --headed --slowmo 500    # watch it run
```

Report: `reports/report.html`. View a failure trace with
`playwright show-trace test-results/<test>/trace.zip`.

## CI/CD pipeline

Defined in `.github/workflows/ci.yml`:

1. **Lint** – Ruff static analysis
2. **Test** – matrix over Chromium / Firefox / WebKit
3. **Artifacts** – HTML report always; traces \& screenshots on failure

