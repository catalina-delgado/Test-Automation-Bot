# TEST-AUTOMATION Bot

## Requirements
This repository requires the following libraries and frameworks:

- Selenium
- pytest
- allure

This repository was developed in the Python3 (3.13) programming language.

## Package installation

Install Python packages within virtual enviroment. To create, execute the command below:
```
python3.13 -m venv env
```
So, activate it
```
pip .env/scripts/activate
```
Now, install the libraries.

## Browsers

Run testing in browsers version below:

- Chrome - 130.0.6723.59 (64 bits)
- FireFox - 131.0.3 (64 bits)

## Execution

for run in chrome browser
```
pytest --browser=chrome tests/
```
for run in firefox browser
```
pytest --browser=firefox tests/
```
## Note 
Before running the test cases, please verify that the file paths are correct.
