import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    y = df['CSIRO Adjusted Sea Level']
    x = df['Year']
    fig, ax = plt.subplots()
    plt.scatter(x,y)

    # Create first line of best fit
    res = linregress(x,y)
    x_pred = pd.Series([i for i in range(1880, 2050)])
    y_pred = res.slope*x_pred + res.intercept
    plt.plot(x_pred,y_pred,'r')

    # Create second line of best fit
    df_2000 = df.loc[df['Year'] >= 2000]
    new_x = df_2000['Year']
    new_y = df_2000['CSIRO Adjusted Sea Level']
    res2 = linregress(new_x, new_y)
    x_pred_new = pd.Series([i for i in range(2000, 2050)])
    y_pred_new = res2.slope*x_pred_new + res2.intercept
    plt.plot(x_pred_new, y_pred_new, 'green')


    # Add labels and title
    ax.set_title('Rise in Sea Level')
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
draw_plot()