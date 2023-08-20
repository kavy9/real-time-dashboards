import pandas as pd

import finnhub

# Setup client
finnhub_client = finnhub.Client(api_key="cjb2vf1r01qn9c1l5iugcjb2vf1r01qn9c1l5iv0")

# Stock candles
res = finnhub_client.stock_candles('AAPL', 'D', 1590988249, 1591852249)
print(res)

finnhub_client.close()