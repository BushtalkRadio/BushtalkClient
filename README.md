# Bushtalk Radio

Bushtalk Radio is a community driven project with the aim to fill the empty world of MSFS2020 with thousands of additional landmarks and POIs. Each landmark has a unique audio tour that is automatically played on arrival. Think of it as having a virtual tour guide by your side.

We have audio tours for all in-game POIs (including Japan and USA update) as well as hundreds of community created content: national parks, forests, islands, active volcanoes, historical battles - there's something for everyone.

There are 3 components to Bushtalk Radio:

* **Bushtalk Radio [website](https://www.bushtalkradio.com)** - This is where our users upload landmarks and POIs. You will also need to have the website open for the audio tours to be played.

* **Bushtalk [client](https://bushtalkradioclient-dist.s3.amazonaws.com/BushtalkClient.zip)** - The client is needed to upload your airplane location to our server. This is what allows us to automatically play the audio tour based on your in-game location.

* **(OPTIONAL) Bushtalk World Landmarks Pack** - This addon allows you to see all of the custom POI markers in-game. This file will be uploaded monthly to include all of the landmarks and POIs submitted on the Bushtalk Radio website.


## How to use

While you can still use the website on mobile to track your flight, we recommend using the computer you'll be playing MSFS2020 on as the browser needs to be open for the audio tours to be played.

1. Make an account at https://www.bushtalkradio.com and log in
2. Download the "Bushtalk World Landmarks Pack" addon and install it to your community folder
3. Download the [Bushtalk Client](https://bushtalkradioclient-dist.s3.amazonaws.com/BushtalkClient.zip) and log in
4. Use our website or the in-game map to find an intresting POI to explore and spawn at the nearest airport
5. If you've logged in with the client, then you should see your plane being tracked on the website
6. Fly towards your destination, if you installed the "World Landmarks Pack" then you'll see the POI marker in-game and as you approach the audio tour will play automatically.

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



