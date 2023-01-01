#!/usr/bin/env python
# coding: utf-8

# In[23]:


import findspark
findspark.init()


# In[26]:


import pyspark
from pyspark.sql import SparkSession
spark=SparkSession.builder.master("spark://pop-os.localdomain:7077").appName('Pi-Estimation').getOrCreate()


# In[21]:


import random
NUM_SAMPLES=1

def inside(p):
    x, y = random.random(), random.random()
    return x**2 + y**2 < 1

count = (
    spark.sparkContext('Pi-Example')
    .parallelize(range(NUM_SAMPLES))
    .filter(inside)
    .count()
)
print(f"Pi is roughly {4.0 * count / NUM_SAMPLES}")


# In[27]:


spark.stop()


# In[ ]:




