from sklearn.datasets import load_iris
import numpy
#loading all data
iris=load_iris()
#printing feature names
#print(iris.feature_names)
#target target_names
#print(iris.target_names)

#training data
#print(iris.data)

#tarfet or flower_data
#print(iris.target)

setosa=iris.data[0:50]
print (setosa)

x=[0,50,100]
only_target_training=numpy.delete(iris.target,x,axis=0)
only_data_training=numpy.delete(iris.data,x,axis=0)

print(only_target_training)
print(only_data_training)

print(only_target_training.size)
print(only_data_training.size)

test_target=iris.target[x]
print(test_target)
