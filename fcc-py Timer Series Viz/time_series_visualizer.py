import calendar
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters


register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv',
                 index_col='date',
                 parse_dates=['date'])

# Clean data
df = df[(df['value'] >= df['value'].quantile(0.025))
        & (df['value'] <= df['value'].quantile(0.975))]


def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize=(32, 10))
    ax.plot(df.value, color='red', linewidth=3)
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')
    ax.tick_params('both', which='major', length=7, width=1.5, labelsize=20)
    
    plt.rcParams.update({
        'axes.linewidth': 1.5,
        'axes.titlesize': 24,
        'axes.titlepad': 12,
        'axes.labelsize': 20,
        'axes.labelpad': 8,,
        'xtick.major.pad': 7,
        'ytick.major.pad': 7,
    })

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig


def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar['year'] = df.index.year
    df_bar['month'] = df.index.month
    df_bar = df_bar.groupby(['year',
                             'month'])['value'].mean().unstack(level='month')
    df_bar.columns = calendar.month_name[1:]

    # Draw bar plot
    fig = df_bar.plot.bar(figsize=(14.8, 13)).figure
    plt.xlabel('Years')
    plt.ylabel('Average Page Views')
    plt.legend(title='Months', title_fontsize=19.5)
    
    plt.rcParams.update({
        'axes.linewidth': 1.5,
        'legend.labelspacing': 0.55,
        'xtick.major.size': 7,
        'xtick.major.width': 1.5,
        'xtick.major.pad': 7,
        'ytick.major.size': 7,
        'ytick.major.width': 1.5,
        'ytick.major.pad': 7,
    })

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig


def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box['year'] = df_box.index.year
    df_box['month'] = df_box.index.strftime('%b')

    # reset plt.rcParams values
    plt.rcdefaults()
    # Draw box plots (using Seaborn)
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(28.8, 10.8))

    ax1 = sns.boxplot(df_box, x='year', y='value', ax=ax1)
    ax1.set_title('Year-wise Box Plot (Trend)', fontsize=19.5)
    ax1.set_xlabel('Year', fontsize=16)
    ax1.set_ylabel('Page Views', fontsize=16)
    ax1.set_yticks(list(range(0, 220000, 20000)))
    ax1.tick_params(axis='both', which='major', labelsize=16)

    ax2 = sns.boxplot(df_box,x='month', y='value', ax=ax2,
                      order=calendar.month_abbr[1:],)
    ax2.set_title('Month-wise Box Plot (Seasonality)', fontsize=19.5)
    ax2.set_xlabel('Month', fontsize=16)
    ax2.set_ylabel('Page Views', fontsize=16)
    ax2.set_yticks(list(range(0, 220000, 20000)))
    ax2.tick_params(axis='both', which='major', labelsize=16)

    plt.tight_layout(pad=4.5, w_pad=4.5, h_pad=1.0)

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
