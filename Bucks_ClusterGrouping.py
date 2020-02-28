#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# # Import data

# In[2]:


raw = pd.read_csv(r"G:\My Drive\BCarney\DataAnalysis\CBP_2017\NAICS_AllDigits\rawdata\cbp17co.txt")
raw


# # Select 6-digit NAICS

# In[3]:


sixdigit = raw[~((raw['naics'].str.contains('/', na=False)) | (raw['naics'].str.contains('-', na=False)))]
sixdigit


# # Select Bucks County

# In[5]:


Bucks_full = sixdigit.loc[(sixdigit['fipstate'] == 42) & (sixdigit['fipscty'] == 17)]
Bucks_full


# In[6]:


Bucks = Bucks_full[['naics', 'emp' ]]
Bucks


# In[7]:


Bucks['naics'].astype(str)
Bucks


# # Cluster Grouping

# In[8]:


Bucks = Bucks.assign(cluster= 0)

Bucks.loc[(Bucks['naics'] == '336411') |
                (Bucks['naics'] == '336412') |
                (Bucks['naics'] == '336413') |
                (Bucks['naics'] == '336414') |
                (Bucks['naics'] == '336415') |
                (Bucks['naics'] == '336419') |
                (Bucks['naics'] == '334511') 
                , 'cluster'] = 1

#Agricultural Inputs and Services
Bucks.loc[(Bucks['naics'] == '115111') |
                (Bucks['naics'] == '115112') |
                (Bucks['naics'] == '115113') |
                (Bucks['naics'] == '115114') |
                (Bucks['naics'] == '115210') |
                (Bucks['naics'] == '115115') |
                (Bucks['naics'] == '115116') |
                (Bucks['naics'] == '325311') |
                (Bucks['naics'] == '325314') 
                , 'cluster'] = 2

#Apparel
Bucks.loc[(Bucks['naics'] == '314999') |
                (Bucks['naics'] == '315292') |
                (Bucks['naics'] == '315299') |
                (Bucks['naics'] == '315991') |
                (Bucks['naics'] == '315992') |
                (Bucks['naics'] == '315993') |
                (Bucks['naics'] == '315999') |
                (Bucks['naics'] == '315221') |
                (Bucks['naics'] == '315222') |
                (Bucks['naics'] == '315223') |
                (Bucks['naics'] == '315224') |
                (Bucks['naics'] == '315225') |
                (Bucks['naics'] == '315228') |
                (Bucks['naics'] == '315231') |
                (Bucks['naics'] == '315232') |
                (Bucks['naics'] == '315233') |
                (Bucks['naics'] == '315234') |
                (Bucks['naics'] == '315239') |
                (Bucks['naics'] == '315291') |
                (Bucks['naics'] == '315211') |
                (Bucks['naics'] == '315212') 
                , 'cluster'] = 3

#Automotive
Bucks.loc[(Bucks['naics'] == '332114') |
                (Bucks['naics'] == '336321') |
                (Bucks['naics'] == '336322') |
                (Bucks['naics'] == '336330') |
                (Bucks['naics'] == '336340') |
                (Bucks['naics'] == '336350') |
                (Bucks['naics'] == '336360') |
                (Bucks['naics'] == '336391') |
                (Bucks['naics'] == '336399') |
                (Bucks['naics'] == '336311') |
                (Bucks['naics'] == '336312') |
                (Bucks['naics'] == '336111') |
                (Bucks['naics'] == '336112') |
                (Bucks['naics'] == '336120') |
                (Bucks['naics'] == '336211') |
                (Bucks['naics'] == '336370') |
                (Bucks['naics'] == '336999') |
                (Bucks['naics'] == '336992') |
                (Bucks['naics'] == '331511') |
                (Bucks['naics'] == '331512') |
                (Bucks['naics'] == '331513') |
                (Bucks['naics'] == '331521') |
                (Bucks['naics'] == '331522') |
                (Bucks['naics'] == '331524') |
                (Bucks['naics'] == '331525') |
                (Bucks['naics'] == '331528') 
                , 'cluster'] = 4

#BioPharmaceuticals
Bucks.loc[(Bucks['naics'] == '325411') |
                (Bucks['naics'] == '325412') |
                (Bucks['naics'] == '325414') |
                (Bucks['naics'] == '325413')
                , 'cluster'] = 5

#Business Services
Bucks.loc[(Bucks['naics'] == '551111') |
                (Bucks['naics'] == '551112') |
                (Bucks['naics'] == '551114') |
                (Bucks['naics'] == '541611') |
                (Bucks['naics'] == '541612') |
                (Bucks['naics'] == '541614') |
                (Bucks['naics'] == '541618') |
                (Bucks['naics'] == '541690') |
                (Bucks['naics'] == '533110') |
                (Bucks['naics'] == '541199') |
                (Bucks['naics'] == '541214') |
                (Bucks['naics'] == '541930') |
                (Bucks['naics'] == '541990') |
                (Bucks['naics'] == '561210') |
                (Bucks['naics'] == '561330') |
                (Bucks['naics'] == '561421') |
                (Bucks['naics'] == '561422') |
                (Bucks['naics'] == '561920') |
                (Bucks['naics'] == '518210') |
                (Bucks['naics'] == '541511') |
                (Bucks['naics'] == '541512') |
                (Bucks['naics'] == '541513') |
                (Bucks['naics'] == '541519') |
                (Bucks['naics'] == '561311') |
                (Bucks['naics'] == '561312') |
                (Bucks['naics'] == '541330') |
                (Bucks['naics'] == '541310') |
                (Bucks['naics'] == '541320') |
                (Bucks['naics'] == '541340') |
                (Bucks['naics'] == '485310') |
                (Bucks['naics'] == '485320') |
                (Bucks['naics'] == '485999') |
                (Bucks['naics'] == '532112') 
                , 'cluster'] = 6

