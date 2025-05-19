import pandas as pd
import numpy as np

# Configurações
np.random.seed(42)
num_users = 1000
start_date = pd.to_datetime('2025-04-01')
end_date = pd.to_datetime('2025-04-08')
dates = pd.date_range(start=start_date, end=end_date)

games = [
    'League of Legends', 'Valorant', 'Fortnite', 'Apex Legends',
    'Call of Duty: Warzone', 'Minecraft', 'Roblox', 'Counter-Strike 2',
    'PUBG', 'Genshin Impact', 'Hearthstone', 'Rocket League',
    'Overwatch 2', 'Among Us', 'Discord'
]

# Gerar IDs únicos com 3 a 9 dígitos
user_ids = [
    np.random.randint(10**2, 10**9)
    for _ in range(num_users)
]

# Gerar médias aleatórias para cada usuário (entre 5 e 40 conexões)
user_lambdas = np.random.uniform(5, 40, size=num_users)

rows = []
for user_id, lam in zip(user_ids, user_lambdas):
    num_connections = np.random.poisson(lam=lam)
    for _ in range(num_connections):
        connection_date = np.random.choice(dates)
        app_name = np.random.choice(games)
        rows.append((user_id, connection_date.date(), app_name))

df = pd.DataFrame(rows, columns=['user_id', 'connection_date', 'app_name'])

print(df.head())

df.to_csv('base_conexoes_jogos_online_media_aleatoria.csv', index=False)
