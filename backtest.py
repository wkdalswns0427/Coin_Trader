import pyupbit
import numpy as np

# 7일간 리플 코인의 코인 시장에서 open시가 high고가 low저가 close종가 volume거래량
df = pyupbit.get_ohlcv("KRW-XRP")
df['range'] = (df['high'] - df['low']) * 0.5
df['target'] = df['open'] + df['range'].shift(1)

# fee = 0.0032
df['ror'] = np.where(df['high'] > df['target'],
                     df['close'] / df['target'],
                     1)

df['hpr'] = df['ror'].cumprod()
df['dd'] = (df['hpr'].cummax() - df['hpr']) / df['hpr'].cummax() * 100
print("MDD(%): ", df['dd'].max())
df.to_excel("dd.xlsx")