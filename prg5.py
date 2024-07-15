from sklearn.ensemble import RandomForestClassifier
from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score,classification_report
from sklearn.preprocessing import StandardScaler

iris=load_iris()
X=iris.data
y=iris.target

X_test,X_train,y_test,y_train=train_test_split(X,y,test_size=0.3,random_state=42)
clf=StandardScaler()
X_train=clf.fit_transform(X_train)
X_test=clf.transform(X_test)
clf=RandomForestClassifier(random_state=42)


clf.fit(X_train,y_train)

y_pred=clf.predict(X_test)

accuracy=accuracy_score(y_test,y_pred)

classification=classification_report(y_test,y_pred)

print(accuracy)
print(classification)