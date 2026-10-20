<h1 align="center">Playwright Python Test Automation</h1>

<p align="center">
  End-to-end UI test automation framework for the <a href="https://www.saucedemo.com">SauceDemo</a> web shop,<br>
  with cross-browser execution, a CI/CD pipeline and a live Allure report.
</p>

<p align="center">
  <a href="https://github.com/divesh-sys/playwright-saucedemo-automation/actions/workflows/ci.yml"><img src="https://github.com/divesh-sys/playwright-saucedemo-automation/actions/workflows/ci.yml/badge.svg" alt="CI/CD status"></a>
  <img src="https://img.shields.io/badge/Python-3.12-3776AB?logo=python&logoColor=white" alt="Python 3.12">
  <img src="https://img.shields.io/badge/Playwright-UI%20testing-45ba4b?logo=playwright&logoColor=white" alt="Playwright">
  <img src="https://img.shields.io/badge/pytest-8.x-0A9EDC?logo=pytest&logoColor=white" alt="pytest">
  <img src="https://img.shields.io/badge/Allure-report-orange" alt="Allure report">
</p>

<p align="center">
  <a href="https://divesh-sys.github.io/playwright-saucedemo-automation/"><b>Live Allure report</b></a> ·
  <a href="https://github.com/divesh-sys/playwright-saucedemo-automation/actions"><b>CI/CD runs</b></a> ·
  <a href="#demo"><b>Demo video</b></a>
</p>

---

## About the project

This project automates the main user journeys of a demo e-commerce site: logging in, browsing and sorting products, managing the cart and completing a purchase. It is built the way a real test automation framework is structured, with reusable page objects, shared fixtures, parametrized data, cross-browser runs and an automated pipeline that publishes the results.

## Highlights

- **Page Object Model** for maintainable, reusable test code
- **Cross-browser testing** on Chromium, Firefox and WebKit
- **14 automated tests** (42 executions across 3 browsers) with `smoke` and `regression` markers
- **Parametrized tests** to cover several data sets with one test function
- **Reporting:** Allure dashboard, pytest HTML report, screenshots and Playwright traces on failure
- **CI/CD with GitHub Actions:** lint, parallel browser matrix, automatic report publishing to GitHub Pages
- **Video recording** of headed runs through a manual workflow

## Tech stack

| Purpose | Tool |
|---|---|
| Language | Python 3.12 |
| Browser automation | Playwright |
| Test runner | pytest, pytest-playwright |
| Reporting | Allure, pytest-html |
| Code quality | Ruff |
| CI/CD | GitHub Actions, GitHub Pages |

## Demo

https://github.com/user-attachments/assets/21d75cc0-65f2-409a-ab51-3b5524907412

### Allure report

<img width="1920" height="871" alt="Allure report dashboard" src="https://github.com/user-attachments/assets/d459e400-7ee3-4a34-9fbb-96780df20e60" />

## CI/CD pipeline

The pipeline is defined in [`.github/workflows/ci.yml`](.github/workflows/ci.yml). It runs on every push and pull request to `main`, every weekday morning, and on demand.

```mermaid
flowchart LR
    A[git push] --> B[GitHub Actions]
    B --> C[Lint with Ruff]
    C --> D1[Tests: Chromium]
    C --> D2[Tests: Firefox]
    C --> D3[Tests: WebKit]
    D1 --> E[Allure report]
    D2 --> E
    D3 --> E
    E --> F[GitHub Pages]
```

| Stage | What happens |
|---|---|
| Lint | Ruff checks code style, and the pipeline stops if it fails |
| Test | The suite runs in parallel on Chromium, Firefox and WebKit |
| Artifacts | HTML reports are always saved, traces and screenshots are saved on failure |
| Report | Results from all browsers are merged into one Allure report and published to GitHub Pages |

A second workflow, `headed-video.yml`, runs the tests in headed mode on a virtual display and records a video of every test. It is started manually from the Actions tab.

## Test coverage

| Area | Scenarios |
|---|---|
| Login | valid login, locked-out user, invalid credentials (3 parametrized cases), logout |
| Inventory | product count, price sorting low to high and high to low, cart badge updates |
| Cart | remove an item from the cart, open a product details page |
| Checkout | full end-to-end purchase, required field validation |

## Project structure

```
playwright-saucedemo-automation/
├── pages/                  # Page objects (login, inventory, cart, checkout)
├── tests/                  # Test suites and shared fixtures (conftest.py)
├── .github/workflows/
│   ├── ci.yml              # Lint, cross-browser tests, Allure report to GitHub Pages
│   └── headed-video.yml    # Manual headed run with video recording
├── pytest.ini              # Configuration, markers, report options
└── requirements.txt
```

## Run it locally

**Requirements:** Python 3.12 and Git.

```bash
# 1. Clone the repository
git clone https://github.com/divesh-sys/playwright-saucedemo-automation.git
cd playwright-saucedemo-automation

# 2. Create and activate a virtual environment
python -m venv .venv
.venv\Scripts\activate          # Windows
# source .venv/bin/activate     # Mac / Linux

# 3. Install dependencies and browsers
pip install -r requirements.txt
playwright install
```

### Useful commands

| Goal | Command |
|---|---|
| Run all tests | `pytest` |
| Smoke tests only | `pytest -m smoke` |
| Regression tests only | `pytest -m regression` |
| Use another browser | `pytest --browser firefox` |
| Watch the browser | `pytest --headed --slowmo 700` |
| Record videos | `pytest --video on` |
| Save traces for every test | `pytest --tracing on` |

### Reports

- **pytest HTML report:** open `reports/report.html`
- **Playwright trace viewer:** `playwright show-trace test-results/<test-folder>/trace.zip`
- **Allure dashboard:** run `allure serve allure-results` (requires the Allure command-line tool)

## Author

**Divesh Jadhav** · [GitHub: divesh-sys](https://github.com/divesh-sys)

If you find this project useful, a star on the repo is appreciated.# Playwright Python Test Automation – SauceDemo

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
12 test scenarios run on Chromium, Firefox and WebKit in CI, giving 42 test executions in the Allure report.
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

