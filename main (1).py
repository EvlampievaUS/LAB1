import math
L=0.37
m=[0.004, 0.00299, 0.00188]
t=[[1.797, 1.727, 1.703, 1.734, 1.713, 1.729, 1.724, 1.715, 1.735, 1.725],
   [2.188, 2.209, 2.195, 2.190, 2.191, 2.200, 2.227, 2.203, 2.198, 2.201],
   [2.950, 2.958, 2.884, 2.955, 2.911, 2.919, 2.943, 2.955, 2.922, 2.874]]
a=[]
a_sr=[]
t_sr=[]
t_ot=0.0002
t_ab=[]
L_ab=0.001
a_ot=[]
a_ab=[]
M=0.0683
g_pr=[]
m0=42/10**5
g=9.8
l=8.23/10**6
r=0.0415
e=[]
g_sr=0.
g_ab=[]
g_sr_ab=0.
g_sr_ot=0.
######################################################################################
for i in range(len(t)):
    a.append([])
    for k in t[i]:
        a[i].append(2*L/k**2)
for i in a:
    a_sr.append(sum(i)/len(i))
for i in t:
    t_sr.append(sum(i)/len(i))
for i in t_sr:
    t_ab.append(t_ot*i)
for i in range(len(t_sr)):
    a_ot.append(((L_ab/L)**2+
                (2*t_ab[i]/t_sr[i])**2)**0.5)
for i in range(len(a_ot)):
    a_ab.append(a_ot[i]*a_sr[i])
for i in range(len(a_sr)):
    g_pr.append(((2*M+m[i])/m[i])*a_sr[i])
for i in range(len(a_sr)):
    e.append(l*a_sr[i]/(m[i]*r**2)+m0*g/m[i])
for i in range(len(g_pr)):
    g_pr[i]+=e[i]
g_sr=sum(g_pr)/len(g_pr)
for i in range(len(a_ot)):
    g_ab.append(a_ot[i]*g_pr[i])
g_sr_ab=sum(g_ab)/len(g_ab)
g_sr_ot=g_sr_ab/g_sr
print('Ускорение свободного падения =', g_sr, '+-', g_sr_ab)
######################################################################################