# Bushtalk Radio

Bushtalk Radio is a [free website](https://www.bushtalkradio.com) that allows you to explore the world in Microsoft Flight Simulator 2020 with a virtual tour guide by your side.

The idea is simple: choose somewhere you'd like to visit on our [map](https://www.bushtalkradio.com), once you arrive at your destination an audio tour will automatically start playing about the area.

We have 1201 destinations for you to explore, each with an individual audio tour. We have all in-game POIs (including Japan and USA update) as well as famous landmarks around the world such as mountains, lakes and National Parks.

## Features

* **Dynamic audio tours** - Fly anywhere in the world and an audio tour will automatically start playing if you're close enough

* **1201 Landmarks and POIs** - We also have all in-game airports on our map to help you plan your bush trip

* **Track your flight** - Use our map on a browser or even on your phone to track your flight path

* **Audio Directions** - Get audio directions when you set a destination. This is great in VR as you won't have to keep looking at the map

## How to use

1. Make an account at https://www.bushtalkradio.com and log in
2. Download the [Bushtalk Client](https://bushtalkradioclient-dist.s3.amazonaws.com/BushtalkClient.zip) and log in with the account made above
3. Run Microsoft Flight Simulator
4. You should see your airplane being tracked on our map.
5. Explore the world!

## FAQ

### How long are the audio tours?

They are typically 1-3 minutes long depending on the landmark

### I have a feature request or bug to report

You can send me a message directly on [/u/bushtalkradio](https://www.reddit.com/user/bushtalkradio) or through the feedback form on our webite via the '+' button.

### Windows is flagging the Bushtalk Client .exe/.zip file as a virus

Unfortunately that's the case whenever you try download a .exe file. You should be able to override and download anyway.

If you're not comfortable running a .exe file on your computer and you have Python installed, then you can follow the instructions below. That way you can personally be sure the script is not doing anything malicious. I understand not a lot a people want to mess around with python scripts which is why I packaged it into a .exe

1. Clone this repository: $ git clone https://github.com/BushtalkRadio/BushtalkClient.git
2. Run the client with python: $ python BushtalkClient.py

#### (OPTIONAL) How package python script into .exe

2. Install pyinstaller: $ pip install pyinstaller
3. Make sure SimConnect.dll is in the same directory as BushtalkClient.py
4. Create .exe with: $ pyinstaller -wF --add-data SimConnect.dll;. --icon=favicon.ico BushtalkClient.py



