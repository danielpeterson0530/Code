#!/sbin/python3
#split GOterm data

# NOTE: pass file named as test.txt in following format:
# GOterm,Genes
# GO:001,AFLA_001|AFLA_002|AFLA_003
# GO:002,AFLA_005|AFLA_006|AFLA_007
# GO:003,AFLA_008|AFLA_009
# GO:004,AFLA_099|AFLA_098
# GO:005,AFLA_097
#
# NOTE: will drop empty cells (not spaces/tabs, just empty)

import pandas as pd
import numpy as np

df1 = pd.read_csv("~/test/test.txt")
df = pd.DataFrame(data=df1)
new_df = pd.DataFrame(df.Genes.str.split('|').tolist(), index=df.GOterm).stack()
new_df = new_df.reset_index([0, 'GOterm'])
new_df.columns = ['GOterm', 'Genes']
new_df.replace('', np.nan, inplace=True)
new_df.dropna(inplace=True)
csv = new_df.to_csv(index=False)
print(csv)
