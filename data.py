import numpy as np
import matplotlib.pyplot as plt

np.random.seed(1)
N=100
K=3
T3=np.zeros((N,3), dtype=np.uint8)
X=np.zeros((N,2))
X_range0=[-3,3]
X_range1=[-3,3]
X_col=['cornflowerblue','black','white']
Mu=np.array([[-.5,-.5], [.5,1.0],[1,-.5]])
Sig=np.array([[.7,.7],[.8,.3],[.3,.8]])
Pi=np.array([0.4,0.8,1])
for n in range(N):
	wk=np.random.rand()
	for k in range(K):
		if wk < Pi[k]:
			T3[n,k]=1
			break
	for k in range(2):
		X[n,k]=(np.random.randn()*Sig[T3[n,:]==1,k]+Mu[T3[n,:]==1,k])

def show_data(x):
	plt.plot(x[:,0],x[:,1], linestyle='none', marker='o', markersize=6, markeredgecolor='black', color='gray', alpha=0.8)
	plt.grid(True)


plt.figure(1,figsize=(4,4))
show_data(X)
plt.xlim(X_range0)
plt.ylim(X_range1)
plt.show()
np.savez('data_ch9.npz', X=X, X_range0=X_range0, X_range1=X_range1)