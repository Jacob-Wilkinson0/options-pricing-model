from numpy import sqrt, log

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

    def calc_prices(self):
        volatility = self.volatility
        stock_price = self.stock_price
        strike_price = self.strike_price
        time_to_expiration = self.time_to_expiration
        interest_rate = self.interest_rate

        d1 = (log(stock_price/strike_price) + (interest_rate + volatility ** 2 / 2) * time_to_expiration) / (volatility * sqrt(time_to_expiration))
        d2 = (log(stock_price/strike_price) + (interest_rate - volatility ** 2 / 2) * time_to_expiration) / (volatility * sqrt(time_to_expiration))