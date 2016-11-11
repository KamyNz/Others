
# coding: utf-8

# In[1]:

get_ipython().magic(u'pylab inline')


# In[96]:

a=10.
b=10.
c=10.
d=10.
e=10.
f=10.
for i in range(100000):
    a_new=0.55*e+0.3*b
    b_new=0.
    c_new=0.3*b
    d_new=0.4*b+0.6*c+f
    e_new=0.1*a+0.4*c+d
    f_new=0.45*e+0.9*a
    a=a_new
    b=b_new
    c=c_new
    d=d_new
    e=e_new
    f=f_new


# In[97]:

print a,b,c,d,e,f


# In[32]:

print a+b+c+d+e+f


# In[92]:

a=10.
b=10.
c=10.
d=10.
e=10.
f=10.
a_list=[]
b_list=[]
c_list=[]
d_list=[]
e_list=[]
f_list=[]
step=[]
for i in range(25):
    a_new=0.55*e+0.3*b
    b_new=0.
    c_new=0.3*b
    d_new=0.4*b+0.6*c+f
    e_new=0.1*a+0.4*c+d
    f_new=0.45*e+0.9*a
    a_list.append(a)
    b_list.append(b)
    c_list.append(c)
    d_list.append(d)
    e_list.append(e)
    f_list.append(f)
    step.append(i)
    a=a_new
    b=b_new
    c=c_new
    d=d_new
    e=e_new
    f=f_new


# In[113]:

lab=["a","b","c","d","e","f"]
figure(figsize=(10, 5))
title('Valor para cada nodo por paso', y=-0.1)
plot(step,a_list,label=lab[0],linewidth=2.0)
plot(step,b_list,label=lab[1],linewidth=2.0)
plot(step,c_list,label=lab[2],linewidth=2.0)
plot(step,d_list,label=lab[3],linewidth=2.0)
plot(step,e_list,label=lab[4],linewidth=2.0)
plot(step,f_list,label=lab[5],linewidth=2.0)
legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3, ncol=6, mode="expand", borderaxespad=0.)
savefig('nodos.png', dpi=100)


# In[ ]:




# In[ ]:



