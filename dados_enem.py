import pandas as pd


df__enem = pd.read_csv('D:/pythonProject/MICRODADOS_ENEM_2019.csv', encoding='Latin1', sep=';')

print('Quantas pessoas de cada idade fizeram o enem 2019: ')
print(dict(df__enem['NU_IDADE'].value_counts()))
print('-=' * 60)

# ## -----------Quantas pessoas abaixo de 20 anos é do estado de SP ----------------------------------------------------
print('Quantas pessoas abaixo de 20 anos é do estado de SP: ')
pessoas_sp = df__enem.loc[df__enem['SG_UF_RESIDENCIA'] == 'SP']
print(int(pessoas_sp.loc[pessoas_sp['NU_IDADE'] < 21, ['NU_IDADE']].count()))
# Pessoas abaixo de 20 anos que fizeram o enem: 572395
print('-=' * 60)

# ## -------------- Dessas pessoas quantas são homens e quantas são mulheres -------------------------------------------
print('Dessas pessoas quantas são homens e quantas são mulheres: ')
print(pessoas_sp.loc[pessoas_sp['NU_IDADE'] < 21, ['TP_SEXO']].value_counts())
# Homens: 230250  Mulheres: 342145
print('-=' * 60)

# ##----------------------- Quantas pessoas moram em Itaperuna - RJ ----------------------------------------------------
print('Quantas pessoas que moram em Itaperuna fizeram o Enem - 2019:')
print(len(df__enem.loc[df__enem['NO_MUNICIPIO_RESIDENCIA'] == 'Itaperuna']))
print('-=' * 60)
# Resposta 1662 pessoas fizeram o enem em Itaperuna

# ## -------------Das pessoas de Itaperuna qual é média de idades, maior idade e a menor idade -------------------------
df_itaperuna = df__enem.loc[df__enem['NO_MUNICIPIO_RESIDENCIA'] == 'Itaperuna']
print('Das pessoas de Itaperuna qual é média de idades, maior idade e a menor idade')
print(f"Média: {df_itaperuna['NU_IDADE'].mean()}")
# média de idades: 20.63
print(f"Menor idade: {df_itaperuna['NU_IDADE'].min()}")
# menor idade: 14
print(f"Maior idade: {df_itaperuna['NU_IDADE'].max()}")
# maior idade: 64
print('-=' * 60)

# ##-------------------- De Itaperuna quantos homens e mulheres fizeram o enem -----------------------------------------
print(f"Quantidade de Homens e Mulheres que fizeram em Itaperuna: \n{df_itaperuna['TP_SEXO'].value_counts()}")
# Homens: 1015  Mulheres: 647
print('-=' * 60)

# ##-------------------------- Média, maior e menor nota em Itaperuna --------------------------------------------------
print('Média, maior e menor nota em Itaperuna:')
notas_Itaperuna = (df_itaperuna['NU_NOTA_CN'] + df_itaperuna['NU_NOTA_CH'] + df_itaperuna['NU_NOTA_LC'] +
                   df_itaperuna['NU_NOTA_MT']) / 4
notas_Itaperuna = notas_Itaperuna.dropna()
media = sum(notas_Itaperuna) / len(notas_Itaperuna)
maior = notas_Itaperuna.max()
menor = notas_Itaperuna.min()
print(f'Maior: {maior}, Menor: {menor}, Média: {media}')  
# Maior: 751.575  Menor: 378.35  Média: 534.751
print('-=' * 60)

# ##-------------------Em Itaperuna, quantos alunos de escola pública e privada fizeram o Enem--------------------------
print('Em Itaperuna, quantos alunos de escola pública e privada fizeram o Enem')
nao_respondeu = 0
publica = 0
privada = 0
for valor in df_itaperuna['TP_ESCOLA']:
    if valor == 1:
        nao_respondeu += 1
    elif valor == 2:
        publica += 1
    elif valor == 3:
        privada += 1
print(f'Não Respondeu: {nao_respondeu}, Pública: {publica}, Privada: {privada}')
print('-=' * 60)


