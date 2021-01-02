import numpy as np
import matplotlib.pyplot as plt

def gauss(x, mu, sigma):
	N,D=x.shape
	c1=1/(2*np.pi)**(D/2)
	c2=1/(np.linalg.det(sigma)**(1/2))
	inv_sigma=np.linalg.inv(sigma)
	c3=x-mu
	c4=np.dot(c3, inv_sigma)
	c5=np.zeros(N)
	for d in range(D):
		c5=c5+c4[:,d]*c3[:,d]
	p=c1*c2*np.exp(-c5/2)
	return p

def mixgauss(x,pi,mu,sigma):
	N,D=x.shape
	K=len(pi)
	p=np.zeros(N)
	for k in range(K):
		p=p+pi[k]*gauss(x,mu[k,:], sigma[k,:,:])
	return p

def show_contour_mixgauss(pi, mu, sigma):
	xn=40
	x0=np.linspace(X_range0[0], X_range0[1], xn)
	x1=np.linspace(X_range1[0], X_range1[1], xn)
	xx0,xx1=np.meshgrid(x0,x1)
	x=np.c_[np.reshape(xx0,(xn*xn,1)), np.reshape(xx1, (xn*xn,1))]
	f=mixgauss(x,pi, mu, sigma)
	f=f.reshape(xn,xn)
	cont=plt.contour(xx0,xx1,f,10,colors='gray')
	cont.clabel(fmt='%3.2f', fontsize=8)

def show3d_mixgauss(ax, pi, mu, sigma):
	xn=40
	x0=np.linspace(X_range0[0], X_range0[1], xn)
	x1=np.linspace(X_range1[0], X_range1[1], xn)
	xx0,xx1=np.meshgrid(x0,x1)
	x=np.c_[np.reshape(xx0,(xn*xn,1)), np.reshape(xx1,(xn*xn,1))]
	f=mixgauss(x,pi,mu,sigma)
	f=f.reshape(xn,xn)
	ax.plot_surface(xx0,xx1,f,rstride=2,cstride=2,alpha=0.3,color='blue', edgecolor='black')

np.random.seed(1)
N=100
K=3
outfile=np.load('data_ch9.npz')

X_range0=outfile['X_range0']
X_range1=outfile['X_range1']
X_col=['cornflowerblue','black','white']

x=np.array([[1,2],[2,1],[3,4]])
pi=np.array([0.2,0.4,0.4])
mu=np.array([[-2,-2],[-1,1],[1.5,1]])
sigma=np.array([[[.5,0],[0,.5]],[[1,0.25],[0.25,.5]],[[.5,0],[0,.5]]])

plt.figure(1,figsize=(8.3,5))
plt.subplot(1,2,1)
show_contour_mixgauss(pi,mu,sigma)
plt.grid(True)

Ax=plt.subplot(1,2,2, projection='3d')
show3d_mixgauss(Ax,pi,mu,sigma)
Ax.set_zticks([0.05,0.10])
Ax.set_xlabel('$x_0$',fontsize=14)
Ax.set_ylabel('$x_1$',fontsize=14)
Ax.view_init(40,-100)
plt.xlim(X_range0)
plt.ylim(X_range1)
plt.show()