#Coal Mining
Bucks.loc[(Bucks['naics'] == '212111') |
                (Bucks['naics'] == '212112') |
                (Bucks['naics'] == '212113') |
                (Bucks['naics'] == '213113')
                , 'cluster'] = 7

#Communications Equipment and Services
Bucks.loc[(Bucks['naics'] == '515210') |
                (Bucks['naics'] == '517210') |
                (Bucks['naics'] == '517410') |
                (Bucks['naics'] == '517919') |
                (Bucks['naics'] == '334210') |
                (Bucks['naics'] == '334220') |
                (Bucks['naics'] == '334290') |
                (Bucks['naics'] == '335912')
                , 'cluster'] = 8

#Construction Products and Services
Bucks.loc[(Bucks['naics'] == '236210') |
                (Bucks['naics'] == '237120') |
                (Bucks['naics'] == '237130') |
                (Bucks['naics'] == '237990') |
                (Bucks['naics'] == '221310') |
                (Bucks['naics'] == '221330') |
                (Bucks['naics'] == '332410') |
                (Bucks['naics'] == '332420') |
                (Bucks['naics'] == '332913') |
                (Bucks['naics'] == '332996') |
                (Bucks['naics'] == '327310') |
                (Bucks['naics'] == '327331') |
                (Bucks['naics'] == '327332') |
                (Bucks['naics'] == '327410') |
                (Bucks['naics'] == '327420') |
                (Bucks['naics'] == '327991') |
                (Bucks['naics'] == '327993') |
                (Bucks['naics'] == '327999') |
                (Bucks['naics'] == '324121') |
                (Bucks['naics'] == '324122') 
                , 'cluster'] = 9

#Distribution and Electronic Commerce
Bucks.loc[(Bucks['naics'] == '493110') |
                (Bucks['naics'] == '493120') |
                (Bucks['naics'] == '493190') |
                (Bucks['naics'] == '425110') |
                (Bucks['naics'] == '454111') |
                (Bucks['naics'] == '454112') |
                (Bucks['naics'] == '454113') |
                (Bucks['naics'] == '454110') |    #added due to 2017 NAICS change
                (Bucks['naics'] == '425120') |
                (Bucks['naics'] == '561499') |
                (Bucks['naics'] == '561910') |
                (Bucks['naics'] == '424310') |
                (Bucks['naics'] == '424320') |
                (Bucks['naics'] == '424330') |
                (Bucks['naics'] == '424340') |
                (Bucks['naics'] == '424920') |
                (Bucks['naics'] == '424610') |
                (Bucks['naics'] == '424690') |
                (Bucks['naics'] == '424210') |
                (Bucks['naics'] == '424590') |
                (Bucks['naics'] == '424910') |
                (Bucks['naics'] == '424930') |
                (Bucks['naics'] == '424940') |
                (Bucks['naics'] == '493130') |
                (Bucks['naics'] == '424440') |
                (Bucks['naics'] == '424460') |
                (Bucks['naics'] == '424470') |
                (Bucks['naics'] == '424480') |
                (Bucks['naics'] == '424820') |
                (Bucks['naics'] == '423210') |
                (Bucks['naics'] == '423220') |
                (Bucks['naics'] == '423940') |
                (Bucks['naics'] == '424110') |
                (Bucks['naics'] == '424120') |
                (Bucks['naics'] == '424130') |
                (Bucks['naics'] == '423910') |
                (Bucks['naics'] == '423920') |
                (Bucks['naics'] == '424950') |
                (Bucks['naics'] == '424990') |
                (Bucks['naics'] == '423820') |
                (Bucks['naics'] == '423810') |
                (Bucks['naics'] == '423830') |
                (Bucks['naics'] == '423840') |
                (Bucks['naics'] == '423850') |
                (Bucks['naics'] == '423860') |
                (Bucks['naics'] == '423410') |
                (Bucks['naics'] == '423420') |
                (Bucks['naics'] == '423430') |
                (Bucks['naics'] == '423440') |
                (Bucks['naics'] == '423450') |
                (Bucks['naics'] == '423460') |
                (Bucks['naics'] == '423490') |
                (Bucks['naics'] == '423610') |
                (Bucks['naics'] == '423620') |
                (Bucks['naics'] == '423690') |
                (Bucks['naics'] == '423510') |
                (Bucks['naics'] == '423520') |
                (Bucks['naics'] == '424710') |
                (Bucks['naics'] == '424720') |
                (Bucks['naics'] == '532411') |
                (Bucks['naics'] == '532412') |
                (Bucks['naics'] == '532420') |
                (Bucks['naics'] == '532490')
                , 'cluster'] = 10

