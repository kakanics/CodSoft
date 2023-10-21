import pandas as pd
from surprise import Dataset, Reader
from surprise import SVD
from surprise.model_selection import train_test_split
from surprise import accuracy

dataset = pd.read_csv("file.csv")

reader = Reader(rating_scale=(1, 5))
data = Dataset.load_from_df(dataset[['user', 'item', 'rating']], reader)

trainset, testset = train_test_split(data, test_size=0.2)

algo = SVD()
algo.fit(trainset)
predictions = algo.test(testset)

rmse = accuracy.rmse(predictions)
print(f'RMSE: {rmse}')

user_id = 'User1'
items_to_recommend = []

all_items = dataset['item'].unique()

user_ratings = {}
for item in all_items:
    prediction = algo.predict(user_id, item)
    user_ratings[item] = prediction.est

recommended_items = sorted(user_ratings.items(), key=lambda x: x[1], reverse=True)[:3]

print(f'Recommended items for {user_id}:')
for item, rating in recommended_items:
    items_to_recommend.append(item)
    print(f'{item} (predicted rating: {rating}')
