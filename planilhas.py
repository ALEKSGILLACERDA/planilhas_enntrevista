import pandas as pd
import numpy as np

np.random.seed(42)
connetions = 1000
start_date = pd.to_datetime('2025-04-01')
end_date = pd.to_datetime('2025-04-08')
dates = pd.date_range(start=start_date, end=end_date)

games = [
    'League of Legends', 'Valorant', 'Fortnite', 'Apex Legends',
    'Call of Duty: Warzone', 'Minecraft', 'Roblox', 'Counter-Strike 2',
    'PUBG', 'Genshin Impact', 'Hearthstone', 'Rocket League',
    'Overwatch 2', 'Among Us', 'Discord'
]

game_weights = [
    0.15, 0.12, 0.10, 0.08, 0.07, 0.06, 0.06, 0.05, 0.05,
    0.05, 0.04, 0.04, 0.04, 0.04, 0.05,
]

user_ids = [np.random.randint(10**2, 10**9) for _ in range(connetions)]
user_connetions = np.random.uniform(1, 40, size=connetions)

table = [
    (user_ids[i], pd.Timestamp(np.random.choice(dates)), np.random.choice(games, p=game_weights))
    for i in range(connetions)
    for _ in range(np.random.poisson(lam=user_connetions[i]))
]

df = pd.DataFrame(table, columns=['user_id', 'connection_date', 'app_name'])

print(df.head())
df.to_csv('base_conexoes_jogos_online_media_aleatoria.csv', index=False)
