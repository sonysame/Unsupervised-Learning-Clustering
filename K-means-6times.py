import numpy as np
import matplotlib.pyplot as plt

def show_prm(x,r,mu,col):
	for k in range(K):
		plt.plot(x[r[:,k]==1,0], x[r[:,k]==1,1], marker='o', markerfacecolor=X_col[k], markeredgecolor='k', markersize=6, alpha=0.5, linestyle='none')
		plt.plot(mu[k,0], mu[k,1], marker='*', markerfacecolor=X_col[k], markeredgecolor='k', markersize=15, markeredgewidth=1)
	plt.xlim(X_range0)
	plt.ylim(X_range1)
	plt.grid(True)

def step1_kmeans(x0,x1,mu):
	N=len(x0)
	r=np.zeros((N,K))
	for n in range(N):
		wk=np.zeros(K)
		for k in range(K):
			wk[k]=(x0[n]-mu[k,0])**2+(x1[n]-mu[k,1])**2
		r[n,np.argmin(wk)]=1
	return r

def step2_kmeans(x0,x1,r):
	mu=np.zeros((K,2))
	for k in range(K):
		mu[k,0]=np.sum(r[:,k]*x0)/np.sum(r[:,k])
		mu[k,1]=np.sum(r[:,k]*x1)/np.sum(r[:,k])
	return mu


np.random.seed(1)
N=100
K=3
outfile=np.load('data_ch9.npz')

X=outfile['X']
X_range0=outfile['X_range0']
X_range1=outfile['X_range1']
X_col=['cornflowerblue','black','white']

Mu=np.array([[-2,1],[-2,0],[-2,-1]])
R=np.c_[np.ones((N,1),dtype=int), np.zeros((N,2),dtype=int)]

max_it=9
plt.figure(figsize=(8,12))
for it in range(0,max_it):
	plt.subplot(3,3, it+1)
	R=step1_kmeans(X[:,0], X[:,1], Mu)
	show_prm(X,R,Mu,X_col)
	plt.title("{0:d}".format(it+1))
	plt.xticks(range(X_range0[0], X_range0[1]), "")
	plt.yticks(range(X_range1[0], X_range1[1]), "")
	Mu=step2_kmeans(X[:,0], X[:,1], R)
plt.show()