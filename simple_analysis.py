import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv('data/raw/full_data_flightdelay.csv')

# Calculate delay statistics
total_flights = len(df)
delayed_flights = df['DEP_DEL15'].sum()
on_time_flights = total_flights - delayed_flights
delay_rate = (delayed_flights / total_flights) * 100

# Print statistics
print(f"Total flights: {total_flights:,}")
print(f"On-time flights: {on_time_flights:,}")
print(f"Delayed flights: {delayed_flights:,}")
print(f"Delay rate: {delay_rate:.2f}%")
print(f"On-time rate: {100-delay_rate:.2f}%")

# Create graph
plt.figure(figsize=(8, 6))
labels = ['On Time', 'Delayed']
counts = [on_time_flights, delayed_flights]
colors = ['green', 'red']

plt.bar(labels, counts, color=colors)
plt.title('Flight Delay Analysis')
plt.ylabel('Number of Flights')
for i, count in enumerate(counts):
    plt.text(i, count + 50000, f'{count:,}', ha='center', fontweight='bold')

plt.tight_layout()
plt.savefig('outputs/flight_delay_analysis.png', dpi=300, bbox_inches='tight')
plt.show()