import csv
from datetime import datetime

import matplotlib.pyplot as plt

#filename = 'data/sitka_weather_07-2018_simple.csv'
filename = 'data/sitka_weather_2018_simple_modified.csv'
try:
    with open(filename) as f:
        reader = csv.reader(f)
        #print(type(reader))
        header_row = next(reader)
        
        #print(header_row)

        """#Fonksiyonda neden highs bile empty list döndü
        highs, dates = [], []
        def _deneme(rdr, highs, dates):
            highs = [int(row[5]) for row in reader]
            dates = [datetime.strptime(d[2], '%Y-%m-%d') for d in reader]
        _deneme(reader, highs, dates)

        # Get dates and high temperatures from this file.
        highs = [int(row[5]) for row in reader]
        dates = [datetime.strptime(d[2], '%Y-%m-%d') for d in reader]
        """
        # Get dates, and high and low temperatures from this file.
        row_number = 1
        highs, dates, lows = [], [], []
        for row in reader:
            try:
                current_date = datetime.strptime(row[2], '%Y-%m-%d')
                high = int(row[5])
                low = int(row[6])
                row_number += 1
            # Bu ValueError current_date'de kapsar mı(eğer datetime.strptime
            #None or '' işleyemiyorsa, exception'a bak)
            except ValueError:
                print(f"Missing data for row_number={row_number}")
            else:
                dates.append(current_date)
                highs.append(high)
                lows.append(low)

except FileNotFoundError:
    print('fnfe')
else:
    #print(type(header_row))
    for index, column_number in enumerate(header_row):
        print(index, column_number)
    #print(type(enumerate(header_row)))
    #print("-----------------")
    #print(reader)
    #print(highs)
    print(type(dates))

    # Plot the high and low temperatures.
    plt.style.use('seaborn')
    #plt.style.use('classic')
    fig, ax = plt.subplots()
    ax.plot(dates, highs, c='red', alpha=0.5)
    ax.plot(dates, lows, c='blue', alpha=0.5)
    plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

    # Format plot.
    #plt.title("Daily high tempratures, July 2018", fontsize=24)
    plt.title("Daily high and low tempratures - 2018", fontsize=24)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Temprature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)

    plt.show()

