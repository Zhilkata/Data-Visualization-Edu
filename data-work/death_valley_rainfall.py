import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename = 'data/death_valley_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Get perspiration
    dates, prcp = [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        persp = float(row[3])
        dates.append(current_date)
        prcp.append(persp)
# Plot the perspiration
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, prcp, c='red')

# Format plot
plt.title("Daily perspiration, 2018\nDeath Valley", fontsize=20)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Perspiration", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