#Downstream Chemical Products
Bucks.loc[(Bucks['naics'] == '325611') |
                (Bucks['naics'] == '325612') |
                (Bucks['naics'] == '325613') |
                (Bucks['naics'] == '325620') |
                (Bucks['naics'] == '325520') |
                (Bucks['naics'] == '325991') |
                (Bucks['naics'] == '325992') |
                (Bucks['naics'] == '325998') |
                (Bucks['naics'] == '325131') |
                (Bucks['naics'] == '325132') |
                (Bucks['naics'] == '325510') |
                (Bucks['naics'] == '325920') |
                (Bucks['naics'] == '324191')
                , 'cluster'] = 11

#Downstream Metal Products
Bucks.loc[(Bucks['naics'] == '332211') |
                (Bucks['naics'] == '332213') |
                (Bucks['naics'] == '332214') |
                (Bucks['naics'] == '332321') |
                (Bucks['naics'] == '332323') |
                (Bucks['naics'] == '332510') |
                (Bucks['naics'] == '332998') |
                (Bucks['naics'] == '332999') |
                (Bucks['naics'] == '332992') |
                (Bucks['naics'] == '332993') |
                (Bucks['naics'] == '332994') |
                (Bucks['naics'] == '332995') |
                (Bucks['naics'] == '332311') |
                (Bucks['naics'] == '332312') |
                (Bucks['naics'] == '332431') |
                (Bucks['naics'] == '332439')
                , 'cluster'] = 12

#Education and Knowledge Creation
Bucks.loc[(Bucks['naics'] == '611410') |
                (Bucks['naics'] == '611420') |
                (Bucks['naics'] == '611430') |
                (Bucks['naics'] == '611512') |
                (Bucks['naics'] == '611513') |
                (Bucks['naics'] == '611630') |
                (Bucks['naics'] == '611691') |
                (Bucks['naics'] == '611699') |
                (Bucks['naics'] == '611210') |
                (Bucks['naics'] == '611310') |
                (Bucks['naics'] == '611710') |
                (Bucks['naics'] == '541711') |
                (Bucks['naics'] == '541712') |
                (Bucks['naics'] == '541713') |  #added due to 2017 NAICS change
                (Bucks['naics'] == '541714') |  #added due to 2017 NAICS change
                (Bucks['naics'] == '541715') |  #added due to 2017 NAICS change
                (Bucks['naics'] == '541720') |
                (Bucks['naics'] == '813920') 
                , 'cluster'] = 13

#Electric Power Generation and Transmisison
Bucks.loc[(Bucks['naics'] == '221112') |
                (Bucks['naics'] == '221111') |
                (Bucks['naics'] == '221113') |
                (Bucks['naics'] == '221119') |
                (Bucks['naics'] == '221121')
                , 'cluster'] = 14

#Environmental Services
Bucks.loc[(Bucks['naics'] == '562112') |
                (Bucks['naics'] == '562119') |
                (Bucks['naics'] == '562211') |
                (Bucks['naics'] == '562213') |
                (Bucks['naics'] == '562219') |
                (Bucks['naics'] == '562920') |
                (Bucks['naics'] == '562998')
                , 'cluster'] = 15

#Financial Services
Bucks.loc[(Bucks['naics'] == '523910') |
                (Bucks['naics'] == '523920') |
                (Bucks['naics'] == '523930') |
                (Bucks['naics'] == '523991') |
                (Bucks['naics'] == '523999') |
                (Bucks['naics'] == '525910') |
                (Bucks['naics'] == '525990') |
                (Bucks['naics'] == '522120') |
                (Bucks['naics'] == '522190') |
                (Bucks['naics'] == '522210') |
                (Bucks['naics'] == '522220') |
                (Bucks['naics'] == '522291') |
                (Bucks['naics'] == '522292') |
                (Bucks['naics'] == '522293') |
                (Bucks['naics'] == '522294') |
                (Bucks['naics'] == '522298') |
                (Bucks['naics'] == '522320') |
                (Bucks['naics'] == '522390') |
                (Bucks['naics'] == '561450') |
                (Bucks['naics'] == '521110') |
                (Bucks['naics'] == '522310') |
                (Bucks['naics'] == '523110') |
                (Bucks['naics'] == '523120') |
                (Bucks['naics'] == '523130') |
                (Bucks['naics'] == '523140') |
                (Bucks['naics'] == '523210')
                , 'cluster'] = 16

#Fishing and Fishing Products
Bucks.loc[(Bucks['naics'] == '114111') |
                (Bucks['naics'] == '114112') |
                (Bucks['naics'] == '114119') |
                (Bucks['naics'] == '311711') |
                (Bucks['naics'] == '311712')
                , 'cluster'] = 17

