import numpy as np
import matplotlib.pyplot as plt

def distortion_measure(x0,x1,r,mu):
	N=len(x0)
	J=0
	for n in range(N):
		for k in range(K):
			J=J+r[n,k]*((x0[n]-mu[k,0])**2+(x1[n]-mu[k,1])**2)
	return J

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

max_it=10
DM=np.zeros(max_it)
for it in range(0,max_it):
	R=step1_kmeans(X[:,0], X[:,1], Mu)
	DM[it]=distortion_measure(X[:,0], X[:,1], R, Mu)
	Mu=step2_kmeans(X[:,0], X[:,1], R)
print(np.round(DM,2))
plt.figure(1, figsize=(4,4))
plt.plot(DM, color='black', linestyle='-', marker='o')
plt.ylim(40, 80)
plt.grid(True)
plt.title("Distortion Measure")
plt.show()