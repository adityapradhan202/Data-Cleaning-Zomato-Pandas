import numpy as np
import pandas as pd

zomato_df = pd.read_csv('zomato_dataset_india.csv')
zomato_df.rename(columns={'Best Seller':'Popularity', 'Votes':'Zomato Votes'}, inplace=True)

zomato_df = zomato_df.dropna(axis = 0)
dropped_cols = ['Dining Votes', 'Delivery Votes']
zomato_df = zomato_df.drop(dropped_cols, axis = 1)
zomato_df = zomato_df[zomato_df['Zomato Votes'] != 0]

grpcols = [
    'City', 'Place Name',
    'Restaurant Name',
    'Popularity',
    'Cuisine', 'Item Name'
]

zomato_df = zomato_df.groupby(grpcols).mean()
zomato_stats = zomato_df.describe()

if __name__ == "__main__":
    print(zomato_df.info())
    print("Zomato stats:")
    print(zomato_stats.transpose())
    print()
    print(zomato_df.head(15))
    
