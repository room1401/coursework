import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')
    oldest = df.Year.min()

    # Create scatter plot
    plt.scatter(df.Year, df['CSIRO Adjusted Sea Level'], marker='^')
    
    # Create first line of best fit
    lr1 = linregress(df.Year, df['CSIRO Adjusted Sea Level'])
    plt.plot(range(oldest, 2051), lr1.slope*range(oldest, 2051) + lr1.intercept, 
             'g', label=f'from {oldest}')

    # Create second line of best fit
    lr2 = linregress(df[df.Year > 1999].Year, df[df.Year > 1999]['CSIRO Adjusted Sea Level'])
    plt.plot(range(2000, 2051), lr2.slope*range(2000, 2051) + lr2.intercept, 
             'orange', label='from 2020')

    # Add labels and title
    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.legend(title='2050 forecast')

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png', dpi=200)
    return plt.gca()
