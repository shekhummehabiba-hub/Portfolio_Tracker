from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150,
    "MSFT": 400,
    "AMZN": 180,
    "META": 500
}

# Portfolio data
portfolio = {}


@app.route("/")
def home():
    total_investment = 0
    portfolio_data = []

    for stock, quantity in portfolio.items():
        price = stock_prices[stock]
        investment = price * quantity
        total_investment += investment

        portfolio_data.append({
            "stock": stock,
            "price": price,
            "quantity": quantity,
            "investment": investment
        })

    return render_template(
        "index.html",
        stocks=stock_prices,
        portfolio=portfolio_data,
        total=total_investment
    )


@app.route("/add", methods=["POST"])
def add_stock():

    stock = request.form["stock"]
    quantity = int(request.form["quantity"])

    if stock in stock_prices:

        if stock in portfolio:
            portfolio[stock] += quantity
        else:
            portfolio[stock] = quantity

    return redirect("/")


@app.route("/remove/<stock>")
def remove_stock(stock):

    if stock in portfolio:
        del portfolio[stock]

    return redirect("/")


@app.route("/clear")
def clear_portfolio():

    portfolio.clear()

    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)