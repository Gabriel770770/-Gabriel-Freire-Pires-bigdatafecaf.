import pandas as pd
from sqlalchemy import create_engine

# Conexão com o banco de dados
engine = create_engine('postgresql://user:GaaBs7007.@192.168.1.47:5432/database')

# Leitura do arquivo CSV
df = pd.read_csv('temperature_readings.csv')

# Inserção dos dados no banco de dados
df.to_sql('temperature_readings', engine, if_exists='replace', index=False)