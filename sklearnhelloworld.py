from sklearn import tree

print( 'start' )

features = [[140, 1], [130, 1], [150, 0], [170, 0]]
labels = [0, 0, 1, 1]

clf = tree.DecisionTreeClassifier()

print( 'train' )
clf = clf.fit( features, labels )

print( 'predict' )
print( clf.predict( [[145, 0]] ) )
