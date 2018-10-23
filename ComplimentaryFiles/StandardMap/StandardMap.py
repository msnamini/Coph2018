
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')


# In[2]:


def logistic(r, x):
    return r * x * (1 - x)


# In[3]:


x = np.arange(0, 1.02,0.02)
plt.plot(x, logistic(2, x), 'b')
plt.show()


# In[10]:


def plot_map(r, x0, n):
    t = np.linspace(0, 1)
    plt.plot(t, logistic(r, t), 'k', lw=2)
    plt.plot([0, 1], [0, 1], 'k', lw=2)
    x = x0
    for i in range(n):
        y = logistic(r, x)
        plt.plot([x, x], [x, y], 'k', lw=1)
        plt.plot([x, y], [y, y], 'k', lw=1)
        plt.plot([x], [y], 'ok', ms=10, alpha=(i + 1) / n)
        x = y
        
plot_map(2.5, .1, 10)


# In[11]:


plot_map(3.9, .1, 80)


# In[6]:


n = 10000
r = np.linspace(2.5, 4.0, n)


# In[7]:


iterations = 1000
last = 100


# In[8]:


x = 1e-5 * np.ones(n)
lyapunov = np.zeros(n)


# In[9]:


for i in range(iterations):
    x = logistic(r, x)
    if i >= (iterations - last):
        plt.plot(r, x, ',k',alpha=0.25)

