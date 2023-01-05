import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

def scatter_plot_x(data: pd.DataFrame, x, y):
    sns.lineplot(
        data=data,
        x=x,
        y=y
    )