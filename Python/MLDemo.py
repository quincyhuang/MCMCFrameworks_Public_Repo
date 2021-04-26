# original post: https://www.cnblogs.com/yszd/p/9167126.html


from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import numpy as np
import matplotlib.pyplot as plt

iris_dataset = load_iris() 
x_train, x_test, y_train, y_test = train_test_split(iris_dataset["data"], iris_dataset["target"], random_state=0)


knn = KNeighborsClassifier(n_neighbors=1) 
knn.fit(x_train, y_train)


y_pre = knn.predict(x_test)
score = knn.score(x_test, y_test)  
print("test set predictions:\n{}".format(y_test))
print("test set score:{:.2f}".format(score))
if score > 0.9:
    x_new = np.array([[5, 2.9, 1, 0.3]])
    print("x_new.shape:{}".format(x_new.shape))
    prediction = knn.predict(x_new) 
    print("prediction:{}".format(prediction))
    print("predicted target name:{}".format(iris_dataset["target_names"][prediction]))


    plt.plot(x_train, y_train, "b.") 
    plt.plot(x_test, y_test, "y.")  
    plt.plot(x_new, prediction, "ro")  
    plt.show()
else:
    print("used train or test data is not available !")