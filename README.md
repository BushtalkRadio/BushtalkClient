# Bushtalk Radio

Bushtalk Radio is a [free website](https://www.bushtalkradio.com) that allows you to explore the world in Microsoft Flight Simulator 2020 with a virtual tour guide by your side.

The idea is simple: choose somewhere you'd like to visit on our [map](https://www.bushtalkradio.com), once you arrive at your destination an audio tour will automatically start playing about the area.

We have thousands of destinations for you to explore, each with an individual audio tour. We have all in-game POIs (including Japan and USA update) as well as hundreds of community created content: national parks, active volcanoes, historical battles - there's something for everyone.

Users can add custom locations and write their own audio tours. Just write an interesting, witty script and we'll create the audio tour for you. Not the creative type? Autogenerate one instead, we won't judge you.

## Features

* **Dynamic audio tours** - Fly anywhere in the world and an audio tour will automatically start playing upon your arrival

* **Track your flight** - Use our map on a browser or even on your phone to track your flight path

* **Audio Directions** - Get audio directions when you set a destination. This is great in VR as you won't have to keep looking at the map

* **Write your own tours** - Add custom locations and write your own audio tours. Write the script and we'll generate the audio for you


## How to use

While you can still use the website on mobile to track your flight, we recommend using your computer for the best experience. 

There are two ways to use Bushtalk Radio: with or without the Bushtalk Client.

### I want to use the client

Using the client allows you to track your in-game location. This will provide the best experience as the audio tours will play automatically upon arrival.

1. Make an account at https://www.bushtalkradio.com and log in
2. Download the [Bushtalk Client](https://bushtalkradioclient-dist.s3.amazonaws.com/BushtalkClient.zip) and log in
3. Browse the map and find a destination that interests you and note the nearest airport in the sidebar
4. Run Microsoft Flight Simulator and spawn at the airport, you should see your plane being tracked on the map
5. Fly towards your destination, upon your arrival the audio tour will play.

### I don't want to use the client

You can still use Bushtalk Radio without downloading the client but you won't be able track your flight on the map and the audio tour won't play automatically

1. Make an account at https://www.bushtalkradio.com and log in
3. Browse the map and find a destination that interests you and note the nearest airport, distance and the heading in the sidebar.
4. Spawn at the airport and fly towards your destination.
5. Once you've reached your destination, play the audio tour on the sidebar

## FAQ

### How long are the audio tours?

They are typically 1-3 minutes long depending on the landmark

### I have a feature request or bug to report

You can send me a message directly on [/u/bushtalkradio](https://www.reddit.com/user/bushtalkradio), email me at admin@bushtalkradio.com or through the feedback form on our webite via the '+' button.

### Windows is flagging the Bushtalk Client .exe/.zip file as a virus

Unfortunately that's the case whenever you try download a .exe file. You should be able to override and download anyway.

If you're not comfortable running a .exe file on your computer and you have Python installed, then you can follow the instructions below. That way you can personally be sure the script is not doing anything malicious. I understand not a lot a people want to mess around with python scripts which is why I packaged it into a .exe

1. Clone this repository: $ git clone https://github.com/BushtalkRadio/BushtalkClient.git
2. Run the client with python: $ python BushtalkClient.py

#### (OPTIONAL) How package python script into .exe

2. Install pyinstaller: $ pip install pyinstaller
3. Make sure SimConnect.dll is in the same directory as BushtalkClient.py
4. Create .exe with: $ pyinstaller -wF --add-data SimConnect.dll;. --icon=favicon.ico BushtalkClient.py



