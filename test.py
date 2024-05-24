import pandas as pd
Data = pd.read_csv("/Users/kshitijberi/Downloads/playground-series-s3e8/train.csv")
Data.to_csv("data/data.csv",index = False)