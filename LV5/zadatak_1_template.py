import numpy as np
import matplotlib
import matplotlib.pyplot as plt

from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix , ConfusionMatrixDisplay
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score

X, y = make_classification(n_samples=200, n_features=2, n_redundant=0, n_informative=2,
                            random_state=213, n_clusters_per_class=1, class_sep=1)

# train test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=5)

# a)

plt.scatter(x=X_train[:, 0], y=X_train[:, 1], c=y_train)
plt.scatter(x=X_test[:, 0], y=X_test[:, 1], c=y_test, marker='x')

# b)

logModel = LogisticRegression()
logModel.fit(X_train, y_train)

# c)

theta0 = logModel.intercept_
theta = logModel.coef_

#print(theta0)
#print(theta)

x = np.linspace(np.min(X_train[:, 0]), np.max(X_train), 20)
y = theta0[0] + theta[0, 0] * x + theta[0, 1] * pow(x, 2)

plt.plot(x, y, color='r')

plt.show()

# d)

y_test_p = logModel.predict(X_test)

disp = ConfusionMatrixDisplay(confusion_matrix(y_test, y_test_p))
disp.plot()

print(f"Tocnost: {accuracy_score(y_test, y_test_p)}")
print(f"Preciznost: {precision_score(y_test, y_test_p)}")
print(f"F1 score: {recall_score(y_test, y_test_p)}")

plt.show()

# e)

indT = y_test == y_test_p
indF = y_test != y_test_p

plt.scatter(X_test[indT, 0], X_test[indT, 1], c='g')
plt.scatter(X_test[indF, 0], X_test[indF, 1], c='k')

plt.show()