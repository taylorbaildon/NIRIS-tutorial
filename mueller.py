import numpy as np
import matplotlib.pyplot as plt

# normal incidence
def ideal_mirror():
    mirror = np.array([
        [1, 0,  0,  0],
        [0, 1,  0,  0],
        [0, 0, -1,  0],
        [0, 0,  0, -1]
    ])
    return mirror

# input theta in degrees
# theta - orientation of transmission axis
def linear_polarizer(theta):
    theta_radians = np.radians(theta)
    cos_2theta = np.cos(2*theta_radians)
    sin_2theta = np.sin(2*theta_radians)
    if np.size(theta) == 1:
        polarizer = 0.5*np.array([
            [1,          cos_2theta,            sin_2theta,            0],
            [cos_2theta, cos_2theta**2,         cos_2theta*sin_2theta, 0],
            [sin_2theta, cos_2theta*sin_2theta, sin_2theta**2,         0],
            [0, 0, 0, 0]      
        ])
    else:
        polarizer = []
        for i in range(len(theta)):
            polarizer_i = 0.5*np.array([
                [1,          cos_2theta[i],            sin_2theta[i],            0],
                [cos_2theta[i], cos_2theta[i]**2,         cos_2theta[i]*sin_2theta[i], 0],
                [sin_2theta[i], cos_2theta[i]*sin_2theta[i], sin_2theta[i]**2,         0],
                [0, 0, 0, 0]      
            ])
            polarizer.append(polarizer_i)
        polarizer = np.array(polarizer)
    return polarizer


# input alpha in degrees
# alpha - rotation angle
def rotator(alpha):
    alpha_radians = np.radians(alpha)
    cos_2alpha = np.cos(2*alpha_radians)
    sin_2alpha = np.sin(2*alpha_radians)
    if np.size(alpha) == 1:
        rotator = np.array([
            [1, 0, 0, 0],
            [0,  cos_2alpha, sin_2alpha, 0],
            [0, -sin_2alpha, cos_2alpha, 0],
            [0, 0, 0, 1]
        ])
    else:
        rotator = []
        for i in range(len(alpha)):
            rotator_i = np.array([
                [1, 0, 0, 0],
                [0,  cos_2alpha[i], sin_2alpha[i], 0],
                [0, -sin_2alpha[i], cos_2alpha[i], 0],
                [0, 0, 0, 1]
            ])
            rotator.append(rotator_i)
        rotator = np.array(rotator)
    return rotator

# input delta and theta in degrees
# delta - phase difference between fast and slow axis (retardation)
# theta - angle (orientation) of fast axis
def retarder(delta, theta):
    delta_radians = np.radians(delta)
    theta_radians = np.radians(theta)
    cos_2theta = np.cos(2 * theta_radians)
    sin_2theta = np.sin(2 * theta_radians)
    cos_del = np.cos(delta_radians)
    sin_del = np.sin(delta_radians)
    if np.size(theta) == 1:
        retarder = np.array([
            [1, 0, 0, 0],
            [0,  cos_2theta**2 + sin_2theta**2*cos_del,  cos_2theta*sin_2theta*(1 - cos_del),      sin_2theta*sin_del],
            [0,  cos_2theta*sin_2theta*(1 - cos_del),    sin_2theta**2 + cos_2theta**2*cos_del,   -cos_2theta*sin_del],
            [0, -sin_2theta*sin_del,                     cos_2theta*sin_del,                       cos_del]
        ])
    else:
        retarder = []
        for i in range(len(theta)):
            retarder_i = np.array([
                [1, 0, 0, 0],
                [0,  cos_2theta[i]**2 + sin_2theta[i]**2*cos_del,  cos_2theta[i]*sin_2theta[i]*(1 - cos_del),      sin_2theta[i]*sin_del],
                [0,  cos_2theta[i]*sin_2theta[i]*(1 - cos_del),    sin_2theta[i]**2 + cos_2theta[i]**2*cos_del,   -cos_2theta[i]*sin_del],
                [0, -sin_2theta[i]*sin_del,                     cos_2theta[i]*sin_del,                       cos_del]
            ])
            retarder.append(retarder_i)
        retarder = np.array(retarder)
    return retarder


# input delta and theta in degrees
# S - Stokes vector, format np.array([I,Q,U,V])
# delta - retardation of modulator
# theta - angular position of modulator's fast axis
def modulated_output(S,delta,theta):
    delta_radians = np.radians(delta)
    theta_radians = np.radians(theta)
    cos_4theta = np.cos(4*theta_radians)
    sin_4theta = np.sin(4*theta_radians)
    sin_2theta = np.sin(2*theta_radians)
    cos_del = np.cos(delta_radians)
    sin_del = np.sin(delta_radians)
    modulated_signal = 0.5*np.array((S[0] 
                            + 0.5*S[1]*((1+cos_del)+(1-cos_del)*cos_4theta) 
                            + 0.5*S[2]*(1-cos_del)*sin_4theta 
                            + S[3]*sin_del*sin_2theta))
    return modulated_signal

def plt_signal(S, theta):
    plt.figure(figsize=(10,8))
    plt.plot(theta,S, linewidth=2, color='black')
    plt.axvline(x=22.5)
    plt.fill_between(theta[:45], S[:45], -1, color='gray', alpha=.2)
    plt.axvline(x=45)
    plt.fill_between(theta[45:90], S[45:90], -1, color='red', alpha=.2)
    plt.axvline(x=67.5)
    plt.fill_between(theta[90:135], S[90:135], -1, color='orange', alpha=.2)
    plt.axvline(x=90)
    plt.fill_between(theta[135:180], S[135:180], -1, color='yellow', alpha=.2)
    plt.axvline(x=112.5)
    plt.fill_between(theta[180:225], S[180:225], -1, color='green', alpha=.2)
    plt.axvline(x=135)
    plt.fill_between(theta[225:270], S[225:270], -1, color='blue', alpha=.2)
    plt.axvline(x=157.5)
    plt.fill_between(theta[270:315], S[270:315], -1, color='indigo', alpha=.2)
    plt.ylim(-1,1)
    plt.fill_between(theta[315:], S[315:], -1, color='violet', alpha=.2)
    plt.xlim(0,180)
    plt.xlabel('Modulator angle (degrees)')
    plt.show()
    
def polarization_degree(S):
    return np.sqrt((S[1]**2 + S[2]**2 + S[3]**2)/(S[0]**2))
        




