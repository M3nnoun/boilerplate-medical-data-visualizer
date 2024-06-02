import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
# read data
df=pd.read_csv('medical_examination.csv')


# print(df.columns)
# 2
bmi = df['weight'] / np.square(df['height']/100)
df['overweight2'] = (bmi > 25).astype('uint8')
df['overweight'] = df.apply(lambda row: 1 if row['weight']/(row['height']/100)**2 > 25 else 0,axis=1)
print(df[['overweight','overweight2']])

# def normalize(value):
#     return 1 if value > 1 else 0 
# df['cholesterol']=df['cholesterol'].apply(normalize)
# df['gluc']=df['gluc'].apply(normalize)
# print(df.gluc.value_counts())
# print('here start ....')
# columns = [
#       'active',
#       'alco',
#       'cholesterol',
#       'gluc',
#       'overweight',
#       'smoke'
#     ]
# df_cat = pd.melt(df, id_vars=["cardio"], value_vars=columns)

#     # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the collumns for the catplot to work correctly.
# df_cat = df_cat.reset_index().groupby(['variable', 'cardio', 'value']).agg('count').rename(columns={'index': 'total'}).reset_index()
                
                
# # print(df_cat)

# fig = sns.catplot(data=df_cat, kind='bar', x='variable',y='total', hue='value', col='cardio')

# df_heat = df[
#         (df['ap_lo'] <= df['ap_hi'])
#         & (df['height'] >= df['height'].quantile(0.025))
#         & (df['height'] <= df['height'].quantile(0.975))
#         & (df['weight'] >= df['weight'].quantile(0.025))
#         & (df['weight'] <= df['weight'].quantile(0.975))
#     ]

#     # 12
# corr = df_heat.corr()

# mask = np.zeros_like(corr)
# mask[np.triu_indices_from(mask)] = True


# print('++++++++++++++++++++')
# print(corr)
# print('++++++++++++++++++++')
# # print(corr.to_numpy()[mask==1])
#  # 14
# fig1, ax = plt.subplots(figsize=(12, 6))


#     # 15

# sns.heatmap(data=corr,
#             annot=True, fmt='.1f',
#             mask=mask,
#             vmin=-0.5,
#             vmax=0.5,
#             ax=ax)
#     # 16
# fig1.savefig('heatmap.png')