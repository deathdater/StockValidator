from Stock import Stock
import csv
with open('data.csv', newline='\n') as f:
    reader = csv.reader(f)
    stock_array = []
#    number_of_records = len(list(f))
    for row in reader:

        print()
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

    print(stock_array.__getattribute__(stk_symbol))
            #print(row[i], end='\t')
      #  print(row[0])

'''
stock_data_file = open("data.csv", "r")
    print(stock_data_file.readline())

if(stock_data_file.readable()):
    for stock in stock_data_file.readlines():
        print(stock)
else:
    print("File Not Readable")

stock_data_file.close()

'''