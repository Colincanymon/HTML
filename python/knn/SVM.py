from sklearn import datasets
from sklearn.model_selection import train_select_split
from sklearn import metrics
from sklearn import svm
cancer=datasets.load_breast_cancer()
x_train,x_test,y_train,y_test=train_test_split(cancer.data,cancer.target,test_sized=0.3,random_state=100)