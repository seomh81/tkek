from datetime import datetime

import pandas as pd

now = datetime.now()
one_mon_ago = now + pd.DateOffset(months=-1)
one_mon_ago1 = one_mon_ago.month

print(one_mon_ago1)
