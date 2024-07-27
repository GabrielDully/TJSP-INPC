import pandas as pd
with open('datas.csv', 'r') as pewdiepie:
    dias = []
    meses = []
    for line in pewdiepie.readlines():
        if line != '':
            componentes = line.split('/')
            dias.append(componentes[0])
            meses.append(f'{componentes[1]}/{componentes[2][:4]}')
    df = pd.DataFrame({'dia': dias, 'meses': meses})
    df.to_csv('naruteba.csv', index=False)
        