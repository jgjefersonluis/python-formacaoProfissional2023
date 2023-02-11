mask = data['Idade'] < 50
mask

nova_dframe = data[mask]
nova_dframe

nova_dframe = data[(data['Idade']>40) & (data['Altura']>1.75) ]
nova_dframe