#Food Processing and Manufacturing
Bucks.loc[(Bucks['naics'] == '311412') |
                (Bucks['naics'] == '311422') |
                (Bucks['naics'] == '311930') |
                (Bucks['naics'] == '311941') |
                (Bucks['naics'] == '311942') |
                (Bucks['naics'] == '311991') |
                (Bucks['naics'] == '311999') |
                (Bucks['naics'] == '311211') |
                (Bucks['naics'] == '311230') |
                (Bucks['naics'] == '311813') |
                (Bucks['naics'] == '311821') |
                (Bucks['naics'] == '311822') |
                (Bucks['naics'] == '311823') |
                (Bucks['naics'] == '311830') |
                (Bucks['naics'] == '311919') |
                (Bucks['naics'] == '311320') |
                (Bucks['naics'] == '311330') |
                (Bucks['naics'] == '311340') |
                (Bucks['naics'] == '311920') |
                (Bucks['naics'] == '311411') |
                (Bucks['naics'] == '311421') |
                (Bucks['naics'] == '311423') |
                (Bucks['naics'] == '311911') |
                (Bucks['naics'] == '311511') |
                (Bucks['naics'] == '311512') |
                (Bucks['naics'] == '311513') |
                (Bucks['naics'] == '311514') |
                (Bucks['naics'] == '311520') |
                (Bucks['naics'] == '311111') |
                (Bucks['naics'] == '311119') |
                (Bucks['naics'] == '312111') |
                (Bucks['naics'] == '312112') |
                (Bucks['naics'] == '312113') |
                (Bucks['naics'] == '311213') |
                (Bucks['naics'] == '312120') |
                (Bucks['naics'] == '312140') |
                (Bucks['naics'] == '312130') |
                (Bucks['naics'] == '311212') |
                (Bucks['naics'] == '311221') |
                (Bucks['naics'] == '311222') |
                (Bucks['naics'] == '311223') |
                (Bucks['naics'] == '311225') |
                (Bucks['naics'] == '311311') |
                (Bucks['naics'] == '311312') |
                (Bucks['naics'] == '311313') |
                (Bucks['naics'] == '424510') |
                (Bucks['naics'] == '327213') 
                , 'cluster'] = 18

#Footwear
Bucks.loc[(Bucks['naics'] == '316211') |
                (Bucks['naics'] == '316212') |
                (Bucks['naics'] == '316213') |
                (Bucks['naics'] == '316214') |
                (Bucks['naics'] == '316219') |
                (Bucks['naics'] == '316110')
                , 'cluster'] = 19

#Forestry
Bucks.loc[(Bucks['naics'] == '113110') |
                (Bucks['naics'] == '113210') |
                (Bucks['naics'] == '113310') |
                (Bucks['naics'] == '115310')
                , 'cluster'] = 20

#Furniture
Bucks.loc[(Bucks['naics'] == '337121') |
                (Bucks['naics'] == '337122') |
                (Bucks['naics'] == '337124') |
                (Bucks['naics'] == '337125') |
                (Bucks['naics'] == '337910') |
                (Bucks['naics'] == '337127') |
                (Bucks['naics'] == '337211') |
                (Bucks['naics'] == '337214') |
                (Bucks['naics'] == '337110') |
                (Bucks['naics'] == '337129') |
                (Bucks['naics'] == '337215') |
                (Bucks['naics'] == '321991')
                , 'cluster'] = 21

#Hospitality and Tourism
Bucks.loc[(Bucks['naics'] == '711211') |
                (Bucks['naics'] == '711212') |
                (Bucks['naics'] == '711219') |
                (Bucks['naics'] == '713110') |
                (Bucks['naics'] == '713120') |
                (Bucks['naics'] == '453920') |
                (Bucks['naics'] == '712110') |
                (Bucks['naics'] == '712120') |
                (Bucks['naics'] == '712130') |
                (Bucks['naics'] == '712190') |
                (Bucks['naics'] == '713210') |
                (Bucks['naics'] == '713290') |
                (Bucks['naics'] == '114210') |
                (Bucks['naics'] == '713920') |
                (Bucks['naics'] == '713930') |
                (Bucks['naics'] == '713990') |
                (Bucks['naics'] == '721214') |
                (Bucks['naics'] == '561591') |
                (Bucks['naics'] == '721110') |
                (Bucks['naics'] == '721120') |
                (Bucks['naics'] == '721191') |
                (Bucks['naics'] == '721199') |
                (Bucks['naics'] == '721211') |
                (Bucks['naics'] == '721310') |
                (Bucks['naics'] == '487110') |
                (Bucks['naics'] == '487210') |
                (Bucks['naics'] == '487990') |
                (Bucks['naics'] == '532292') |
                (Bucks['naics'] == '561510') |
                (Bucks['naics'] == '561520') |
                (Bucks['naics'] == '561599') 
                , 'cluster'] = 22

#Information Technology and Analytical Instruments
Bucks.loc[(Bucks['naics'] == '334411') |
                (Bucks['naics'] == '334412') |
                (Bucks['naics'] == '334414') |
                (Bucks['naics'] == '334415') |
                (Bucks['naics'] == '334416') |
                (Bucks['naics'] == '334417') |
                (Bucks['naics'] == '334418') |
                (Bucks['naics'] == '334419') |
                (Bucks['naics'] == '334111') |
                (Bucks['naics'] == '334112') |
                (Bucks['naics'] == '334113') |
                (Bucks['naics'] == '334119') |
                (Bucks['naics'] == '333295') |
                (Bucks['naics'] == '334413') |
                (Bucks['naics'] == '511210') |
                (Bucks['naics'] == '334611') |
                (Bucks['naics'] == '334613') |
                (Bucks['naics'] == '334512') |
                (Bucks['naics'] == '334513') |
                (Bucks['naics'] == '334514') |
                (Bucks['naics'] == '334515') |
                (Bucks['naics'] == '334516') |
                (Bucks['naics'] == '334518') |
                (Bucks['naics'] == '334519') |
                (Bucks['naics'] == '334510') |
                (Bucks['naics'] == '334517') |
                (Bucks['naics'] == '334310')
                , 'cluster'] = 23

