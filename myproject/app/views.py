from django.shortcuts import render
from app.forms import *
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
# Create your views here.
def show(request):
	if request.method=="POST":

		frm=FlowerForm(request.POST)
		sl=request.POST['sl']
		sw=request.POST['sw']
		pl=request.POST['pl']
		pw=request.POST['pw']
		data=pd.read_csv('iris.csv',names=['sl','sw','pl','pw','type'])
		x=data.iloc[:,0:4]
		y=data['type']
		x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=.2,random_state=12)
		knn=KNeighborsClassifier(n_neighbors=7)
		knn.fit(x_train,y_train)
		test=[[sl,sw,pl,pw]]
		testdata=pd.DataFrame(test)
		prediction=knn.predict(testdata)
		return render(request,'predict.html',{'p':prediction})
	else:
		frm=FlowerForm()


	return render(request,'abc.html',{'e':frm})

