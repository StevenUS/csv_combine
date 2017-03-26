import pandas as pd

# filenames
excel_names = ["August2016_0599.csv", "August2016_2808.csv", "December2016_0599.csv", "December2016_2808.csv", "February2016_0599.csv", "February2016_2808.csv", "January2016_0599.csv", "January2016_2808.csv", "July2016_0599.csv", "July2016_2808.csv",  "June2016_0599.csv", "June2016_2808.csv",  "November2016_0599.csv", "November2016_2808.csv",  "October2016_0599.csv", "October2016_2808.csv", "September2016_0599.csv", "September2016_2808.csv"]

# read them in
excels = [pd.ExcelFile(name) for name in excel_names]

# turn them into dataframes
frames = [x.parse(x.sheet_names[0], header=None,index_col=None) for x in excels]

# delete the first row for all frames except the first
# i.e. remove the header row -- assumes it's the first
frames[1:] = [df[1:] for df in frames[1:]]

# concatenate them..
combined = pd.concat(frames)

# write it out
combined.to_csv("c.csv", header=False, index=False)
