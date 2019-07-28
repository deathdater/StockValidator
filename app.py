from Stock import Stock
import csv,os

with open('data.csv', newline='\n') as f:
    reader = csv.reader(f)
    stock_array = []
#    number_of_records = len(list(f))
    for row in reader:

        #print()
        for i in range(13): ## Intialize single Stock
            Stock.stk_symbol = row[0]
            Stock.stk_open = row[1]
            Stock.stk_high = row[2]
            Stock.stk_low = row[3]
            Stock.stk_lasttradeprice = row[4]
            Stock.stk_change = row[5]
            Stock.stk_change_percent = row[6]
            Stock.stk_volume = row[7]
            Stock.stk_value = row[8]
            Stock.stk_year_high = row[9]
            Stock.stk_year_low = row[10]
            Stock.stk_year_change = row[11]
            Stock.stk_month_change = row[12]


        stock_array.append(Stock(Stock.stk_symbol,Stock.stk_open,Stock.stk_high,
                                     Stock.stk_low,Stock.stk_lasttradeprice,Stock.stk_change,
                                     Stock.stk_change_percent,Stock.stk_volume,
                                     Stock.stk_value,Stock.stk_year_high,Stock.stk_year_low,
                                     Stock.stk_year_change,Stock.stk_month_change))

#        print(Stock.stk_symbol)
    # Stock.print_stock_details(stock_array[2])
choice = 0
while choice is not str(4):
    print("\n\n\nSelect your Choice:\n\t1. Search"
          "\n\t1. Find Intraday Buys Calls"
          "\n\t3. Find Intraday Sells Calls"
          "\n\t4. Quit")
    choice = input("\nEnter Your Choice :")
    if choice == str(1):
        stockname = input("Enter the Stock Name (As Listed on NSE) :")
        ## Searching the stock  based on user input
        for obj in stock_array:
            if obj.stk_symbol == stockname.upper():
                print("Found it ..!!")
                obj.print_stock_details()
                break
            else:
                None

    elif choice == str(2):

        ## Searching the stock based on Buy Trend
        for obj in stock_array:
            if obj.is_buy == True:
                print(obj.stk_symbol)
            else:
                None

    elif choice == str(3):
        ## Searching the stock based on Sell Trend
        for obj in stock_array:
            if obj.is_sell == True:
                print(obj.stk_symbol)
            else:
                None

    elif choice == str(4):
        exit(0)

    else:
        print("\n\nIncorrect Choice!! Try Again")
