# # Downloads Qantas share price beginning 1 January 2020
# import yfinance
# tic = "QAN.AX"
# start = '2020-01-01'
# df = yfinance.download(tic, start, None)
# print(df)
# df.to_csv('qan_stk_prc.csv')

# Downloads Qantas share price beginning 1 January 2020
import yfinance as df
df.download("QAN.AX", '2020-01-01', None).to_csv('qan_stk_prce.csv')
