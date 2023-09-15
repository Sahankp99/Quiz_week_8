import matplotlib.pyplot as plt
import pandas as pd
# Read csv file
df = pd.read_csv('climate.csv')

years = []
co2 = []
temp = []

# loop to extract and save values in variables
for index, row in df.iterrows():
    years.append(int(row[0]))
    co2.append(int(row[1]))
    temp.append(row[2])


plt.subplot(2, 1, 1)
plt.plot(years, co2, 'b--')
plt.title("Climate Data")
plt.ylabel("[CO2]")
plt.xlabel("Year (decade)")

plt.subplot(2, 1, 2)
plt.plot(years, temp, 'r*-')
plt.ylabel("Temp (C)")
plt.xlabel("Year (decade)")
plt.show()
plt.savefig("co2_temp_2.png")
