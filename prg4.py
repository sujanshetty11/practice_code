from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score,classification_report
import numpy as np 
import matplotlib.pyplot as plt



iris=datasets.load_iris()
X=iris.data[:,:-2]
y=iris.target

X_train,X_test,y_train, y_test =train_test_split(X,y,test_size=0.3,random_state=42)



clf=SVC(kernel='linear',C=1.0,random_state=42)

clf.fit(X_train,y_train)

y_pred=clf.predict(X_test)
accuracy=accuracy_score(y_test,y_pred)

print("accuracy :",accuracy)

print("classification :",classification_report(y_test,y_pred,target_names=iris.target_names))

# import numpy as np
# import matplotlib.pyplot as plt
# from sklearn import datasets
# from sklearn.model_selection import train_test_split
# from sklearn.preprocessing import StandardScaler
# from sklearn.svm import SVC
# from sklearn.metrics import accuracy_score, classification_report
# # Load the Iris dataset
# iris = datasets.load_iris()
# X = iris.data[:, :2]  # Using only the first two features for easy visualization
# y = iris.target
# # Split the dataset into training and test sets
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
# # Standardize the features
# scaler = StandardScaler()
# X_train = scaler.fit_transform(X_train)
# X_test = scaler.transform(X_test)
# # Train the SVM classifier
# svm = SVC(kernel='linear', C=1.0, random_state=42)
# svm.fit(X_train, y_train)
# # Predict the test set results
# y_pred = svm.predict(X_test)
# # Evaluate the classifier
# print(f"Accuracy: {accuracy_score(y_test, y_pred):.2f}")
# print("Classification Report:")
# print(classification_report(y_test, y_pred, target_names=iris.target_names))