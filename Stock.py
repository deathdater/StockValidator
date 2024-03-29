class Stock:
    is_buy = False
    is_sell = False
    def __init__(self,stk_symbol,stk_open,stk_high,stk_low,stk_lasttradeprice,stk_change,stk_change_percent,stk_volume,stk_value,stk_year_high,stk_year_low,stk_year_change,stk_month_change):
        self.stk_symbol=stk_symbol
        self.stk_open=stk_open
        self.stk_high=stk_high
        self.stk_low=stk_low
        self.stk_lasttradeprice=stk_lasttradeprice
        self.stk_change=stk_change
        self.stk_change_percent=stk_change_percent
        self.stk_volume=stk_volume
        self.stk_value=stk_value
        self.stk_year_high=stk_year_high
        self.stk_year_low=stk_year_low
        self.stk_year_change=stk_year_change
        self.stk_month_change=stk_month_change
        self.set_buy()

    def print_stock_details(self):
        print("Symbol:            " +self.stk_symbol)
        print("Open Price:        " +self.stk_open)
        print("High:              " +self.stk_high)
        print("Low:               " +self.stk_low)
        print("LTP:               " +self.stk_lasttradeprice)
        print("Change:            " +self.stk_change)
        print("Change %age:       " +self.stk_change_percent)
        print("Traded Volume:     " +self.stk_volume)
        print("Traded Value:      " +self.stk_value)
        print("52 Week High:      " +self.stk_year_high)
        print("52 Week Low:       " +self.stk_year_low)
        print("365 Days % Change: " +self.stk_year_change)
        print("30 Days % Change:  " +self.stk_month_change)
        print("Buy:               " + str(self.is_buy))
        print("Sell:              " + str(self.is_sell))

    def set_buy(self):
        if self.stk_lasttradeprice >= self.stk_open:
            self.is_buy = True
        else:
            self.is_sell = True
