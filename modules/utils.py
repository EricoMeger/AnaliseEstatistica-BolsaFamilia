import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

class Utils():
    def __init__(self):
        pass
    
    def read_csv(self, file_path):
        return pd.read_csv(file_path)

    def plot_histogram(self, x, weights, x_label, y_label, title):
        plt.figure(figsize=(6, 4))

        sns.histplot(x= x, weights= weights, bins=len(x))
        plt.title(title)
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.ticklabel_format(style='plain', axis='y')
        plt.tight_layout()
        plt.savefig("images/histogram_" + title + ".png")
        plt.show()

    def plot_boxplot(self, data, x, y, x_label, y_label, title):
        plt.figure(figsize=(10, 6))
        sns.boxplot(x= x, y= y, data=data)
        plt.title(title)
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.ticklabel_format(style='plain', axis='y')
        plt.savefig("images/boxplot_" + title + ".png")
        plt.show()

    def plot_scatterplot(self, data, x, y, xlabel, ylabel, title):
        plt.figure(figsize=(10, 6))
        sns.scatterplot(x= x, y= y, data= data)
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.ticklabel_format(style='plain', axis='y')
        plt.ticklabel_format(style='plain', axis='x')
        plt.axhline(0, color='gray', linewidth=0.8, linestyle='--')
        plt.axvline(0, color='gray', linewidth=0.8, linestyle='--')
        plt.savefig("images/scatterplot_" + title + ".png")
        plt.show()

    def plot_regression(self, data, x, y, predicted_values, xlabel, ylabel, title):
        plt.figure(figsize=(10, 6))
        sns.scatterplot(x=x, y=y, data=data)
        plt.plot(data[x], predicted_values, color='red')
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.savefig("images/regression_" + title + ".png")
        plt.show()

