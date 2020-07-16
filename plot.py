import pandas as pd
import matplotlib.pyplot as plt
import argparse

parser = argparse.ArgumentParser(description='Plot watch history file')
parser.add_argument('-i', metavar='input.txt', help='input file')

args = parser.parse_args()

filename = args.i

df = pd.read_csv(filename, parse_dates=True, names=['date'])
df["date"] = df["date"].astype("datetime64")

df.groupby([df['date'].dt.year, df['date'].dt.month]).count().plot(kind='bar')

plt.legend(["Videos watched on this month"])
plt.title('Amount of videos watched every month')
plt.ylabel('Amount of videos watched')
plt.xlabel('Month, Year')

plt.tight_layout()
plt.show()
