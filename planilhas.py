import pandas as pd
import numpy as np

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

game_weights = [
    0.15, 0.12, 0.10, 0.08, 0.07, 0.06, 0.06, 0.05, 0.05,
    0.05, 0.04, 0.04, 0.04, 0.04, 0.05
]

# Gerar usuários únicos
user_ids = [np.random.randint(10**2, 10**9) for _ in range(num_users)]

# Gerar valor médio de conexões para cada usuário
user_connections = np.random.gamma(shape=2.0, scale=7.0, size=num_users)

# Criar a tabela com list comprehension (sem zip)
data = [
    (user_ids[i], np.random.choice(dates), np.random.choice(games, p=game_weights))
    for i in range(num_users)
    for _ in range(np.random.poisson(user_connections[i]))
]

# Criar DataFrame
df = pd.DataFrame(data, columns=['user_id', 'connection_date', 'app_name'])

# Salvar CSV
df.to_csv('base_conexoes_distribuicao_realista.csv', index=False)
