#JIRA FP-2
#compute returns over a period of z days in which you save
#x dollars, in ticker y, on a biweekly basis

from datetime import datetime
from datetime import timedelta
from dateutil.relativedelta import relativedelta
import yfinance as yf

#returns: the dates of the transactions, the stocks in the account at each transaction, the dollars in the account
#at each transaction, the savings at each instant

def compute_returns (start_date: datetime, amount_saved: float, ticker_str: str, period: relativedelta):

  relative_delta2 = relativedelta(weeks=2)
  ticker_data = yf.Ticker(ticker_str).history(start=start_date, end = start_date+period, interval = "1wk")

  stocks_in_acct_lst = []
  dollars_in_acct_lst = []
  savings_percentage_lst = []
  dates_lst = []

  stocks_in_acct = 0
  savings_perc = 0
  curr_date = start_date
  num_transactions = 0

  for i in range(len(ticker_data)):
    if i%2 == 0:
      price = ticker_data.iloc[i]["Open"]

      num_stocks_bought = amount_saved/price
      stocks_in_acct += num_stocks_bought
      num_transactions += 1

      stocks_in_acct_lst.append(num_stocks_bought)
      dollars_in_acct_lst.append(stocks_in_acct*price)
      savings_percentage_lst.append(100*((stocks_in_acct*price/(amount_saved*num_transactions))-1))
      dates_lst.append(curr_date)
      curr_date = curr_date + relativedelta(weeks=2)
  return list(zip(dates_lst, stocks_in_acct_lst, dollars_in_acct_lst, savings_percentage_lst))



  print(ticker_data)

#potential new questions: is there a tendency to lose money if the previous day was very volatile (big difference between low and high)

res = compute_returns(datetime(2010, 12, 22), 1000.0, ticker_str = "VTI", period = relativedelta(years=10))
print(res)