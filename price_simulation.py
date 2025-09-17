import numpy as np
import matplotlib.pyplot as plt
import random

edge = 2.0  # % edge

def refresh_simulation():
    plt.cla()
    price = 100 # initial stock price
    prices = [price]

    total_expected_return = 1 + (edge / 100)
    period_edge = np.log(total_expected_return) / 100
    
    for _ in range(1000): # no. of price changes
        change = random.gauss(period_edge, 0.003)  # volatility e.g. 0.003 == 3% vol
        price *= np.exp(change)
        prices.append(price)
    
    final_return = (prices[-1] - 100) / 100 * 100 # Calculate actual return percentage
    plt.plot(prices, 'blue')
    plt.axhline(y=100, color='red', linestyle='--') # baseline / start price value
    plt.title(f"Stock Price\n{edge}% Total Edge                  Return: {final_return:.1f}%")
    plt.xlabel("no. of price changes")
    plt.ylabel("Price ")
    plt.draw()

fig, ax = plt.subplots(figsize=(10, 5))
fig.canvas.mpl_connect('key_press_event', lambda event: refresh_simulation() if event.key == 'r' else None) # press 'R' to refresh
refresh_simulation()
plt.show()