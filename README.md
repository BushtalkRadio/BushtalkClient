# Bushtalk Client

## How to package client into .exe

1. Make sure script runs correctly from commandline i.e. $ python script.py
2. Install pyinstaller: $ pip install pyinstaller
3. Make sure SimConnect.dll is in the same directory as BushtalkClient.py
4. Create .exe with: $ pyinstaller -wF --add-data SimConnect.dll;. --icon=favicon.ico BushtalkClient.py