#Insurance Services
Bucks.loc[(Bucks['naics'] == '524291') |
                (Bucks['naics'] == '524298') |
                (Bucks['naics'] == '524113') |
                (Bucks['naics'] == '524114') |
                (Bucks['naics'] == '524126') |
                (Bucks['naics'] == '524127') |
                (Bucks['naics'] == '524128') |
                (Bucks['naics'] == '524130') 
                , 'cluster'] = 24

#Jewelry and Precious Metals
Bucks.loc[(Bucks['naics'] == '339911') |
                (Bucks['naics'] == '339912') |
                (Bucks['naics'] == '339913') |
                (Bucks['naics'] == '339914') 
                , 'cluster'] = 25

#Leather and Related Products
Bucks.loc[(Bucks['naics'] == '316991') |
                (Bucks['naics'] == '316993') |
                (Bucks['naics'] == '316999') |
                (Bucks['naics'] == '316992') |
                (Bucks['naics'] == '314911') |
                (Bucks['naics'] == '314912') 
                , 'cluster'] = 26

#Lighting and Electrical Equipment
Bucks.loc[(Bucks['naics'] == '335110') |
                (Bucks['naics'] == '335121') |
                (Bucks['naics'] == '335122') |
                (Bucks['naics'] == '335129') |
                (Bucks['naics'] == '335311') |
                (Bucks['naics'] == '335312') |
                (Bucks['naics'] == '335313') |
                (Bucks['naics'] == '335314') |
                (Bucks['naics'] == '335921') |
                (Bucks['naics'] == '335929') |
                (Bucks['naics'] == '335931') |
                (Bucks['naics'] == '335932') |
                (Bucks['naics'] == '335991') |
                (Bucks['naics'] == '335999') |
                (Bucks['naics'] == '335911')
                , 'cluster'] = 27

#Leather and Related Products
Bucks.loc[(Bucks['naics'] == '311611') |
                (Bucks['naics'] == '311612') |
                (Bucks['naics'] == '311613') |
                (Bucks['naics'] == '311615') |
                (Bucks['naics'] == '424520')
                , 'cluster'] = 28

#Marketing, Design, and Publishing
Bucks.loc[(Bucks['naics'] == '541810') |
                (Bucks['naics'] == '541850') |
                (Bucks['naics'] == '541860') |
                (Bucks['naics'] == '541870') |
                (Bucks['naics'] == '541890') |
                (Bucks['naics'] == '541613') |
                (Bucks['naics'] == '541820') |
                (Bucks['naics'] == '541830') |
                (Bucks['naics'] == '541840') |
                (Bucks['naics'] == '541910') |
                (Bucks['naics'] == '541410') |
                (Bucks['naics'] == '541420') |
                (Bucks['naics'] == '541430') |
                (Bucks['naics'] == '541490') |
                (Bucks['naics'] == '511120') |
                (Bucks['naics'] == '511130') |
                (Bucks['naics'] == '511140') |
                (Bucks['naics'] == '511199') |
                (Bucks['naics'] == '519110') |
                (Bucks['naics'] == '519120') |
                (Bucks['naics'] == '519130') |
                (Bucks['naics'] == '519190')
                , 'cluster'] = 29

#Medical Devices
Bucks.loc[(Bucks['naics'] == '333314') |
                (Bucks['naics'] == '339115') |
                (Bucks['naics'] == '339112') |
                (Bucks['naics'] == '339113') |
                (Bucks['naics'] == '339114')
                , 'cluster'] = 30

#Metal Mining
Bucks.loc[(Bucks['naics'] == '212210') |
                (Bucks['naics'] == '212221') |
                (Bucks['naics'] == '212222') |
                (Bucks['naics'] == '212231') |
                (Bucks['naics'] == '212234') |
                (Bucks['naics'] == '212291') |
                (Bucks['naics'] == '212299') |
                (Bucks['naics'] == '212230') | #added due to 2017 NAICS change
                (Bucks['naics'] == '213114')
                , 'cluster'] = 31

#Metalworking Technology
Bucks.loc[(Bucks['naics'] == '333511') |
                (Bucks['naics'] == '333514') |
                (Bucks['naics'] == '333516') |
                (Bucks['naics'] == '333518') |
                (Bucks['naics'] == '333992') |
                (Bucks['naics'] == '333512') |
                (Bucks['naics'] == '333513') |
                (Bucks['naics'] == '333515') |
                (Bucks['naics'] == '332212') |
                (Bucks['naics'] == '333991') |
                (Bucks['naics'] == '332721') |
                (Bucks['naics'] == '332722') |
                (Bucks['naics'] == '327910') |
                (Bucks['naics'] == '332313') |
                (Bucks['naics'] == '332811') |
                (Bucks['naics'] == '332812') |
                (Bucks['naics'] == '332813') 
                , 'cluster'] = 32

