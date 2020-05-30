#Michael Solimano 2020

#Find the max close for any stock ticker in a user given time-frame.

import matplotlib.pyplot as plt
from pandas_datareader import data as pdr
from datetime import date
from datetime import datetime
import numpy as np
import yfinance as yf
yf.pdr_override()
import pandas as pd
import csv

def get_data(tick, start, end):
	#call yahoo finance to retrieve info on given stock and store data in a csv

	data = pdr.get_data_yahoo(tick, start=start, end=end)
	stock_name = tick+'_'+str(date.today())
	data.to_csv(stock_name+'.csv')
	print(f"Grabbed data on {stock_name} and stored it in a csv file.")

def compile_data(tick, start, end):
	#compile the data from the created csv and print the max close date

	get_data(tick, start, end)
	file = tick+'_'+str(date.today())+'.csv'
	with open(file) as f:
		read_file = csv.reader(f)
		header_row = next(read_file)

		#store close data from csv file in list
		closes = []
		for row in read_file:
			closes.append(row[4])
		max_close = max(closes)
	print(f"Highest close price for {tick.upper()} in this range is {max_close}.")

def run():
	#ask for user input and run the stock high-close finder functions

	tick = input("Enter stock ticker: ")
	start = input("Enter desired start date in form YEAR-MONTH-DAY: ")
	end = input("Enter desired end date in form YEAR-MONTH-DAY: ")
	compile_data(tick, start, end)

run()