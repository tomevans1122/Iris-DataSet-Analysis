# Iris-DataSet-Analysis

This repository investigates the iris dataset. This dataset contains information on three different classes of flowers. It has been used extensively in machine learning so I thought it a good dataset to conduct analysis of machine learning models on. Here is a snippet of what the dataset looks like: 
| Sepal-length | sepal-width | petal-length | petal-width | class |
|---------------|---------------|--------------|--------------|-------|
|  5.1 | 3.5 | 1.4 | 0.2 | iris-setosa |
| 4.9  | 3.0 | 1.4 | 0.2 | Iris-setosa |

There are 50 entries for each species, thus totalling 150 entries.

## iris-investigation.py

This script produces a first look at the data:

sepal-length |  sepal-width  | petal-length | petal-width
-------------|---------------|--------------|--------------
count  |  150.000000  | 150.000000   | 150.000000 |  150.000000
mean  |     5.843333  |   3.054000   |   3.758667  |   1.198667
std    |    0.828066  |   0.433594    |  1.764420  |   0.763161

The table shows the sepal dimensions are on average bigger than petal dimensions for all classes of iris species. <br/>
###### comparing_sepals.png 
This figure compares sepal widths and lengths across the three classes of iris class. The figure shows three things: 
* Iris-setosa tends to have the largest sepal width and shortest sepal length 
* Iris-versicolor and iris-verginica tend to have similar sepal widths
* Iris-verginica tends to have the largest sepal length

###### comparing_petals.png
This figure is analagous to the figure described above, however this time regarding petal lengths and widths across the three classes. This figure shows a much clearer picture:
* Iris-setosa have much smaller petal lengths and widths compared to the other species
* The vast majority of Iris-verginica show superior petal lengths and widths to Iris-versicolor
* There is less spread of the data for each class compared to the previous sepal figure

