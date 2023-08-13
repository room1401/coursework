import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


# import data
df = pd.read_csv('medical_examination.csv')

# ddd 'overweight' column
df['overweight'] = np.where(df.weight / (df.height / 100)**2 > 25, 1, 0)
# normalize data
df['cholesterol'] = df['cholesterol'].map(lambda x: 0 if x == 1 else 1)
df['gluc'] = df['gluc'].map(lambda x: 0 if x == 1 else 1)

# draw categorical plot
def draw_cat_plot():
    # create DataFrame for cat plot from 6 features
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=df.iloc[:, 7:])
    # group and reformat data, split by 'cardio', then count features
    df_cat = df_cat.groupby(['cardio', 'variable', 'value'], \
            as_index=False).value_counts(sort=False)

    # get the figure for the output
    fig = sns.catplot(
        data=df_cat,
        x='variable',
        y='count',
        hue='value',
        col='cardio',
        kind='bar',
        height=5,
        )
    fig.set_ylabels('total')

    # do not modify the next two lines
    fig.savefig('catplot.png')
    return fig

# draw heat map
def draw_heat_map():
    # clean the data
    df_heat = df[(df['ap_lo'] <= df['ap_hi']) & \
                (df['height'] >= df['height'].quantile(0.025)) & \
                (df['height'] >= df['height'].quantile(0.025)) & \
                (df['height'] <= df['height'].quantile(0.975)) & \
                (df['weight'] >= df['weight'].quantile(0.025)) & \
                (df['weight'] <= df['weight'].quantile(0.975))]
    
    # calculate the correlation matrix
    df_corr = df_heat.corr()
    # generate a mask for the upper triangle
    df_mask = np.triu(df_corr).astype(bool)
    # set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(11, 9))
    # draw the heatmap with 'sns.heatmap()'
    sns.heatmap(df_corr, mask=df_mask,annot=True, annot_kws={"size": 7}, 
            fmt=".1f", linewidth=.5, vmax=0.30, vmin=-0.15, center=0, 
            cbar_kws={'shrink':0.5, 'ticks':[-0.08, 0.00, 0.08, 0.16, 0.24]},)
            
    # do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig
