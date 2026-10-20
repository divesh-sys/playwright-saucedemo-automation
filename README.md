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
|Checkout|<br />full purchase flow, form validation|
|cart |remove item from cart |
|Product|open product details page|

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
<img width="1920" height="871" alt="Screenshot 2026-10-20 154950" src="https://github.com/user-attachments/assets/d459e400-7ee3-4a34-9fbb-96780df20e60" />


## CI/CD pipeline

## demo video [video.webm](https://github.com/user-attachments/assets/21d75cc0-65f2-409a-ab51-3b5524907412)


Defined in `.github/workflows/ci.yml`:

1. **Lint** – Ruff static analysis
2. **Test** – matrix over Chromium / Firefox / WebKit
3. **Artifacts** – HTML report always; traces \& screenshots on failure

