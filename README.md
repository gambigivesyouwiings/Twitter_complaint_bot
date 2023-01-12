# Twitter_complaint_bot

#Introduction:
--------------------------------------------------------------------

Have you ever gotten bad service from your Internet Service Provider on a consistent basis and wanted to complain but don't have the time and energy to keep doing it? This bot automates that for you,

Run an Internet speed test,

Fetch the download and upload speeds.

Log into twitter and share your complaint.

That's it. As a bonus, you can tag your Intenet Provder.

#Functionality:
-----------------------------------------------------------------------
The code is based on two files. 

1: The InternetSpeedTest.py, which stores a class that has all the bot functionality. i.e: get_internet_speed(), text_internet_provider()

2: The main.py - this is the driver code.

In the program, you will notice two requirements for you to set up. The selenium package and the consumer secret keys from the Twitter API.

Get the selenium executable file on your computer. Copy the absolute path. Paste it in the path variable in the code. That's it.

From the twitter developer API, copy each of the keys and plug into the variable constants in Internetspeedtest.py