#Music and Sound Recording
Bucks.loc[(Bucks['naics'] == '512210') |
                (Bucks['naics'] == '512220') |
                (Bucks['naics'] == '512230') |
                (Bucks['naics'] == '512240') |
                (Bucks['naics'] == '512250') | #added due to 2017 NAICS change
                (Bucks['naics'] == '512290')
                , 'cluster'] = 33

#Nonmetal Mining
Bucks.loc[(Bucks['naics'] == '212311') |
                (Bucks['naics'] == '212312') |
                (Bucks['naics'] == '212313') |
                (Bucks['naics'] == '212319') |
                (Bucks['naics'] == '212321') |
                (Bucks['naics'] == '212322') |
                (Bucks['naics'] == '212324') |
                (Bucks['naics'] == '212325') |
                (Bucks['naics'] == '212391') |
                (Bucks['naics'] == '212392') |
                (Bucks['naics'] == '212393') |
                (Bucks['naics'] == '212399') |
                (Bucks['naics'] == '213115')
                , 'cluster'] = 34

#Oil and Gas Production and Transportation
Bucks.loc[(Bucks['naics'] == '324110') |
                (Bucks['naics'] == '324199') |
                (Bucks['naics'] == '213112') |
                (Bucks['naics'] == '541360') |
                (Bucks['naics'] == '213111') |
                (Bucks['naics'] == '211111') |
                (Bucks['naics'] == '211112') |
                (Bucks['naics'] == '211120') |
                (Bucks['naics'] == '211130') |
                (Bucks['naics'] == '333132') |
                (Bucks['naics'] == '486110') |
                (Bucks['naics'] == '486210') |
                (Bucks['naics'] == '486910') |
                (Bucks['naics'] == '486990')
                , 'cluster'] = 35

#Paper and Packaging
Bucks.loc[(Bucks['naics'] == '322110') |
                (Bucks['naics'] == '322121') |
                (Bucks['naics'] == '322122') |
                (Bucks['naics'] == '322130') |
                (Bucks['naics'] == '322211') |
                (Bucks['naics'] == '322212') |
                (Bucks['naics'] == '322213') |
                (Bucks['naics'] == '322214') |
                (Bucks['naics'] == '322215') |
                (Bucks['naics'] == '322221') |
                (Bucks['naics'] == '322222') |
                (Bucks['naics'] == '322223') |
                (Bucks['naics'] == '322224') |
                (Bucks['naics'] == '322225') |
                (Bucks['naics'] == '322226') |
                (Bucks['naics'] == '322231') |
                (Bucks['naics'] == '322232') |
                (Bucks['naics'] == '322233') |
                (Bucks['naics'] == '322291') |
                (Bucks['naics'] == '322299') 
                , 'cluster'] = 36

#Performing Arts
Bucks.loc[(Bucks['naics'] == '711110') |
                (Bucks['naics'] == '711120') |
                (Bucks['naics'] == '711130') |
                (Bucks['naics'] == '711190') |
                (Bucks['naics'] == '711510') |
                (Bucks['naics'] == '711310') |
                (Bucks['naics'] == '711320') | 
                (Bucks['naics'] == '711410')
                , 'cluster'] = 37

#Plastics
Bucks.loc[(Bucks['naics'] == '326111') |
                (Bucks['naics'] == '326122') |
                (Bucks['naics'] == '326140') |
                (Bucks['naics'] == '326150') |
                (Bucks['naics'] == '326160') |
                (Bucks['naics'] == '326191') |
                (Bucks['naics'] == '326192') |
                (Bucks['naics'] == '326199') |
                (Bucks['naics'] == '339994') |
                (Bucks['naics'] == '325211') |
                (Bucks['naics'] == '326112') |
                (Bucks['naics'] == '326113') |
                (Bucks['naics'] == '326121') |
                (Bucks['naics'] == '326130') |
                (Bucks['naics'] == '333220')
                , 'cluster'] = 38

#Printing Services
Bucks.loc[(Bucks['naics'] == '325910') |
                (Bucks['naics'] == '323121') |
                (Bucks['naics'] == '323122') |
                (Bucks['naics'] == '323110') |
                (Bucks['naics'] == '323111') |
                (Bucks['naics'] == '323112') |
                (Bucks['naics'] == '323113') |
                (Bucks['naics'] == '323115') |
                (Bucks['naics'] == '323116') |
                (Bucks['naics'] == '323117') |
                (Bucks['naics'] == '323118') |
                (Bucks['naics'] == '323119') |
                (Bucks['naics'] == '511191') 
                , 'cluster'] = 39

