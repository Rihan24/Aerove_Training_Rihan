import numpy as np


y=np.random.randint(1,101,20,dtype="int32")  #create array y with random 20 numbers

X=np.random.normal(size=(20,20))   #create random normalized matrix X of size(20,20)

X_trnsp=X.transpose()

A=np.linalg.inv(np.matmul(X_trnsp,X))
theta=np.matmul((np.matmul(A,X_trnsp)),y)  #compute matrix theta
print(theta)
