# Bushtalk Radio

Bushtalk Radio is a community driven project with the aim to fill the world of MSFS with thousands of interesting landmarks and POIs. Each landmark has a unique audio tour that is automatically played based on your in-game location.

We have audio tours for all in-game POIs (including Japan and USA update) as well as hundreds of community created content with more being added every day: national parks, forests, islands, active volcanoes, historical battles - there's something for everyone.

Users can add custom locations and write their own audio tours. Just write an interesting, witty script and we'll create the audio tour for you. Not the creative type? Autogenerate one with our Wikipedia Import tool, we won't judge you. We want to introduce players to amazing locations around the world. Add them as part of your next bush trip or fly aimlessly and stumble into something special.

There are 3 components to Bushtalk Radio:

* **[Bushtalk Radio website](https://www.bushtalkradio.com)** - This is where our users upload landmarks and POIs. Once you connect, the audio will be played through the browser so make sure to keep this open.

* **[Bushtalk client](https://bushtalkradioclient-dist.s3.amazonaws.com/BushtalkClient.zip)** - The client is needed to upload your airplane location to our server. This is what allows us to automatically play the audio tour based on your in-game location. Windows may flag it as a virus but this is a false positive. See FAQ below for more information for peace of mind

* **[Bushtalk World Landmarks Pack](https://flightsim.to/file/7285/bushtalk-radio-world-landmarks-pack)** (OPTIONAL) - This addon allows you to see all of the custom POI markers in-game. This file will be updated monthly to include all of the landmarks and POIs submitted on the Bushtalk Radio website.

Here are some of the best Bushtalk Radio has to offer:

1. [Second Punic War: Battle of Cannae ](https://bushtalkradio.com/?landmark=1437) - part of a 11-part audio tour covering the Second Punic War
2. [World's Largest Beaver Dam ](https://bushtalkradio.com/?landmark=1426) - a dam so big that can be seen from space
3. [Sinking of the Titanic](https://bushtalkradio.com/?landmark=1425) - a tragic loss of life in the middle of the Atlantic
4. [Fordlândia](https://bushtalkradio.com/?landmark=1220) - a failed experiment deep in the Amazon
5. [Galápagos Islands](https://bushtalkradio.com/?landmark=1397) - Many islands and volcanoes in close proximity. Find out what makes this place so unique.
6. [Flevoland](https://bushtalkradio.com/?landmark=1591) - If god built the world, then the Dutch built the Netherlands. Find out why

## How to use

While you can still use the website on mobile to track your flight, we recommend using the computer you'll be playing MSFS2020 on as the browser needs to be open for the audio tours to be played.

1. Make an account at https://www.bushtalkradio.com and log in
2. Download the [Bushtalk World Landmarks Pack](https://flightsim.to/file/7285/bushtalk-radio-world-landmarks-pack) and install it to your community folder
3. Download the [Bushtalk Client](https://bushtalkradioclient-dist.s3.amazonaws.com/BushtalkClient.zip) and log in
4. Spawn at a suitable airport near to the landmark you wish to explore
5. If you've logged in with the client, then you should see your plane being tracked on the website
6. Fly towards your destination, if you installed the "World Landmarks Pack" then you'll see the POI marker in-game and as you approach the audio tour will play automatically.

### I don't want to use the client

You can still use Bushtalk Radio without downloading the client but you won't be able track your flight on our map and the audio tour won't play automatically - you'll have manually play the audio tour during your trip.

1. Make an account at https://www.bushtalkradio.com and log in
3. Browse the map and find a destination that interests you and note the nearest airport, distance and the heading in the sidebar.
4. Spawn at the airport and fly towards your destination.
5. Once you've reached your destination, play the audio tour on the sidebar

## FAQ

### I love the idea! How can I support the project?

Help us by creating as many high quality landmarks with well written audio tours. You can also help by promoting the project to fellow flightsimmers. Finally, if you really love what we're doing then [help us pay for server costs](https://www.paypal.com/donate?hosted_button_id=PNDL5HN4K4KJN). Any amount is welcome.

### I have a feature request or bug to report

You can send me a message directly on [/u/bushtalkradio](https://www.reddit.com/user/bushtalkradio), email me at admin@bushtalkradio.com or through the feedback form on our webite via the '+' button.

### Windows is flagging the Bushtalk Client .exe/.zip file as a virus

Unfortunately exe files almost always get flagged as a virus. You should be able to override and download anyway and/or add the file to your trusted list. I've also chosen to open source the client, that way you can read the code and be sure nothing malicious is going on.

If you're not comfortable running a .exe file on your computer and you have Python installed, then you can follow the instructions below. I understand not a lot a people want to mess around with python scripts which is why I packaged it into a .exe.

1. Clone this repository: $ git clone https://github.com/BushtalkRadio/BushtalkClient.git
2. Run the client with python: $ python BushtalkClient.py

#### (OPTIONAL) How package python script into .exe

2. Install pyinstaller: $ pip install pyinstaller
3. Make sure SimConnect.dll is in the same directory as BushtalkClient.py
4. Create .exe with: $ pyinstaller -wF --add-data SimConnect.dll;. --icon=favicon.ico BushtalkClient.py



