@echo off
cd %WORKSPACE%

echo Installing dependencies...
D:\Software\python.exe -m pip install pytest
D:\Software\python.exe -m pip install selenium
D:\Software\python.exe -m pytest -v -s .\test_cases\