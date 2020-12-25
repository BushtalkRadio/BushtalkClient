# Bushtalk Radio

Bushtalk Radio is a free website that allows you to explore the world in Microsoft Flight Simulator 2020 with an audio guide by your side.

The idea is simple: choose somewhere you’d like to explore, fly there and our audio guide will start talking about the area you’re in. 

## Features

* Dynamic audio tours which automatically trigger as you approach the landmark

* A map with over 1000 landmarks and all in-game airports and radio towers for you to plan your bush trips

* Track your flight on a map from your computer or phone and keep track of which landmarks you’ve already visited

* Get audio directions when you set a destination. This is great in VR as you won't have to keep looking at the map

## How to connect to Bushtalk Radio

1. Make an account at https://www.bushtalkradio.com and log in
2. Download the [Bushtalk Client](https://bushtalkradioclient-dist.s3.amazonaws.com/BushtalkClient.zip) and log in with the account made above
3. Run Microsoft Flight Simulator
4. You should see your airplane being tracked on our map.
5. Explore the world! You might learn something new!

## The Bushtalk Client .zip/.exe file is being flagged as virus

Unfortunately that's the case whenever you try download a .exe file. You should be able to override and download anyway.

If you're not comfortable running a .exe file on your computer and you have Python installed, then you can follow the instructions below. That way you can personally be sure the script is not doing anything malicious. I understand not a lot a people want to mess around with python scripts which is why I packaged it into a .exe

1. Clone this repository: $ git clone https://github.com/BushtalkRadio/BushtalkClient.git
2. Run the client with python: $ python BushtalkClient.py

### (OPTIONAL) How package python script into .exe

2. Install pyinstaller: $ pip install pyinstaller
3. Make sure SimConnect.dll is in the same directory as BushtalkClient.py
4. Create .exe with: $ pyinstaller -wF --add-data SimConnect.dll;. --icon=favicon.ico BushtalkClient.py



