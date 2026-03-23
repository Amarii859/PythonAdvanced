import pandas as pd
import matplotlib.pyplot as plt

# Create dataset manually
data = {
    "date": [
        "2023-01-01","2023-01-02","2023-02-01","2023-02-02",
        "2023-03-01","2023-03-02","2023-07-01","2023-07-02",
        "2023-08-01","2023-08-02"
    ],
    "temperature": [5, 6, 8, 7, 12, 14, 30, 32, 35, 34]
}

df = pd.DataFrame(data)

# Convert date column
df["date"] = pd.to_datetime(df["date"])

print(df.head())

# 1. Average temperature
print("Average Temperature:", df["temperature"].mean())

# 2. Monthly averages
df["month"] = df["date"].dt.month
print("\nMonthly Average:\n", df.groupby("month")["temperature"].mean())

# 3. Hottest and coldest days
print("\nHottest Day:\n", df.loc[df["temperature"].idxmax()])
print("\nColdest Day:\n", df.loc[df["temperature"].idxmin()])

# 4. Plot
plt.plot(df["date"], df["temperature"])
plt.title("Tokyo Temperature")
plt.xlabel("Date")
plt.ylabel("Temperature")
plt.show()