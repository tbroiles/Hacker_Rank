
from numpy.random import normal as rnormal
from numpy import array, arange, sin, cos, pi, identity, matmul, zeros, cov
from numpy.linalg import inv
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

del_t = 0.1

t = arange(0, 1000, del_t)

x = .002*t + rnormal(0,.5,10000)
y = .0000003*(t-500)**3 + rnormal(0,.5,10000)
z = 4*sin(pi*t/1000) + rnormal(0,.5, 10000)

xt = .002*t
yt = .0000003*(t-500)**3
zt = 4*sin(pi*t/1000) 

v_x = array([(x[i] - x[i-1])/del_t for i in xrange(1,len(x))]+[(x[-1]-x[-2])/del_t])
v_y = array([(y[i] - y[i-1])/del_t for i in xrange(1,len(y))]+[(y[-1]-y[-2])/del_t])
v_z = array([(z[i] - z[i-1])/del_t for i in xrange(1,len(z))]+[(z[-1]-z[-2])/del_t])

X = array([x,v_x])
Y = array([y,v_y])
Z = array([z,v_z])

F = array([[1,del_t],[0,1]])
G = array([[del_t**2/2], [del_t]])
Q = matmul(G, G.transpose())*.5**2
Px = identity(2)*5
Py = identity(2)*5
Pz = identity(2)*5
H = array([1,0])
Rx = cov(X)
Ry = cov(Y)
Rz = cov(Z)


f_xobs = zeros((2,10000))
f_yobs = zeros((2,10000))
f_zobs = zeros((2,10000))
f_xobs[:,0] = X[:,0]
f_yobs[:,0] = Y[:,0]
f_zobs[:,0] = Z[:,0]

for i in xrange(1, len(x)):
    P_xminus = matmul(matmul(F,Px), F.T) + Q
    S = matmul(matmul(H,P_xminus),H.T) + Rx
    K = matmul(matmul(P_xminus, H.T), inv(S))
    f_xobs[:,i] = f_xobs[:,i-1] + matmul(K, (X[:,i]-matmul(H,f_xobs[:,i-1])))
    Px = matmul(matmul(identity(2)-matmul(K,H), P_xminus), (identity(2)-matmul(K,H)).T) + matmul(matmul(K,Rx),K.T)

    P_yminus = matmul(matmul(F,Py), F.T) + Q
    S = matmul(matmul(H,P_yminus),H.T) + Ry
    f_yobs[:,i] = f_yobs[:,i-1] + matmul(K, (Y[:,i]-matmul(H,f_yobs[:,i-1])))
    Py = matmul(matmul(identity(2)-matmul(K,H), P_yminus), (identity(2)-matmul(K,H)).T) + matmul(matmul(K,Ry),K.T)

    P_zminus = matmul(matmul(F,Pz), F.T) + Q
    S = matmul(matmul(H,P_zminus),H.T) + Rz
    K = matmul(matmul(P_zminus, H.T), inv(S))
    f_zobs[:,i] = f_zobs[:,i-1] + matmul(K, (Z[:,i]-matmul(H,f_zobs[:,i-1])))
    Pz = matmul(matmul(identity(2)-matmul(K,H), P_zminus), (identity(2)-matmul(K,H)).T) + matmul(matmul(K,Rz),K.T)


fig = plt.figure()
ax = fig.gca(projection = '3d')


ax.plot(X[0,:], Y[0,:], Z[0,:], 'k.')
ax.plot(f_xobs[0,:], f_yobs[0,:], f_zobs[0,:], 'r-')
ax.plot(xt,yt,zt, 'b-.', linewidth = 2)
plt.show()
