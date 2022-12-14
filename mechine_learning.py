# -*- coding: utf-8 -*-
"""Mechine Learning

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_SyQ438ekhGX4ycaERD1L2IO_PFB8Iz5
"""

from sklearn import tree

# Database: Gerbang Logika AND
# x = Data , Y = Target
x = [[0,0], [0,1], [1,0], [1,1], [0,2], [2,0], [2,2], [0,3], [3,0], [3,3]]
y = [0,0,0,1,0,0,2,0,0,3]

# Training and Classify
clf = tree.DecisionTreeClassifier()
clf = clf.fit(x,y)

# Prediksi
print ("Logika AND Metode Desicion Tree")
print ("Logika = Prediksi")
print (" 0 0 = ", clf.predict([[0,0]]))
print (" 0 1 = ", clf.predict([[0,1]]))
print (" 1 0 = ", clf.predict([[1,0]]))
print (" 1 1 = ", clf.predict([[1,1]]))
print (" 0 2 = ", clf.predict([[0,2]]))
print (" 2 0 = ", clf.predict([[2,0]]))
print (" 2 2 = ", clf.predict([[2,2]]))
print (" 0 3 = ", clf.predict([[0,3]]))
print (" 3 0 = ", clf.predict([[3,0]]))
print (" 3 3 = ", clf.predict([[3,3]]))
