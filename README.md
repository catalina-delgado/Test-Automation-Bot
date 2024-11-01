# TECNICAL - TEST - FLYR

## Folders

- **Test Automation** This folder contains files for test cases structured using POM logic.

## Files

 - **foo_bar.py** solution to problem: "Foo Bar".
 - **happy_number.py** solution to problem: happy number validation.
 
## Requirements
This repository requires the following libraries and frameworks:

- Selenium
- pytest
- allure
- numPy 
- Time

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

After installing all the Requirements, you must clone the repository using.
```
git clone https://github.com/catalina-delgado/TECNICAL-TEST.git
```
Enter the cloned folder, then enter the "Test_Automation" folder and run the test cases using.

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
