# Automated Testing for SauceDemo

This project demonstrates automated testing for the [SauceDemo](https://www.saucedemo.com/) website using Python, Pytest, and Selenium.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
  - [Clone the Repository](#clone-the-repository)
  - [Set Up a Virtual Environment](#set-up-a-virtual-environment)
  - [Install Dependencies](#install-dependencies)
- [Running Tests](#running-tests)
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

### GitHub Actions Workflow
This repository is configured with a GitHub Actions workflow for automated testing. The workflow runs tests whenever changes are pushed to the main branch.

For more details, check the GitHub Actions Workflow configuration.
