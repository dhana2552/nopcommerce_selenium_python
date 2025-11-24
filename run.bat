@echo off
cd %WORKSPACE%

echo Installing dependencies...
"C:\Users\Dhanalakshmi Scal\AppData\Local\Microsoft\WindowsApps\python.exe" -m pip install pytest
"C:\Users\Dhanalakshmi Scal\AppData\Local\Microsoft\WindowsApps\python.exe" -m pip install selenium
"C:\Users\Dhanalakshmi Scal\AppData\Local\Microsoft\WindowsApps\python.exe" -m pip install undetected_chromedriver
"C:\Users\Dhanalakshmi Scal\AppData\Local\Microsoft\WindowsApps\python.exe" -m pytest -v -s .\test_cases\