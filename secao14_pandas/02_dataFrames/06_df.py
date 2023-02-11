import pandas as pd
dados = {
        'Idade': [45,34,56,21],
        'Profissão': ['Engeheiro','Desenvolvedor','Metalurgico','Médica']
        }
data_frame = pd.DataFrame(dados, index=['Roger','Cristiano','Diego','Carla'])
data_frame

data_frame.loc['Roger']
