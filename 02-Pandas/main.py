import pandas as pd 

# series - 1d labeled array
# dataframe - 2d labeled array
# df = pd.read_csv("pandas/Bengaluru_House_Data.csv")
# print(df)

customers = {
    "names" : ["navin", "vinoth"],
    "age": [20, 34]
}

print(pd.DataFrame(customers))