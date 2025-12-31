from numpy import sqrt, log, exp
from scipy.stats import norm

class BlackScholesFormula:
    def __init__(
            self,
            volatility: float,
            stock_price: float,
            strike_price: float,
            time_to_expiration: float,
            interest_rate: float
    ):

        self.volatility = volatility
        self.stock_price = stock_price
        self.strike_price = strike_price
        self.time_to_expiration = time_to_expiration
        self.interest_rate = interest_rate

    def calculate(self):
        volatility = self.volatility
        stock_price = self.stock_price
        strike_price = self.strike_price
        time_to_expiration = self.time_to_expiration
        interest_rate = self.interest_rate

        d1 = ((log(stock_price/strike_price) + (interest_rate + volatility ** 2 / 2) * time_to_expiration) /
              (volatility * sqrt(time_to_expiration)))
        d2 = ((log(stock_price/strike_price) + (interest_rate - volatility ** 2 / 2) * time_to_expiration) /
              (volatility * sqrt(time_to_expiration)))

        N_d1 = norm.cdf(d1)
        N_d2 = norm.cdf(d2)

        N_minus_d1 = norm.cdf(-d1)
        N_minus_d2 = norm.cdf(-d2)

        call_price = (stock_price * N_d1) - (strike_price * exp(-interest_rate * time_to_expiration) * N_d2)
        put_price = (strike_price * exp(-interest_rate * time_to_expiration) * N_minus_d2) - (stock_price * N_minus_d1)
        
        self.call_price = call_price
        self.put_price = put_price

        self.call_delta = N_d1
        self.put_delta = N_d1 - 1
        self.call_gamma = norm.pdf(d1) / (stock_price * volatility * sqrt(time_to_expiration))
        self.put_gamma = self.call_gamma

    def __repr__(self):
        return (
            f"Black-Scholes Model Output:\n"
            f"---------------------------\n"
            f"Call Price: {self.call_price:.4f}\n"
            f"Put Price:  {self.put_price:.4f}\n"
            f"---------------------------\n"
            f"Call Delta: {self.call_delta:.4f}\n"
            f"Put Delta:  {self.put_delta:.4f}\n"
            f"Gamma:      {self.call_gamma:.4f}\n"
        )


def validate_number(prompt: str) -> float | None:
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("Error: non-negative number")
                continue
            return value
        except ValueError:
            print("Error: Non-valid Number")

if __name__ == '__main__':
    while True:
        print(f"Black-Scholes Model\n")
        print(f"-------------------\n")
        print("1. Run default calculation")
        print("2. Enter your own values")

        choice = input("\nEnter choice (1 or 2): ")

        params = {}

        if choice == "1":
            print("\nUsing Default Values...")

            params = {
                "time_to_expiration": 1.0,
                "strike_price": 100,
                "stock_price": 100,
                "volatility": 0.20,
                "interest_rate": 0.05
            }
            break

        elif choice == "2":
            print("\nEnter The Following Parameters:")
            params["stock_price"] = validate_number("Stock Price: ")
            params["strike_price"] = validate_number("Strike Price: ")
            params["time_to_expiration"] = validate_number("Time To Expiration: ")
            params["volatility"] = validate_number("Volatility: ")
            params["interest_rate"] = validate_number("Interest Rate: ")
            break

        else:
            print("\nInvalid selection. Enter 1 or 2")

    BS = BlackScholesFormula(**params)
    BS.calculate()
    print(BS)