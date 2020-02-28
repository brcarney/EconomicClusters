#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# # Import data

# In[2]:


raw = pd.read_csv(r"G:\My Drive\BCarney\DataAnalysis\CBP_2017\NAICS_AllDigits\rawdata\cbp17co.txt")
raw


# # Select 6-Digit NAICS

# In[3]:


sixdigit = raw[~((raw['naics'].str.contains('/', na=False)) | (raw['naics'].str.contains('-', na=False)))]
sixdigit  


# # Select NJ (34) and PA (42)

# In[5]:


regionstates = sixdigit[(sixdigit['fipstate'] == 34) | (sixdigit['fipstate'] == 42)]
regionstates


# # Select respective counties for NJ and PA

# In[6]:


region_NAICS = regionstates.loc[((regionstates['fipstate'] == 34) & ((regionstates['fipscty'] == 5) | (regionstates['fipscty'] == 7) | (regionstates['fipscty'] == 15) | (regionstates['fipscty'] == 21))) |  ((regionstates['fipstate'] == 42) & ((regionstates['fipscty'] == 17) | (regionstates['fipscty'] == 29) | (regionstates['fipscty'] == 45) | (regionstates['fipscty'] == 91) | (regionstates['fipscty'] == 101)))]
region_NAICS


# In[7]:


region_NAICS.to_csv(r"G:\My Drive\BCarney\DataAnalysis\CBP_2017\NAICS_AllDigits\DVRPC_region\region_NAICS.csv", index=0)


# In[8]:


ninecountyregion = region_NAICS[['naics', 'emp' ]]
ninecountyregion


# # Calculate total employment for each 6-digit NAICS via groupby

# In[10]:


ninecountyregion_sum = ninecountyregion.groupby(['naics']).sum()
ninecountyregion_sum.to_csv(r"G:\My Drive\BCarney\DataAnalysis\CBP_2017\NAICS_AllDigits\DVRPC_region\region_NAICStotal.csv")
ninecountyregion_sum

