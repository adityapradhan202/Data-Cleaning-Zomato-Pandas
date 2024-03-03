from data_cleaning import zomato_stats  as zs
from data_cleaning import zomato_df as zdf

n_orders = zs['Prices']['count']
max_din_rating = zs['Dining Rating']['max']
min_din_rating = zs['Dining Rating']['min']
max_del_rating = zs['Delivery Rating']['max']
min_del_rating = zs['Delivery Rating']['min']
mean_din_rating = zs['Dining Rating']['mean']
mean_del_rating = zs['Delivery Rating']['mean']

print(zdf.info())
print()
print("Some statistical data from this zomato's dataset:")
print(f"Total number of orders: {n_orders}")
print(f"Average dining rating of the food that zomato delivers: {mean_din_rating:.2f}")
print(f"Average delivery rating of the food delivered: {mean_del_rating:.2f}")
print(f"Maximum delivery rating in the dataset: {max_del_rating}")
print(f"Minimum delivery rating in the dataset: {min_del_rating}")
print(f"Maximum dining rating in the dataset: {max_din_rating}")
print(f"Minimum dining rating in the dataset: {min_din_rating}")