from mpl_toolkits import mplot3d
import numpy as np 
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import mpl_toolkits.mplot3d.axes3d as p3
fig = plt.figure()
ax = p3.Axes3D(fig)
 #setup polar coordinates
CONTRACTION_FACTOR = 0.3 #how much does the arm move inward 
ARM_LENGTH = 15#mm
ARM_RAD = CONTRACTION_FACTOR*ARM_LENGTH
#Draw the range of motion ellipsoid
draw_ROME = True

#Draw the starting position (0,0)
draw_ORIGIN = True


#The control inputs for now are theta and rho (spherical coordinates)
    #note these will need to be remapped later to be in terms of motor drives

#convert a vector from the two inputs to x,y,z
def findVector(theta,rho):
    x = ARM_RAD*np.cos(theta)*np.sin(rho)
    y = ARM_RAD*np.sin(theta)*np.sin(rho)
    z = ARM_LENGTH*np.cos(rho)
    return x,y,z

#create a bezier curve that resembles the true position of the arm
def quadBez(p2,p3,t):
    x = 2*t*(1-t)*p2[0] + t**(2)*p3[0]
    y = 2*t*(1-t)*p2[1] + t**(2)*p3[1]
    return x,y

#Draw the bezier'd arm into position given the inputs
def moveArm(theta,rho,draw_Vector = False):
    xp,yp,zp = findVector(theta,rho)
    radius = np.sqrt(xp**2 + yp**2)
    r_feed = np.linspace(0,1,10)
    r,z_r = quadBez((0,zp),(radius,zp),r_feed)
    x_r = r*np.cos(theta)
    y_r = r*np.sin(theta)
    if draw_Vector:
        ax.quiver(0,0,0,xp,yp,zp,color='orange',arrow_length_ratio=0.1)
    return x_r,y_r,z_r


theta_feed = np.linspace(0,2*np.pi,30)
rho_feed = np.linspace(0,np.pi/3,30)
for i in theta_feed:
    for j in rho_feed:
        x,y,z = moveArm(i,j)
        ax.plot3D(x,y,z,color = 'black',linewidth = 3)
        if draw_ORIGIN:
            zline = np.linspace(0, ARM_LENGTH, 10)
            xline = zline*0
            yline = zline*0
            ax.plot3D(xline, yline, zline, 'r', linewidth=3)
        if draw_ROME:
            theta,rho = np.mgrid[0:2*np.pi:30j,0:np.pi/2:30j]
            x = ARM_RAD*np.cos(theta)*np.sin(rho)
            y = ARM_RAD*np.sin(theta)*np.sin(rho)
            z = ARM_LENGTH*np.cos(rho) 
            ax.plot_wireframe(x,y,z,color='b',linewidth=0.2)
        plt.pause(0.1)
        plt.cla()
plt.show()

