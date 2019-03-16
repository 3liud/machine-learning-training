import pandas

data = 'iris.csv'
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = pandas.read_csv(data, names=names)


#data shape
print(dataset.shape)
# data head
print(dataset.head(30))
#data description
print(dataset.describe())
