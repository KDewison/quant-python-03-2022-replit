#import pandas

import pandas as pd

#Load datafile and assign it

surveys_df = pd.read_csv("surveys.csv")

#describe the weight column

desc_weight = surveys_df["weight"].describe()

#Print out summary of stats

print(desc_weight)