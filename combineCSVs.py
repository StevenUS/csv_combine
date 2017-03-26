import os
import glob
import pandas as pd

# assign path to the folder where the script is located
path = os.path.dirname(os.path.realpath(__file__))

# join files together
# allFiles = os.path.join(path, "*.csv")
allFiles = filenames = glob.glob(path + "/*.csv")

#create a data frame
frame = pd.DataFrame()

# create empty list for csvs to temporarily live
list_ = []

# loop through allFiles and append to the empty list
for file_ in allFiles:
    df = pd.read_csv(file_,index_col=None, header=0)
    list_.append(df)

# concatenate into empty frame
frame = pd.concat(list_)

frame.to_csv("combined.csv", header=False, index=False)
