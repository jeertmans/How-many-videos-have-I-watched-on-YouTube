# How many videos have I watched on YouTube
 
This repository contains Python 3 codes which use your personal YouTube data to tell you how many videos you've watches as a function of time. Any improvement or add-on can be proposed.

## 1. Download your personal data

You can download it here : https://myaccount.google.com/u/0/yourdata/youtube.
Then, uncompress the whole **Takeout** folder. The file of interest is *watch-history.html*, located in **/Takeout/Youtube and Youtube Music/history**.

Depending on your Google account language, the folders may differ a little bit.

## 2. Indicate your locale

In order to parse datetimes, a dictionary is needed. It should contains months in English as keys and how they are written in your language as values. An example is provided for French, but I encourage you to submit your own locales.

## 3. Parse the data

In a terminal, run `python parse.py -i /path/to/watch_history.html -o output.txt -l locale.json`

## 4. Plot the data

In a terminal, run `python plot.py -i history.txt`

# Contributions or ideas to improve this repo

Any contribution or idea is welcomed and I'm will be happy to add your work to this repo or implement any add-on you feel interesting or fun :-)