#Production Technology and Heavy Machinery
Bucks.loc[(Bucks['naics'] == '333210') |
                (Bucks['naics'] == '333291') |
                (Bucks['naics'] == '333292') |
                (Bucks['naics'] == '333293') |
                (Bucks['naics'] == '333294') |
                (Bucks['naics'] == '333298') |
                (Bucks['naics'] == '333993') |
                (Bucks['naics'] == '333999') |
                (Bucks['naics'] == '333111') |
                (Bucks['naics'] == '333112') |
                (Bucks['naics'] == '333120') |
                (Bucks['naics'] == '333131') |
                (Bucks['naics'] == '333611') |
                (Bucks['naics'] == '333612') |
                (Bucks['naics'] == '333613') |
                (Bucks['naics'] == '333618') |
                (Bucks['naics'] == '336510') |
                (Bucks['naics'] == '333411') |
                (Bucks['naics'] == '333412') |
                (Bucks['naics'] == '333414') |
                (Bucks['naics'] == '333415') |
                (Bucks['naics'] == '333311') |
                (Bucks['naics'] == '333312') |
                (Bucks['naics'] == '333319') |
                (Bucks['naics'] == '333921') |
                (Bucks['naics'] == '333922') |
                (Bucks['naics'] == '333923') |
                (Bucks['naics'] == '333924') |
                (Bucks['naics'] == '332911') |
                (Bucks['naics'] == '332912') |
                (Bucks['naics'] == '332919') |
                (Bucks['naics'] == '332991') |
                (Bucks['naics'] == '332997') |
                (Bucks['naics'] == '333911') |
                (Bucks['naics'] == '333912') |
                (Bucks['naics'] == '333913') |
                (Bucks['naics'] == '333913') |   #added due to 2017 NAICS change
                (Bucks['naics'] == '333994') |
                (Bucks['naics'] == '333995') |
                (Bucks['naics'] == '333996') |
                (Bucks['naics'] == '333997') |
                (Bucks['naics'] == '339991') 
                , 'cluster'] = 40

#Recreational and Small Electric Goods
Bucks.loc[(Bucks['naics'] == '337920') |
                (Bucks['naics'] == '339992') |
                (Bucks['naics'] == '339993') |
                (Bucks['naics'] == '339999') |
                (Bucks['naics'] == '339931') |
                (Bucks['naics'] == '339932') |
                (Bucks['naics'] == '336991') |
                (Bucks['naics'] == '339920') |
                (Bucks['naics'] == '333313') |
                (Bucks['naics'] == '333315') |
                (Bucks['naics'] == '339941') |
                (Bucks['naics'] == '339942') |
                (Bucks['naics'] == '339943') |
                (Bucks['naics'] == '339944') |
                (Bucks['naics'] == '335211')
                , 'cluster'] = 41

#Textile Manufacturing
Bucks.loc[(Bucks['naics'] == '313111') |
                (Bucks['naics'] == '313112') |
                (Bucks['naics'] == '313113') |
                (Bucks['naics'] == '313210') |
                (Bucks['naics'] == '313221') |
                (Bucks['naics'] == '313222') |
                (Bucks['naics'] == '313230') |
                (Bucks['naics'] == '313241') |
                (Bucks['naics'] == '313249') |
                (Bucks['naics'] == '313311') |
                (Bucks['naics'] == '313312') |
                (Bucks['naics'] == '313320') |
                (Bucks['naics'] == '315111') |
                (Bucks['naics'] == '315119') |
                (Bucks['naics'] == '315191') |
                (Bucks['naics'] == '315192') |
                (Bucks['naics'] == '314110') |
                (Bucks['naics'] == '314121') |
                (Bucks['naics'] == '314129') |
                (Bucks['naics'] == '314991') |
                (Bucks['naics'] == '314992') |
                (Bucks['naics'] == '325221') |
                (Bucks['naics'] == '325222')
                , 'cluster'] = 42

#Tobacco
Bucks.loc[(Bucks['naics'] == '312210') |
                (Bucks['naics'] == '312221') |
                (Bucks['naics'] == '312229')
                , 'cluster'] = 43

#Trailers, Motor Homes, and Appliances
Bucks.loc[(Bucks['naics'] == '336212') |
                (Bucks['naics'] == '336213') |
                (Bucks['naics'] == '336214') |
                (Bucks['naics'] == '339995') |
                (Bucks['naics'] == '335212') |
                (Bucks['naics'] == '335221') |
                (Bucks['naics'] == '335222') |
                (Bucks['naics'] == '335224') |
                (Bucks['naics'] == '335220') |   #added due to 2017 NAICS change
                (Bucks['naics'] == '335228') 
                , 'cluster'] = 44

#Transportation and Logistics
Bucks.loc[(Bucks['naics'] == '481111') |
                (Bucks['naics'] == '481112') |
                (Bucks['naics'] == '481212') |
                (Bucks['naics'] == '488111') |
                (Bucks['naics'] == '488119') |
                (Bucks['naics'] == '488190') |
                (Bucks['naics'] == '481211') |
                (Bucks['naics'] == '481219') |
                (Bucks['naics'] == '488210') |
                (Bucks['naics'] == '488490') |
                (Bucks['naics'] == '488510') |
                (Bucks['naics'] == '488991') |
                (Bucks['naics'] == '488999') |
                (Bucks['naics'] == '484121') |
                (Bucks['naics'] == '484230') |
                (Bucks['naics'] == '485210') |
                (Bucks['naics'] == '485510') 
                , 'cluster'] = 45

#Upstream Chemical Products
Bucks.loc[(Bucks['naics'] == '325110') |
                (Bucks['naics'] == '325191') |
                (Bucks['naics'] == '325192') |
                (Bucks['naics'] == '325193') |
                (Bucks['naics'] == '325199') |
                (Bucks['naics'] == '325212') |
                (Bucks['naics'] == '325181') |
                (Bucks['naics'] == '325182') |
                (Bucks['naics'] == '325188') |
                (Bucks['naics'] == '325120') |
                (Bucks['naics'] == '325312') |
                (Bucks['naics'] == '325320') 
                , 'cluster'] = 46

