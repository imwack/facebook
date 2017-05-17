#coding=utf-8
from sklearn.datasets import load_digits
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

digits = load_digits()
print(digits.data.shape)
data = digits.data
target = digits.target

feature_train, feature_test, target_train, target_test = train_test_split(data, target, test_size=0.5, random_state=1)

clf = tree.DecisionTreeClassifier()
clf.fit(data[0:len(data)/2], target[0:len(data)/2])
r = clf.score(data[len(data)/2:], target[len(data)/2:])
print r

clf.fit(feature_train, target_train)
r = clf.score(feature_test, target_test)
print r


clf = RandomForestClassifier(n_estimators=5)  # 5 tree
clf.fit(data[0:len(data)/2], target[0:len(data)/2])
r = clf.score(data[len(data)/2:], target[len(data)/2:])
print r

clf.fit(feature_train, target_train)
r = clf.score(feature_test, target_test)
print r
