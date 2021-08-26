# Load libraries
from pandas import read_csv
import matplotlib.pyplot as plt
import seaborn as sns


# Load dataset
url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = read_csv(url, names=names)

# # basic functions
print(dataset.head(5))      # shows first 5 rows
print(dataset.describe())   # describes basic statistical information  

# Figure comparing sepals between classes of irises
plt.figure(figsize=(17, 9))
plt.title("Comparison between various species based on sepal length and width")
sns.set_theme(style="darkgrid")
sns.scatterplot(x=dataset["sepal-length"], y=dataset["sepal-width"], hue=dataset["class"], s=50)
plt.show()

# Figure comparing petals between classes of irises
plt.figure(figsize=(17, 9))
plt.title("Comparison between various species based on petal length and width")
sns.set_theme(style="darkgrid")
sns.scatterplot(x=dataset["petal-length"], y=dataset["petal-width"], hue=dataset["class"], s=50)
plt.show()