#Upstream Metal Manufacturing
Bucks.loc[(Bucks['naics'] == '331111') |
                (Bucks['naics'] == '331112') |
                (Bucks['naics'] == '332111') |
                (Bucks['naics'] == '331221') |
                (Bucks['naics'] == '331311') |
                (Bucks['naics'] == '331312') |
                (Bucks['naics'] == '331314') |
                (Bucks['naics'] == '331315') |
                (Bucks['naics'] == '331316') |
                (Bucks['naics'] == '331319') |
                (Bucks['naics'] == '331411') |
                (Bucks['naics'] == '331419') |
                (Bucks['naics'] == '331421') |
                (Bucks['naics'] == '331422') |
                (Bucks['naics'] == '331423') |
                (Bucks['naics'] == '331491') |
                (Bucks['naics'] == '331492') |
                (Bucks['naics'] == '332112') |
                (Bucks['naics'] == '331210') |
                (Bucks['naics'] == '332115') |
                (Bucks['naics'] == '332116') |
                (Bucks['naics'] == '332117') |
                (Bucks['naics'] == '331222') |
                (Bucks['naics'] == '332611') |
                (Bucks['naics'] == '332612') |
                (Bucks['naics'] == '332618') 
                , 'cluster'] = 47


#Video Production and Distribution
Bucks.loc[(Bucks['naics'] == '334612') |
                (Bucks['naics'] == '512110') |
                (Bucks['naics'] == '512120') |
                (Bucks['naics'] == '512132') |
                (Bucks['naics'] == '512191') |
                (Bucks['naics'] == '512199')
                , 'cluster'] = 48

#Vulcanized and Fired Materials
Bucks.loc[(Bucks['naics'] == '327111') |
                (Bucks['naics'] == '327112') |
                (Bucks['naics'] == '327113') |
                (Bucks['naics'] == '327121') |
                (Bucks['naics'] == '327122') |
                (Bucks['naics'] == '327123') |
                (Bucks['naics'] == '327124') |
                (Bucks['naics'] == '327125') |
                (Bucks['naics'] == '327992') |
                (Bucks['naics'] == '327211') |
                (Bucks['naics'] == '327212') |
                (Bucks['naics'] == '327215') |
                (Bucks['naics'] == '326211') |
                (Bucks['naics'] == '326212') |
                (Bucks['naics'] == '326220') |
                (Bucks['naics'] == '326291') |
                (Bucks['naics'] == '326299') 
                , 'cluster'] = 49

#Water Transportation
Bucks.loc[(Bucks['naics'] == '483112') |
                (Bucks['naics'] == '483114') |
                (Bucks['naics'] == '483212') |
                (Bucks['naics'] == '483111') |
                (Bucks['naics'] == '483113') |
                (Bucks['naics'] == '483211') |
                (Bucks['naics'] == '488310') |
                (Bucks['naics'] == '488320') |
                (Bucks['naics'] == '488330') |
                (Bucks['naics'] == '488390') |
                (Bucks['naics'] == '336611') |
                (Bucks['naics'] == '336612') 
                , 'cluster'] = 50

#Wood Products
Bucks.loc[(Bucks['naics'] == '321113') |
                (Bucks['naics'] == '321114') |
                (Bucks['naics'] == '321912') |
                (Bucks['naics'] == '321211') |
                (Bucks['naics'] == '321212') |
                (Bucks['naics'] == '321213') |
                (Bucks['naics'] == '321214') |
                (Bucks['naics'] == '321219') |
                (Bucks['naics'] == '321911') |
                (Bucks['naics'] == '321918') |
                (Bucks['naics'] == '321920') |
                (Bucks['naics'] == '321999') |                
                (Bucks['naics'] == '321992') 
                , 'cluster'] = 51

Bucks


# # Remove local industries that weren't grouped in an economic cluster

# In[9]:


Bucks_traded = Bucks.loc[Bucks['cluster'] != 0]
Bucks_traded = Bucks_traded.sort_values('cluster')
Bucks_traded


# In[10]:


Bucks_traded.to_csv(r"G:\My Drive\BCarney\DataAnalysis\CBP_2017\NAICS_AllDigits\DVRPC_counties\Bucks\Bucks_traded.csv", index=False)
Bucks_traded


# # Calculate employment totals for each cluster via groupby

# In[11]:


Bucks_clustertotals = Bucks_traded.groupby('cluster').sum()
Bucks_clustertotals


# # Import Economic Cluster .csv for Indexing

# In[12]:


cluster_index = pd.read_csv(r"G:\My Drive\BCarney\DataAnalysis\CBP_2017\NAICS_AllDigits\USClusterMapping_EconomicClusters.csv", index_col = 'cluster')
cluster_index


# # Left Join Index with Bucks County Cluster Totals

# In[13]:


clusters_joined = pd.merge(cluster_index, Bucks_clustertotals, how= "left", left_on='cluster', right_on='cluster')
clusters_joined


# # Export cluster totals df to .csv

# In[20]:


clusters_joined.to_csv(r"G:\My Drive\BCarney\DataAnalysis\CBP_2017\NAICS_AllDigits\DVRPC_counties\Bucks\Bucks_ClusterTotals.csv")


# In[ ]:




