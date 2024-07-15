from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,classification_report
from sklearn.datasets import fetch_20newsgroups

iris=fetch_20newsgroups()
X=iris.data
y=iris.target

X_test,X_train,y_test,y_train=train_test_split(X,y,test_size=0.3,random_state=42)

vec=TfidfVectorizer(stop_words='english')

X_test=vec.fit_transform(X_test)
X_train=vec.transform(X_train)

clf=MultinomialNB()

clf.fit(X_train,y_train)

y_pred=clf.predict(X_test)

accuracy=accuracy_score(y_test,y_pred)
print(classification_report(y_test,y_pred))