from bs4 import BeautifulSoup
import datetime
import json
import argparse
from tqdm import tqdm

parser = argparse.ArgumentParser(description='Parse watch history file')
parser.add_argument('-i', metavar='input.html', help='input file')
parser.add_argument('-o', metavar='output.txt', help='output file')
parser.add_argument('-l', metavar='locale.json', help='locale file')

args = parser.parse_args()

filename = args.i
date_format = "%d %B %Y" # Example : 15 July 2020 - a better format can be use to extract HH:MM informations
history_output_filename = args.o

print(f"Opening and reading file {filename}")
data = open(filename, encoding='UTF8').read()

print("Parsing HTML")
soup = BeautifulSoup(data, 'lxml')


months = json.load(open(args.l, 'r', encoding='UTF8'))

print("Searching for videos watches...", end="")


output_file = open(history_output_filename, "w")

for box in tqdm(soup.find_all('div', class_="mdl-grid")):

    video_watched = box.find('div', class_="content-cell mdl-cell mdl-cell--6-col mdl-typography--body-1")
    
    
    if video_watched:
        text = repr(video_watched)
        date_raw = " ".join(text.split("<br/>")[-1].split(" ")[:3])
        
        for key, value in months.items():
            date_raw = date_raw.replace(value, key)
            
        date = datetime.datetime.strptime(date_raw, date_format)
        output_file.write(str(date) + "\n")


output_file.close()

print(f" Done !\nSaved everything in {history_output_filename}")
