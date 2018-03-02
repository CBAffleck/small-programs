# Netflix Viewing Stats

This program allows the user to specify the filename of the text file containing the content they copy and pasted from their Netflix account viewing history. Stats produced from this program include:
* Total watch time
* Date with most activity
	* Number of episodes watched on this date
	* Name of TV show watched
	* Time spent watching
* Show with the most watch time and hour count
* Most consecutive days of watching Netflix, with start and end dates
* A breakdown of views and time spent watching per show/movie 

## Getting Started

Following these instructions will help you get the program running so you can see your Netflix stats.

### Prerequisites

First make sure you have python2 installed on your computer.

Then go to Netflix. Click on "account" from the drop down menu under your profile picture. Scroll down to the bottom and under "My Profile" click on "Viewing activity". Here you'll see a breakdown of the shows you've seen. Scroll down until you're not able to scroll down any further, and click "CMD+A" or "CTRL+A" to select all of the content on the page. Paste this into a .txt file, and place that .txt file into the same directory as the netflix_stats.py file. 

### Running the program

After making sure your text file containing your netflix viewing history and the netflix_stats program file are in the same directory, run the following in your terminal:

```
python2 netflix_stats.py
```
You'll see a prompt for the filename of the .txt file you made earlier. Type that in (without the .txt extension), and check out your stats!

## Authors

* **Campbell Affleck**