# Automated Testing for SauceDemo

This project demonstrates automated testing for the [SauceDemo](https://www.saucedemo.com/) website using Python, Pytest, and Selenium.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
  - [Clone the Repository](#clone-the-repository)
  - [Set Up a Virtual Environment](#set-up-a-virtual-environment)
  - [Install Dependencies](#install-dependencies)
- [Running Tests](#running-tests)
- [Testing Framework](#testing-framework)
- [GitHub Actions Workflow](#github-actions-workflow)

## Prerequisites

Before you begin, ensure you have met the following requirements:
- Python 3.x installed on your system
- GitHub account (for using GitHub Actions)

## Getting Started

### Clone the Repository

git clone https://github.com/yourusername/saucedemo-automation.git
cd saucedemo-automation

### Set Up a Virtual Environment

python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate

### Install Dependencies
pip install -r requirements.txt
### Running Tests
You can run the tests using Pytest:
pytest

## Testing Framework
### Framework Overview
This project utilizes a testing framework based on the following technologies:

Pytest: A testing framework that makes it easy to write simple and scalable test cases.
Selenium: A powerful tool for controlling a web browser through the program.
Page Object Model (POM): A design pattern for creating well-structured test automation frameworks by encapsulating web page elements and their interactions in separate classes.
Page Object Model (POM)
The Page Object Model (POM) design pattern is used to create a structured and maintainable test automation framework. It encapsulates the web page elements and interactions in separate Python classes, making the code easy to understand and maintain.

In this project, you'll find POM classes for the login page, product page, and cart page, making it straightforward to interact with elements on these pages.

## Pytest Features
Test Parameterization: Test scenarios are parameterized using Pytest fixtures, allowing for reusable and data-driven tests.

Explicit Waits: Explicit waits are implemented to ensure that the page loads and elements become visible and interactable before test actions are performed.

Error Handling: Exception handling is implemented to gracefully handle errors and avoid abrupt test failures.

Comprehensive Reporting: The project is configured to provide comprehensive test reports using Pytest reporting features, including the generation of JUnit XML reports.

### GitHub Actions Workflow
This repository is configured with a GitHub Actions workflow for automated testing. The workflow runs tests whenever changes are pushed to the main branch.

For more details, check the GitHub Actions Workflow configuration.
