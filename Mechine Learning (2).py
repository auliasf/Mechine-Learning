from sklearn.neighbors import NearestCentroid

# Database: Gerbang logika AND
# x = Data, Y = Target 
x = [[0,0], [0,1], [1,1], [2,0], [2,2], [4,0], [4,4], [6,0], [6,6], [7,0]]
y = [0,0,1,0,2,0,4,0,6,0]

# Training and Classify
clf = NearestCentroid()
clf.fit(x,y)

# Prediksi
print ("Logika AND Metode K. Nearest Neighbors (KNN)")
print ("Logika = Prediksi")
print ("0 0 = ", clf.predict([[0,0]]))
print ("0 1 = ", clf.predict([[0,1]]))
print ("1 0 = ", clf.predict([[1,0]]))
print ("1 1 = ", clf.predict([[1,1]]))
print ("2 2 = ", clf.predict([[2,2]]))
print ("3 3 = ", clf.predict([[3,3]]))
print ("4 4 = ", clf.predict([[4,4]]))
print ("5 5 = ", clf.predict([[5,5]]))
print ("6 6 = ", clf.predict([[6,6]]))
print ("7 7 = ", clf.predict([[7,7]]))
