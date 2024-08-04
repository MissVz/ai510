# train svm classifier
#from sklearn import svm
from sklearn.ensemble import RandomForestClassifier # Vz

# train data 10 is mapped to prediction 1
# train data 100 is mapped to prediction 0
train_data = [[10], [100]]
train_target = [1, 0]

#clf = svm.SVC()
clf = RandomForestClassifier() # Vz train a Random Forest Classifier

#clf.fit(train_data, train_target)
clf.fit(train_data, train_target) # Vz

# save trained classifier as joblib for server to use
import joblib
joblib.dump(clf, "binary_clf.joblib")