# Stock Portfolio Tracker

stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 330,
    "AMZN": 145
}

portfolio = {}
total_investment = 0

print("Available Stocks:")
for stock, price in stock_prices.items():
    print(f"{stock} : ${price}")

while True:
    stock_name = input("\nEnter Stock Name (or 'done' to finish): ").upper()

    if stock_name == "DONE":
        break

    if stock_name not in stock_prices:
        print("Stock not available!")
        continue

    quantity = int(input("Enter Quantity: "))
    portfolio[stock_name] = portfolio.get(stock_name, 0) + quantity

print("\n----- Portfolio Summary -----")

for stock, quantity in portfolio.items():
    value = stock_prices[stock] * quantity
    total_investment += value
    print(f"{stock} - {quantity} shares × ${stock_prices[stock]} = ${value}")

print(f"\nTotal Investment Value = ${total_investment}")

# Save to text file
with open("portfolio_summary.txt", "w") as file:
    file.write("Stock Portfolio Summary\n")
    file.write("-------------------------\n")

    for stock, quantity in portfolio.items():
        value = stock_prices[stock] * quantity
        file.write(f"{stock}: {quantity} shares = ${value}\n")

    file.write(f"\nTotal Investment Value = ${total_investment}")

print("\nPortfolio saved as 'portfolio_summary.txt'")