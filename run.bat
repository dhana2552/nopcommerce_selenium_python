@echo off
cd %WORKSPACE%

echo Installing dependencies...
D:\py311\python.exe -m pip install pytest
D:\py311\python.exe -m pip install selenium
D:\py311\python.exe -m pip install undetected_chromedriver
D:\py311\python.exe -m pytest -v -s .\test_cases\