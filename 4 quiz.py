# noinspection PyUnresolvedReferences
import pandas as pd
# noinspection PyUnresolvedReferences
import numpy as np
# from import

aud_usd_lst = [
    ('2020-09-08', 0.7280),
    ('2020-09-09', 0.7209),
    ('2020-09-11', 0.7263),
    ('2020-09-14', 0.7281),
    ('2020-09-15', 0.7285),
    ]

eur_aud_lst = [
    ('2020-09-08',  1.6232),
    ('2020-09-09',  1.6321),
    ('2020-09-10',  1.6221),
    ('2020-09-11',  1.6282),
    ('2020-09-15',  1.6288),
    ]

# Replace unanswered with your solution.
aud_usd_series = pd.Series(np.array(aud_usd_lst)[:, 1], index=np.array(eur_aud_lst)[:, 0]).astype(float)
print(aud_usd_series)

eur_aud_series = pd.Series(np.array(eur_aud_lst)[:, 1], index=np.array(aud_usd_lst)[:, 0]).astype(float)
print(eur_aud_series)

df = pd.DataFrame({'AUD/USD': aud_usd_series, 'EUR/AUD': eur_aud_series})
print(df)

# aud_usd_df = pd.DataFrame(aud_usd_lst, columns=['Date', 'AUD/USD']).set_index('Date')
# eur_aud_df = pd.DataFrame(eur_aud_lst, columns=['Date', 'EUR/AUD']).set_index('Date')
#
# df = pd.merge(aud_usd_df, eur_aud_df, how='outer', left_index=True, right_index=True)
# print(df)