import tkinter as tk
from tkinter.filedialog import askopenfilename
import sys
import subprocess
import pandas as pd
import numpy as np
from sklearn import preprocessing, neighbors
import matplotlib.pyplot as plt
from tkinter import ttk


window = tk.Tk()
window.title("ml_project")
window.geometry("200x100")
window.configure(background='gray19')

#canvas in tkinter
canvas = tk.Canvas(window, width=201, height=201,bg="gray")



def OpenFile():
	file1= open("file1","w+")
	name = askopenfilename(initialdir="C:/Users/Batman/Documents/Programming/tkinter/",
                           filetypes =(("Text File", "*.txt"),("All Files","*.*")),
                           title = "Choose a file."
                           )
	print (name)
	file1.write(name)
	file1.close()


def predictor():
	subprocess.call ("./try.R")
	file2= open("out","r")
	buf1=file2.read()
	file2.close()
	print(buf1)
	a=[float(x) for x in buf1.split()]
	#print(a)


	df = pd.read_csv('voice.csv')

	df = df.rename(columns={'label': 'gender'})


	#Lets use SVM:
	#Bootstrapping

	df1=df[['meanfun','IQR','Q25','sp.ent','sd','sfm','meanfreq','gender']]
	#Producing X and y
	X = df1.drop(['gender'], 1)
	y = df1['gender']

	from sklearn.preprocessing import LabelEncoder
	labelencoder1 = LabelEncoder()
	y = labelencoder1.fit_transform(y)

	#Dividing the data randomly into training and test set
	from sklearn.cross_validation import ShuffleSplit
	rs =ShuffleSplit(n=3168,n_iter=30,train_size=.8,test_size=.2, random_state=0)

	for train_index, test_index in rs:
		X_train, X_test = X.iloc[train_index], X.iloc[test_index]
		y_train, y_test = y[train_index], y[test_index]

	from sklearn.preprocessing import StandardScaler
	sc = StandardScaler()
	X_train = sc.fit_transform(X_train)
	X_test = sc.transform(X_test)


	from sklearn.svm import SVC
	from sklearn import svm
	classifier = SVC(kernel = 'linear', random_state=10, gamma='auto')
	classifier.fit(X_train, y_train)

	a=np.array(a).reshape(1, -1)
	a = sc.transform(a)

	y_pred=classifier.predict(a)
	y_score = classifier.fit(X_train, y_train).decision_function(X_test)
	if y_pred[0]==0:print("Female")
	else:print("Male")


#creating frame to put the direction buttons
f = tk.Frame(window, width=200, height=400,bg="gray19")
f.pack(side=tk.LEFT)



#c1 = tk.Button(f, text="BROWSE",command=lambda : OpenFile).pack(padx="10", pady="10",side=tk.RIGHT)
c2 = tk.Button(f,text="Predict",command=predictor).pack(padx="10", pady="10",side=tk.LEFT)
c1 = tk.Button(f, text="BROWSE",command=lambda : OpenFile()).pack(padx="10", pady="10",side=tk.RIGHT)

window.mainloop()
