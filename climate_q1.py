import sqlite3
import matplotlib.pyplot as plt

conn = sqlite3.connect(r"climate.db")
cursor = conn.cursor()

sql_command = "SELECT * FROM ClimateData"
cursor.execute(sql_command)
result = cursor.fetchall()

years = []
co2 = []
temp = []

for row in result:
    years.append(row[0])
    co2.append(row[1])
    temp.append(row[2])
conn.close()

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
plt.savefig("co2_temp_1.png")
