import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def plot_multiple(df, start_index, stop_index, start_row, stop_row, columns = 1, averaging=1):s

'''
    plots multiple columns of data on separate subplots,
    color encoded by target with optional smoothing

    Parameters
    ----------
    df: dataframe
    start_index: int
    stop_index: int
    start_row: int
    stop_row: int
    columns: int, default = 1
    averaging: int, default = 1

    Returns
    -------
    fig: matplotlib figure object

'''

    le = preprocessing.LabelEncoder()
    le.fit(df.event.unique())
    list(le.classes_)
    cm = le.transform(df.event[start_row:stop_row])

    rows_needed = (stop_index-start_index)/columns+1
    fig = plt.figure(figsize = (15, rows_needed*5))

    for i in range(start_index, stop_index):
        ax = fig.add_subplot(rows_needed, columns, i-start_index+1)
        y = df.iloc[:,i].rolling(averaging).mean().iloc[start_row:stop_row]
        x = np.arange(start_row, stop_row, 1)
        plt.xlabel(df.columns[i])
        line1 = ax.scatter(x, y, c = cm, marker='.')

    return (fig)

if __name__ == '__main__':
    path = input('path to csv file? ')
    df = pd.read_csv(path)
    start_index = int(input('start column number? '))
    stop_index = int(input('stop column number? '))
    start_row = int(input('start row? '))
    stop_row = int(input('stop row? '))
    columns = int(input('number of columns to plot? '))
    averaging = int(input('rolling average over how many rows? '))

    plot_multiple(df, start_index, stop_index, start_row, stop_row, columns = 1, averaging=1)

    plt.show()
