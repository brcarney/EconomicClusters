#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# # Import data

# In[2]:


regionNAICS = pd.read_csv(r"G:\My Drive\BCarney\DataAnalysis\CBP_2017\NAICS_AllDigits\DVRPC_region\region_NAICStotal.csv")
regionNAICS


# # Convert NAICS dtype to string

# In[3]:


regionNAICS['naics'] = regionNAICS['naics'].astype(str)


# # Cluster Grouping

# In[4]:


regionNAICS = regionNAICS.assign(cluster= 0)

#Aerospace Vehicles and Defense
regionNAICS.loc[(regionNAICS['naics'] == '336411') |
                (regionNAICS['naics'] == '336412') |
                (regionNAICS['naics'] == '336413') |
                (regionNAICS['naics'] == '336414') |
                (regionNAICS['naics'] == '336415') |
                (regionNAICS['naics'] == '336419') |
                (regionNAICS['naics'] == '334511') 
                , 'cluster'] = 1

#Agricultural Inputs and Services
regionNAICS.loc[(regionNAICS['naics'] == '115111') |
                (regionNAICS['naics'] == '115112') |
                (regionNAICS['naics'] == '115113') |
                (regionNAICS['naics'] == '115114') |
                (regionNAICS['naics'] == '115210') |
                (regionNAICS['naics'] == '115115') |
                (regionNAICS['naics'] == '115116') |
                (regionNAICS['naics'] == '325311') |
                (regionNAICS['naics'] == '325314') 
                , 'cluster'] = 2

#Apparel
regionNAICS.loc[(regionNAICS['naics'] == '314999') |
                (regionNAICS['naics'] == '315292') |
                (regionNAICS['naics'] == '315299') |
                (regionNAICS['naics'] == '315991') |
                (regionNAICS['naics'] == '315992') |
                (regionNAICS['naics'] == '315993') |
                (regionNAICS['naics'] == '315999') |
                (regionNAICS['naics'] == '315221') |
                (regionNAICS['naics'] == '315222') |
                (regionNAICS['naics'] == '315223') |
                (regionNAICS['naics'] == '315224') |
                (regionNAICS['naics'] == '315225') |
                (regionNAICS['naics'] == '315228') |
                (regionNAICS['naics'] == '315231') |
                (regionNAICS['naics'] == '315232') |
                (regionNAICS['naics'] == '315233') |
                (regionNAICS['naics'] == '315234') |
                (regionNAICS['naics'] == '315239') |
                (regionNAICS['naics'] == '315291') |
                (regionNAICS['naics'] == '315211') |
                (regionNAICS['naics'] == '315212') 
                , 'cluster'] = 3

#Automotive
regionNAICS.loc[(regionNAICS['naics'] == '332114') |
                (regionNAICS['naics'] == '336321') |
                (regionNAICS['naics'] == '336322') |
                (regionNAICS['naics'] == '336330') |
                (regionNAICS['naics'] == '336340') |
                (regionNAICS['naics'] == '336350') |
                (regionNAICS['naics'] == '336360') |
                (regionNAICS['naics'] == '336391') |
                (regionNAICS['naics'] == '336399') |
                (regionNAICS['naics'] == '336311') |
                (regionNAICS['naics'] == '336312') |
                (regionNAICS['naics'] == '336111') |
                (regionNAICS['naics'] == '336112') |
                (regionNAICS['naics'] == '336120') |
                (regionNAICS['naics'] == '336211') |
                (regionNAICS['naics'] == '336370') |
                (regionNAICS['naics'] == '336999') |
                (regionNAICS['naics'] == '336992') |
                (regionNAICS['naics'] == '331511') |
                (regionNAICS['naics'] == '331512') |
                (regionNAICS['naics'] == '331513') |
                (regionNAICS['naics'] == '331521') |
                (regionNAICS['naics'] == '331522') |
                (regionNAICS['naics'] == '331524') |
                (regionNAICS['naics'] == '331525') |
                (regionNAICS['naics'] == '331528') 
                , 'cluster'] = 4

#BioPharmaceuticals
regionNAICS.loc[(regionNAICS['naics'] == '325411') |
                (regionNAICS['naics'] == '325412') |
                (regionNAICS['naics'] == '325414') |
                (regionNAICS['naics'] == '325413')
                , 'cluster'] = 5

#Business Services
regionNAICS.loc[(regionNAICS['naics'] == '551111') |
                (regionNAICS['naics'] == '551112') |
                (regionNAICS['naics'] == '551114') |
                (regionNAICS['naics'] == '541611') |
                (regionNAICS['naics'] == '541612') |
                (regionNAICS['naics'] == '541614') |
                (regionNAICS['naics'] == '541618') |
                (regionNAICS['naics'] == '541690') |
                (regionNAICS['naics'] == '533110') |
                (regionNAICS['naics'] == '541199') |
                (regionNAICS['naics'] == '541214') |
                (regionNAICS['naics'] == '541930') |
                (regionNAICS['naics'] == '541990') |
                (regionNAICS['naics'] == '561210') |
                (regionNAICS['naics'] == '561330') |
                (regionNAICS['naics'] == '561421') |
                (regionNAICS['naics'] == '561422') |
                (regionNAICS['naics'] == '561920') |
                (regionNAICS['naics'] == '518210') |
                (regionNAICS['naics'] == '541511') |
                (regionNAICS['naics'] == '541512') |
                (regionNAICS['naics'] == '541513') |
                (regionNAICS['naics'] == '541519') |
                (regionNAICS['naics'] == '561311') |
                (regionNAICS['naics'] == '561312') |
                (regionNAICS['naics'] == '541330') |
                (regionNAICS['naics'] == '541310') |
                (regionNAICS['naics'] == '541320') |
                (regionNAICS['naics'] == '541340') |
                (regionNAICS['naics'] == '485310') |
                (regionNAICS['naics'] == '485320') |
                (regionNAICS['naics'] == '485999') |
                (regionNAICS['naics'] == '532112') 
                , 'cluster'] = 6

#Coal Mining
regionNAICS.loc[(regionNAICS['naics'] == '212111') |
                (regionNAICS['naics'] == '212112') |
                (regionNAICS['naics'] == '212113') |
                (regionNAICS['naics'] == '213113')
                , 'cluster'] = 7

#Communications Equipment and Services
regionNAICS.loc[(regionNAICS['naics'] == '515210') |
                (regionNAICS['naics'] == '517210') |
                (regionNAICS['naics'] == '517410') |
                (regionNAICS['naics'] == '517919') |
                (regionNAICS['naics'] == '334210') |
                (regionNAICS['naics'] == '334220') |
                (regionNAICS['naics'] == '334290') |
                (regionNAICS['naics'] == '335912')
                , 'cluster'] = 8

#Construction Products and Services
regionNAICS.loc[(regionNAICS['naics'] == '236210') |
                (regionNAICS['naics'] == '237120') |
                (regionNAICS['naics'] == '237130') |
                (regionNAICS['naics'] == '237990') |
                (regionNAICS['naics'] == '221310') |
                (regionNAICS['naics'] == '221330') |
                (regionNAICS['naics'] == '332410') |
                (regionNAICS['naics'] == '332420') |
                (regionNAICS['naics'] == '332913') |
                (regionNAICS['naics'] == '332996') |
                (regionNAICS['naics'] == '327310') |
                (regionNAICS['naics'] == '327331') |
                (regionNAICS['naics'] == '327332') |
                (regionNAICS['naics'] == '327410') |
                (regionNAICS['naics'] == '327420') |
                (regionNAICS['naics'] == '327991') |
                (regionNAICS['naics'] == '327993') |
                (regionNAICS['naics'] == '327999') |
                (regionNAICS['naics'] == '324121') |
                (regionNAICS['naics'] == '324122') 
                , 'cluster'] = 9

#Distribution and Electronic Commerce
regionNAICS.loc[(regionNAICS['naics'] == '493110') |
                (regionNAICS['naics'] == '493120') |
                (regionNAICS['naics'] == '493190') |
                (regionNAICS['naics'] == '425110') |
                (regionNAICS['naics'] == '454111') |
                (regionNAICS['naics'] == '454112') |
                (regionNAICS['naics'] == '454113') |
                (regionNAICS['naics'] == '454110') |    #added due to 2017 NAICS change
                (regionNAICS['naics'] == '425120') |
                (regionNAICS['naics'] == '561499') |
                (regionNAICS['naics'] == '561910') |
                (regionNAICS['naics'] == '424310') |
                (regionNAICS['naics'] == '424320') |
                (regionNAICS['naics'] == '424330') |
                (regionNAICS['naics'] == '424340') |
                (regionNAICS['naics'] == '424920') |
                (regionNAICS['naics'] == '424610') |
                (regionNAICS['naics'] == '424690') |
                (regionNAICS['naics'] == '424210') |
                (regionNAICS['naics'] == '424590') |
                (regionNAICS['naics'] == '424910') |
                (regionNAICS['naics'] == '424930') |
                (regionNAICS['naics'] == '424940') |
                (regionNAICS['naics'] == '493130') |
                (regionNAICS['naics'] == '424440') |
                (regionNAICS['naics'] == '424460') |
                (regionNAICS['naics'] == '424470') |
                (regionNAICS['naics'] == '424480') |
                (regionNAICS['naics'] == '424820') |
                (regionNAICS['naics'] == '423210') |
                (regionNAICS['naics'] == '423220') |
                (regionNAICS['naics'] == '423940') |
                (regionNAICS['naics'] == '424110') |
                (regionNAICS['naics'] == '424120') |
                (regionNAICS['naics'] == '424130') |
                (regionNAICS['naics'] == '423910') |
                (regionNAICS['naics'] == '423920') |
                (regionNAICS['naics'] == '424950') |
                (regionNAICS['naics'] == '424990') |
                (regionNAICS['naics'] == '423820') |
                (regionNAICS['naics'] == '423810') |
                (regionNAICS['naics'] == '423830') |
                (regionNAICS['naics'] == '423840') |
                (regionNAICS['naics'] == '423850') |
                (regionNAICS['naics'] == '423860') |
                (regionNAICS['naics'] == '423410') |
                (regionNAICS['naics'] == '423420') |
                (regionNAICS['naics'] == '423430') |
                (regionNAICS['naics'] == '423440') |
                (regionNAICS['naics'] == '423450') |
                (regionNAICS['naics'] == '423460') |
                (regionNAICS['naics'] == '423490') |
                (regionNAICS['naics'] == '423610') |
                (regionNAICS['naics'] == '423620') |
                (regionNAICS['naics'] == '423690') |
                (regionNAICS['naics'] == '423510') |
                (regionNAICS['naics'] == '423520') |
                (regionNAICS['naics'] == '424710') |
                (regionNAICS['naics'] == '424720') |
                (regionNAICS['naics'] == '532411') |
                (regionNAICS['naics'] == '532412') |
                (regionNAICS['naics'] == '532420') |
                (regionNAICS['naics'] == '532490')
                , 'cluster'] = 10

#Downstream Chemical Products
regionNAICS.loc[(regionNAICS['naics'] == '325611') |
                (regionNAICS['naics'] == '325612') |
                (regionNAICS['naics'] == '325613') |
                (regionNAICS['naics'] == '325620') |
                (regionNAICS['naics'] == '325520') |
                (regionNAICS['naics'] == '325991') |
                (regionNAICS['naics'] == '325992') |
                (regionNAICS['naics'] == '325998') |
                (regionNAICS['naics'] == '325131') |
                (regionNAICS['naics'] == '325132') |
                (regionNAICS['naics'] == '325510') |
                (regionNAICS['naics'] == '325920') |
                (regionNAICS['naics'] == '324191')
                , 'cluster'] = 11

#Downstream Metal Products
regionNAICS.loc[(regionNAICS['naics'] == '332211') |
                (regionNAICS['naics'] == '332213') |
                (regionNAICS['naics'] == '332214') |
                (regionNAICS['naics'] == '332321') |
                (regionNAICS['naics'] == '332323') |
                (regionNAICS['naics'] == '332510') |
                (regionNAICS['naics'] == '332998') |
                (regionNAICS['naics'] == '332999') |
                (regionNAICS['naics'] == '332992') |
                (regionNAICS['naics'] == '332993') |
                (regionNAICS['naics'] == '332994') |
                (regionNAICS['naics'] == '332995') |
                (regionNAICS['naics'] == '332311') |
                (regionNAICS['naics'] == '332312') |
                (regionNAICS['naics'] == '332431') |
                (regionNAICS['naics'] == '332439')
                , 'cluster'] = 12

#Education and Knowledge Creation
regionNAICS.loc[(regionNAICS['naics'] == '611410') |
                (regionNAICS['naics'] == '611420') |
                (regionNAICS['naics'] == '611430') |
                (regionNAICS['naics'] == '611512') |
                (regionNAICS['naics'] == '611513') |
                (regionNAICS['naics'] == '611630') |
                (regionNAICS['naics'] == '611691') |
                (regionNAICS['naics'] == '611699') |
                (regionNAICS['naics'] == '611210') |
                (regionNAICS['naics'] == '611310') |
                (regionNAICS['naics'] == '611710') |
                (regionNAICS['naics'] == '541711') |
                (regionNAICS['naics'] == '541712') |
                (regionNAICS['naics'] == '541713') |  #added due to 2017 NAICS change
                (regionNAICS['naics'] == '541714') |  #added due to 2017 NAICS change
                (regionNAICS['naics'] == '541715') |  #added due to 2017 NAICS change
                (regionNAICS['naics'] == '541720') |
                (regionNAICS['naics'] == '813920') 
                , 'cluster'] = 13

#Electric Power Generation and Transmisison
regionNAICS.loc[(regionNAICS['naics'] == '221112') |
                (regionNAICS['naics'] == '221111') |
                (regionNAICS['naics'] == '221113') |
                (regionNAICS['naics'] == '221119') |
                (regionNAICS['naics'] == '221121')
                , 'cluster'] = 14

#Environmental Services
regionNAICS.loc[(regionNAICS['naics'] == '562112') |
                (regionNAICS['naics'] == '562119') |
                (regionNAICS['naics'] == '562211') |
                (regionNAICS['naics'] == '562213') |
                (regionNAICS['naics'] == '562219') |
                (regionNAICS['naics'] == '562920') |
                (regionNAICS['naics'] == '562998')
                , 'cluster'] = 15

#Financial Services
regionNAICS.loc[(regionNAICS['naics'] == '523910') |
                (regionNAICS['naics'] == '523920') |
                (regionNAICS['naics'] == '523930') |
                (regionNAICS['naics'] == '523991') |
                (regionNAICS['naics'] == '523999') |
                (regionNAICS['naics'] == '525910') |
                (regionNAICS['naics'] == '525990') |
                (regionNAICS['naics'] == '522120') |
                (regionNAICS['naics'] == '522190') |
                (regionNAICS['naics'] == '522210') |
                (regionNAICS['naics'] == '522220') |
                (regionNAICS['naics'] == '522291') |
                (regionNAICS['naics'] == '522292') |
                (regionNAICS['naics'] == '522293') |
                (regionNAICS['naics'] == '522294') |
                (regionNAICS['naics'] == '522298') |
                (regionNAICS['naics'] == '522320') |
                (regionNAICS['naics'] == '522390') |
                (regionNAICS['naics'] == '561450') |
                (regionNAICS['naics'] == '521110') |
                (regionNAICS['naics'] == '522310') |
                (regionNAICS['naics'] == '523110') |
                (regionNAICS['naics'] == '523120') |
                (regionNAICS['naics'] == '523130') |
                (regionNAICS['naics'] == '523140') |
                (regionNAICS['naics'] == '523210')
                , 'cluster'] = 16

#Fishing and Fishing Products
regionNAICS.loc[(regionNAICS['naics'] == '114111') |
                (regionNAICS['naics'] == '114112') |
                (regionNAICS['naics'] == '114119') |
                (regionNAICS['naics'] == '311711') |
                (regionNAICS['naics'] == '311712')
                , 'cluster'] = 17

#Food Processing and Manufacturing
regionNAICS.loc[(regionNAICS['naics'] == '311412') |
                (regionNAICS['naics'] == '311422') |
                (regionNAICS['naics'] == '311930') |
                (regionNAICS['naics'] == '311941') |
                (regionNAICS['naics'] == '311942') |
                (regionNAICS['naics'] == '311991') |
                (regionNAICS['naics'] == '311999') |
                (regionNAICS['naics'] == '311211') |
                (regionNAICS['naics'] == '311230') |
                (regionNAICS['naics'] == '311813') |
                (regionNAICS['naics'] == '311821') |
                (regionNAICS['naics'] == '311822') |
                (regionNAICS['naics'] == '311823') |
                (regionNAICS['naics'] == '311830') |
                (regionNAICS['naics'] == '311919') |
                (regionNAICS['naics'] == '311320') |
                (regionNAICS['naics'] == '311330') |
                (regionNAICS['naics'] == '311340') |
                (regionNAICS['naics'] == '311920') |
                (regionNAICS['naics'] == '311411') |
                (regionNAICS['naics'] == '311421') |
                (regionNAICS['naics'] == '311423') |
                (regionNAICS['naics'] == '311911') |
                (regionNAICS['naics'] == '311511') |
                (regionNAICS['naics'] == '311512') |
                (regionNAICS['naics'] == '311513') |
                (regionNAICS['naics'] == '311514') |
                (regionNAICS['naics'] == '311520') |
                (regionNAICS['naics'] == '311111') |
                (regionNAICS['naics'] == '311119') |
                (regionNAICS['naics'] == '312111') |
                (regionNAICS['naics'] == '312112') |
                (regionNAICS['naics'] == '312113') |
                (regionNAICS['naics'] == '311213') |
                (regionNAICS['naics'] == '312120') |
                (regionNAICS['naics'] == '312140') |
                (regionNAICS['naics'] == '312130') |
                (regionNAICS['naics'] == '311212') |
                (regionNAICS['naics'] == '311221') |
                (regionNAICS['naics'] == '311222') |
                (regionNAICS['naics'] == '311223') |
                (regionNAICS['naics'] == '311225') |
                (regionNAICS['naics'] == '311311') |
                (regionNAICS['naics'] == '311312') |
                (regionNAICS['naics'] == '311313') |
                (regionNAICS['naics'] == '424510') |
                (regionNAICS['naics'] == '327213') 
                , 'cluster'] = 18

#Footwear
regionNAICS.loc[(regionNAICS['naics'] == '316211') |
                (regionNAICS['naics'] == '316212') |
                (regionNAICS['naics'] == '316213') |
                (regionNAICS['naics'] == '316214') |
                (regionNAICS['naics'] == '316219') |
                (regionNAICS['naics'] == '316110')
                , 'cluster'] = 19

#Forestry
regionNAICS.loc[(regionNAICS['naics'] == '113110') |
                (regionNAICS['naics'] == '113210') |
                (regionNAICS['naics'] == '113310') |
                (regionNAICS['naics'] == '115310')
                , 'cluster'] = 20

#Furniture
regionNAICS.loc[(regionNAICS['naics'] == '337121') |
                (regionNAICS['naics'] == '337122') |
                (regionNAICS['naics'] == '337124') |
                (regionNAICS['naics'] == '337125') |
                (regionNAICS['naics'] == '337910') |
                (regionNAICS['naics'] == '337127') |
                (regionNAICS['naics'] == '337211') |
                (regionNAICS['naics'] == '337214') |
                (regionNAICS['naics'] == '337110') |
                (regionNAICS['naics'] == '337129') |
                (regionNAICS['naics'] == '337215') |
                (regionNAICS['naics'] == '321991')
                , 'cluster'] = 21

#Hospitality and Tourism
regionNAICS.loc[(regionNAICS['naics'] == '711211') |
                (regionNAICS['naics'] == '711212') |
                (regionNAICS['naics'] == '711219') |
                (regionNAICS['naics'] == '713110') |
                (regionNAICS['naics'] == '713120') |
                (regionNAICS['naics'] == '453920') |
                (regionNAICS['naics'] == '712110') |
                (regionNAICS['naics'] == '712120') |
                (regionNAICS['naics'] == '712130') |
                (regionNAICS['naics'] == '712190') |
                (regionNAICS['naics'] == '713210') |
                (regionNAICS['naics'] == '713290') |
                (regionNAICS['naics'] == '114210') |
                (regionNAICS['naics'] == '713920') |
                (regionNAICS['naics'] == '713930') |
                (regionNAICS['naics'] == '713990') |
                (regionNAICS['naics'] == '721214') |
                (regionNAICS['naics'] == '561591') |
                (regionNAICS['naics'] == '721110') |
                (regionNAICS['naics'] == '721120') |
                (regionNAICS['naics'] == '721191') |
                (regionNAICS['naics'] == '721199') |
                (regionNAICS['naics'] == '721211') |
                (regionNAICS['naics'] == '721310') |
                (regionNAICS['naics'] == '487110') |
                (regionNAICS['naics'] == '487210') |
                (regionNAICS['naics'] == '487990') |
                (regionNAICS['naics'] == '532292') |
                (regionNAICS['naics'] == '561510') |
                (regionNAICS['naics'] == '561520') |
                (regionNAICS['naics'] == '561599') 
                , 'cluster'] = 22

#Information Technology and Analytical Instruments
regionNAICS.loc[(regionNAICS['naics'] == '334411') |
                (regionNAICS['naics'] == '334412') |
                (regionNAICS['naics'] == '334414') |
                (regionNAICS['naics'] == '334415') |
                (regionNAICS['naics'] == '334416') |
                (regionNAICS['naics'] == '334417') |
                (regionNAICS['naics'] == '334418') |
                (regionNAICS['naics'] == '334419') |
                (regionNAICS['naics'] == '334111') |
                (regionNAICS['naics'] == '334112') |
                (regionNAICS['naics'] == '334113') |
                (regionNAICS['naics'] == '334119') |
                (regionNAICS['naics'] == '333295') |
                (regionNAICS['naics'] == '334413') |
                (regionNAICS['naics'] == '511210') |
                (regionNAICS['naics'] == '334611') |
                (regionNAICS['naics'] == '334613') |
                (regionNAICS['naics'] == '334512') |
                (regionNAICS['naics'] == '334513') |
                (regionNAICS['naics'] == '334514') |
                (regionNAICS['naics'] == '334515') |
                (regionNAICS['naics'] == '334516') |
                (regionNAICS['naics'] == '334518') |
                (regionNAICS['naics'] == '334519') |
                (regionNAICS['naics'] == '334510') |
                (regionNAICS['naics'] == '334517') |
                (regionNAICS['naics'] == '334310')
                , 'cluster'] = 23

#Insurance Services
regionNAICS.loc[(regionNAICS['naics'] == '524291') |
                (regionNAICS['naics'] == '524298') |
                (regionNAICS['naics'] == '524113') |
                (regionNAICS['naics'] == '524114') |
                (regionNAICS['naics'] == '524126') |
                (regionNAICS['naics'] == '524127') |
                (regionNAICS['naics'] == '524128') |
                (regionNAICS['naics'] == '524130') 
                , 'cluster'] = 24

#Jewelry and Precious Metals
regionNAICS.loc[(regionNAICS['naics'] == '339911') |
                (regionNAICS['naics'] == '339912') |
                (regionNAICS['naics'] == '339913') |
                (regionNAICS['naics'] == '339914') 
                , 'cluster'] = 25

#Leather and Related Products
regionNAICS.loc[(regionNAICS['naics'] == '316991') |
                (regionNAICS['naics'] == '316993') |
                (regionNAICS['naics'] == '316999') |
                (regionNAICS['naics'] == '316992') |
                (regionNAICS['naics'] == '314911') |
                (regionNAICS['naics'] == '314912') 
                , 'cluster'] = 26

#Lighting and Electrical Equipment
regionNAICS.loc[(regionNAICS['naics'] == '335110') |
                (regionNAICS['naics'] == '335121') |
                (regionNAICS['naics'] == '335122') |
                (regionNAICS['naics'] == '335129') |
                (regionNAICS['naics'] == '335311') |
                (regionNAICS['naics'] == '335312') |
                (regionNAICS['naics'] == '335313') |
                (regionNAICS['naics'] == '335314') |
                (regionNAICS['naics'] == '335921') |
                (regionNAICS['naics'] == '335929') |
                (regionNAICS['naics'] == '335931') |
                (regionNAICS['naics'] == '335932') |
                (regionNAICS['naics'] == '335991') |
                (regionNAICS['naics'] == '335999') |
                (regionNAICS['naics'] == '335911')
                , 'cluster'] = 27

#Leather and Related Products
regionNAICS.loc[(regionNAICS['naics'] == '311611') |
                (regionNAICS['naics'] == '311612') |
                (regionNAICS['naics'] == '311613') |
                (regionNAICS['naics'] == '311615') |
                (regionNAICS['naics'] == '424520')
                , 'cluster'] = 28

#Marketing, Design, and Publishing
regionNAICS.loc[(regionNAICS['naics'] == '541810') |
                (regionNAICS['naics'] == '541850') |
                (regionNAICS['naics'] == '541860') |
                (regionNAICS['naics'] == '541870') |
                (regionNAICS['naics'] == '541890') |
                (regionNAICS['naics'] == '541613') |
                (regionNAICS['naics'] == '541820') |
                (regionNAICS['naics'] == '541830') |
                (regionNAICS['naics'] == '541840') |
                (regionNAICS['naics'] == '541910') |
                (regionNAICS['naics'] == '541410') |
                (regionNAICS['naics'] == '541420') |
                (regionNAICS['naics'] == '541430') |
                (regionNAICS['naics'] == '541490') |
                (regionNAICS['naics'] == '511120') |
                (regionNAICS['naics'] == '511130') |
                (regionNAICS['naics'] == '511140') |
                (regionNAICS['naics'] == '511199') |
                (regionNAICS['naics'] == '519110') |
                (regionNAICS['naics'] == '519120') |
                (regionNAICS['naics'] == '519130') |
                (regionNAICS['naics'] == '519190')
                , 'cluster'] = 29

#Medical Devices
regionNAICS.loc[(regionNAICS['naics'] == '333314') |
                (regionNAICS['naics'] == '339115') |
                (regionNAICS['naics'] == '339112') |
                (regionNAICS['naics'] == '339113') |
                (regionNAICS['naics'] == '339114')
                , 'cluster'] = 30

#Metal Mining
regionNAICS.loc[(regionNAICS['naics'] == '212210') |
                (regionNAICS['naics'] == '212221') |
                (regionNAICS['naics'] == '212222') |
                (regionNAICS['naics'] == '212231') |
                (regionNAICS['naics'] == '212234') |
                (regionNAICS['naics'] == '212291') |
                (regionNAICS['naics'] == '212299') |
                (regionNAICS['naics'] == '212230') | #added due to 2017 NAICS change
                (regionNAICS['naics'] == '213114')
                , 'cluster'] = 31

#Metalworking Technology
regionNAICS.loc[(regionNAICS['naics'] == '333511') |
                (regionNAICS['naics'] == '333514') |
                (regionNAICS['naics'] == '333516') |
                (regionNAICS['naics'] == '333518') |
                (regionNAICS['naics'] == '333992') |
                (regionNAICS['naics'] == '333512') |
                (regionNAICS['naics'] == '333513') |
                (regionNAICS['naics'] == '333515') |
                (regionNAICS['naics'] == '332212') |
                (regionNAICS['naics'] == '333991') |
                (regionNAICS['naics'] == '332721') |
                (regionNAICS['naics'] == '332722') |
                (regionNAICS['naics'] == '327910') |
                (regionNAICS['naics'] == '332313') |
                (regionNAICS['naics'] == '332811') |
                (regionNAICS['naics'] == '332812') |
                (regionNAICS['naics'] == '332813') 
                , 'cluster'] = 32

#Music and Sound Recording
regionNAICS.loc[(regionNAICS['naics'] == '512210') |
                (regionNAICS['naics'] == '512220') |
                (regionNAICS['naics'] == '512230') |
                (regionNAICS['naics'] == '512240') |
                (regionNAICS['naics'] == '512250') | #added due to 2017 NAICS change
                (regionNAICS['naics'] == '512290')
                , 'cluster'] = 33

#Nonmetal Mining
regionNAICS.loc[(regionNAICS['naics'] == '212311') |
                (regionNAICS['naics'] == '212312') |
                (regionNAICS['naics'] == '212313') |
                (regionNAICS['naics'] == '212319') |
                (regionNAICS['naics'] == '212321') |
                (regionNAICS['naics'] == '212322') |
                (regionNAICS['naics'] == '212324') |
                (regionNAICS['naics'] == '212325') |
                (regionNAICS['naics'] == '212391') |
                (regionNAICS['naics'] == '212392') |
                (regionNAICS['naics'] == '212393') |
                (regionNAICS['naics'] == '212399') |
                (regionNAICS['naics'] == '213115')
                , 'cluster'] = 34

#Oil and Gas Production and Transportation
regionNAICS.loc[(regionNAICS['naics'] == '324110') |
                (regionNAICS['naics'] == '324199') |
                (regionNAICS['naics'] == '213112') |
                (regionNAICS['naics'] == '541360') |
                (regionNAICS['naics'] == '213111') |
                (regionNAICS['naics'] == '211111') |
                (regionNAICS['naics'] == '211112') |
                (regionNAICS['naics'] == '211120') |
                (regionNAICS['naics'] == '211130') |
                (regionNAICS['naics'] == '333132') |
                (regionNAICS['naics'] == '486110') |
                (regionNAICS['naics'] == '486210') |
                (regionNAICS['naics'] == '486910') |
                (regionNAICS['naics'] == '486990')
                , 'cluster'] = 35

#Paper and Packaging
regionNAICS.loc[(regionNAICS['naics'] == '322110') |
                (regionNAICS['naics'] == '322121') |
                (regionNAICS['naics'] == '322122') |
                (regionNAICS['naics'] == '322130') |
                (regionNAICS['naics'] == '322211') |
                (regionNAICS['naics'] == '322212') |
                (regionNAICS['naics'] == '322213') |
                (regionNAICS['naics'] == '322214') |
                (regionNAICS['naics'] == '322215') |
                (regionNAICS['naics'] == '322221') |
                (regionNAICS['naics'] == '322222') |
                (regionNAICS['naics'] == '322223') |
                (regionNAICS['naics'] == '322224') |
                (regionNAICS['naics'] == '322225') |
                (regionNAICS['naics'] == '322226') |
                (regionNAICS['naics'] == '322231') |
                (regionNAICS['naics'] == '322232') |
                (regionNAICS['naics'] == '322233') |
                (regionNAICS['naics'] == '322291') |
                (regionNAICS['naics'] == '322299') 
                , 'cluster'] = 36

#Performing Arts
regionNAICS.loc[(regionNAICS['naics'] == '711110') |
                (regionNAICS['naics'] == '711120') |
                (regionNAICS['naics'] == '711130') |
                (regionNAICS['naics'] == '711190') |
                (regionNAICS['naics'] == '711510') |
                (regionNAICS['naics'] == '711310') |
                (regionNAICS['naics'] == '711320') | 
                (regionNAICS['naics'] == '711410')
                , 'cluster'] = 37

#Plastics
regionNAICS.loc[(regionNAICS['naics'] == '326111') |
                (regionNAICS['naics'] == '326122') |
                (regionNAICS['naics'] == '326140') |
                (regionNAICS['naics'] == '326150') |
                (regionNAICS['naics'] == '326160') |
                (regionNAICS['naics'] == '326191') |
                (regionNAICS['naics'] == '326192') |
                (regionNAICS['naics'] == '326199') |
                (regionNAICS['naics'] == '339994') |
                (regionNAICS['naics'] == '325211') |
                (regionNAICS['naics'] == '326112') |
                (regionNAICS['naics'] == '326113') |
                (regionNAICS['naics'] == '326121') |
                (regionNAICS['naics'] == '326130') |
                (regionNAICS['naics'] == '333220')
                , 'cluster'] = 38

#Printing Services
regionNAICS.loc[(regionNAICS['naics'] == '325910') |
                (regionNAICS['naics'] == '323121') |
                (regionNAICS['naics'] == '323122') |
                (regionNAICS['naics'] == '323110') |
                (regionNAICS['naics'] == '323111') |
                (regionNAICS['naics'] == '323112') |
                (regionNAICS['naics'] == '323113') |
                (regionNAICS['naics'] == '323115') |
                (regionNAICS['naics'] == '323116') |
                (regionNAICS['naics'] == '323117') |
                (regionNAICS['naics'] == '323118') |
                (regionNAICS['naics'] == '323119') |
                (regionNAICS['naics'] == '511191') 
                , 'cluster'] = 39

#Production Technology and Heavy Machinery
regionNAICS.loc[(regionNAICS['naics'] == '333210') |
                (regionNAICS['naics'] == '333291') |
                (regionNAICS['naics'] == '333292') |
                (regionNAICS['naics'] == '333293') |
                (regionNAICS['naics'] == '333294') |
                (regionNAICS['naics'] == '333298') |
                (regionNAICS['naics'] == '333993') |
                (regionNAICS['naics'] == '333999') |
                (regionNAICS['naics'] == '333111') |
                (regionNAICS['naics'] == '333112') |
                (regionNAICS['naics'] == '333120') |
                (regionNAICS['naics'] == '333131') |
                (regionNAICS['naics'] == '333611') |
                (regionNAICS['naics'] == '333612') |
                (regionNAICS['naics'] == '333613') |
                (regionNAICS['naics'] == '333618') |
                (regionNAICS['naics'] == '336510') |
                (regionNAICS['naics'] == '333411') |
                (regionNAICS['naics'] == '333412') |
                (regionNAICS['naics'] == '333414') |
                (regionNAICS['naics'] == '333415') |
                (regionNAICS['naics'] == '333311') |
                (regionNAICS['naics'] == '333312') |
                (regionNAICS['naics'] == '333319') |
                (regionNAICS['naics'] == '333921') |
                (regionNAICS['naics'] == '333922') |
                (regionNAICS['naics'] == '333923') |
                (regionNAICS['naics'] == '333924') |
                (regionNAICS['naics'] == '332911') |
                (regionNAICS['naics'] == '332912') |
                (regionNAICS['naics'] == '332919') |
                (regionNAICS['naics'] == '332991') |
                (regionNAICS['naics'] == '332997') |
                (regionNAICS['naics'] == '333911') |
                (regionNAICS['naics'] == '333912') |
                (regionNAICS['naics'] == '333913') |
                (regionNAICS['naics'] == '333913') |   #added due to 2017 NAICS change
                (regionNAICS['naics'] == '333994') |
                (regionNAICS['naics'] == '333995') |
                (regionNAICS['naics'] == '333996') |
                (regionNAICS['naics'] == '333997') |
                (regionNAICS['naics'] == '339991') 
                , 'cluster'] = 40

#Recreational and Small Electric Goods
regionNAICS.loc[(regionNAICS['naics'] == '337920') |
                (regionNAICS['naics'] == '339992') |
                (regionNAICS['naics'] == '339993') |
                (regionNAICS['naics'] == '339999') |
                (regionNAICS['naics'] == '339931') |
                (regionNAICS['naics'] == '339932') |
                (regionNAICS['naics'] == '336991') |
                (regionNAICS['naics'] == '339920') |
                (regionNAICS['naics'] == '333313') |
                (regionNAICS['naics'] == '333315') |
                (regionNAICS['naics'] == '339941') |
                (regionNAICS['naics'] == '339942') |
                (regionNAICS['naics'] == '339943') |
                (regionNAICS['naics'] == '339944') |
                (regionNAICS['naics'] == '335211')
                , 'cluster'] = 41

#Textile Manufacturing
regionNAICS.loc[(regionNAICS['naics'] == '313111') |
                (regionNAICS['naics'] == '313112') |
                (regionNAICS['naics'] == '313113') |
                (regionNAICS['naics'] == '313210') |
                (regionNAICS['naics'] == '313221') |
                (regionNAICS['naics'] == '313222') |
                (regionNAICS['naics'] == '313230') |
                (regionNAICS['naics'] == '313241') |
                (regionNAICS['naics'] == '313249') |
                (regionNAICS['naics'] == '313311') |
                (regionNAICS['naics'] == '313312') |
                (regionNAICS['naics'] == '313320') |
                (regionNAICS['naics'] == '315111') |
                (regionNAICS['naics'] == '315119') |
                (regionNAICS['naics'] == '315191') |
                (regionNAICS['naics'] == '315192') |
                (regionNAICS['naics'] == '314110') |
                (regionNAICS['naics'] == '314121') |
                (regionNAICS['naics'] == '314129') |
                (regionNAICS['naics'] == '314991') |
                (regionNAICS['naics'] == '314992') |
                (regionNAICS['naics'] == '325221') |
                (regionNAICS['naics'] == '325222')
                , 'cluster'] = 42

#Tobacco
regionNAICS.loc[(regionNAICS['naics'] == '312210') |
                (regionNAICS['naics'] == '312221') |
                (regionNAICS['naics'] == '312229')
                , 'cluster'] = 43

#Trailers, Motor Homes, and Appliances
regionNAICS.loc[(regionNAICS['naics'] == '336212') |
                (regionNAICS['naics'] == '336213') |
                (regionNAICS['naics'] == '336214') |
                (regionNAICS['naics'] == '339995') |
                (regionNAICS['naics'] == '335212') |
                (regionNAICS['naics'] == '335221') |
                (regionNAICS['naics'] == '335222') |
                (regionNAICS['naics'] == '335224') |
                (regionNAICS['naics'] == '335220') |   #added due to 2017 NAICS change
                (regionNAICS['naics'] == '335228') 
                , 'cluster'] = 44

#Transportation and Logistics
regionNAICS.loc[(regionNAICS['naics'] == '481111') |
                (regionNAICS['naics'] == '481112') |
                (regionNAICS['naics'] == '481212') |
                (regionNAICS['naics'] == '488111') |
                (regionNAICS['naics'] == '488119') |
                (regionNAICS['naics'] == '488190') |
                (regionNAICS['naics'] == '481211') |
                (regionNAICS['naics'] == '481219') |
                (regionNAICS['naics'] == '488210') |
                (regionNAICS['naics'] == '488490') |
                (regionNAICS['naics'] == '488510') |
                (regionNAICS['naics'] == '488991') |
                (regionNAICS['naics'] == '488999') |
                (regionNAICS['naics'] == '484121') |
                (regionNAICS['naics'] == '484230') |
                (regionNAICS['naics'] == '485210') |
                (regionNAICS['naics'] == '485510') 
                , 'cluster'] = 45

#Upstream Chemical Products
regionNAICS.loc[(regionNAICS['naics'] == '325110') |
                (regionNAICS['naics'] == '325191') |
                (regionNAICS['naics'] == '325192') |
                (regionNAICS['naics'] == '325193') |
                (regionNAICS['naics'] == '325199') |
                (regionNAICS['naics'] == '325212') |
                (regionNAICS['naics'] == '325181') |
                (regionNAICS['naics'] == '325182') |
                (regionNAICS['naics'] == '325188') |
                (regionNAICS['naics'] == '325120') |
                (regionNAICS['naics'] == '325312') |
                (regionNAICS['naics'] == '325320') 
                , 'cluster'] = 46

#Upstream Metal Manufacturing
regionNAICS.loc[(regionNAICS['naics'] == '331111') |
                (regionNAICS['naics'] == '331112') |
                (regionNAICS['naics'] == '332111') |
                (regionNAICS['naics'] == '331221') |
                (regionNAICS['naics'] == '331311') |
                (regionNAICS['naics'] == '331312') |
                (regionNAICS['naics'] == '331314') |
                (regionNAICS['naics'] == '331315') |
                (regionNAICS['naics'] == '331316') |
                (regionNAICS['naics'] == '331319') |
                (regionNAICS['naics'] == '331411') |
                (regionNAICS['naics'] == '331419') |
                (regionNAICS['naics'] == '331421') |
                (regionNAICS['naics'] == '331422') |
                (regionNAICS['naics'] == '331423') |
                (regionNAICS['naics'] == '331491') |
                (regionNAICS['naics'] == '331492') |
                (regionNAICS['naics'] == '332112') |
                (regionNAICS['naics'] == '331210') |
                (regionNAICS['naics'] == '332115') |
                (regionNAICS['naics'] == '332116') |
                (regionNAICS['naics'] == '332117') |
                (regionNAICS['naics'] == '331222') |
                (regionNAICS['naics'] == '332611') |
                (regionNAICS['naics'] == '332612') |
                (regionNAICS['naics'] == '332618') 
                , 'cluster'] = 47


#Video Production and Distribution
regionNAICS.loc[(regionNAICS['naics'] == '334612') |
                (regionNAICS['naics'] == '512110') |
                (regionNAICS['naics'] == '512120') |
                (regionNAICS['naics'] == '512132') |
                (regionNAICS['naics'] == '512191') |
                (regionNAICS['naics'] == '512199')
                , 'cluster'] = 48

#Vulcanized and Fired Materials
regionNAICS.loc[(regionNAICS['naics'] == '327111') |
                (regionNAICS['naics'] == '327112') |
                (regionNAICS['naics'] == '327113') |
                (regionNAICS['naics'] == '327121') |
                (regionNAICS['naics'] == '327122') |
                (regionNAICS['naics'] == '327123') |
                (regionNAICS['naics'] == '327124') |
                (regionNAICS['naics'] == '327125') |
                (regionNAICS['naics'] == '327992') |
                (regionNAICS['naics'] == '327211') |
                (regionNAICS['naics'] == '327212') |
                (regionNAICS['naics'] == '327215') |
                (regionNAICS['naics'] == '326211') |
                (regionNAICS['naics'] == '326212') |
                (regionNAICS['naics'] == '326220') |
                (regionNAICS['naics'] == '326291') |
                (regionNAICS['naics'] == '326299') 
                , 'cluster'] = 49

#Water Transportation
regionNAICS.loc[(regionNAICS['naics'] == '483112') |
                (regionNAICS['naics'] == '483114') |
                (regionNAICS['naics'] == '483212') |
                (regionNAICS['naics'] == '483111') |
                (regionNAICS['naics'] == '483113') |
                (regionNAICS['naics'] == '483211') |
                (regionNAICS['naics'] == '488310') |
                (regionNAICS['naics'] == '488320') |
                (regionNAICS['naics'] == '488330') |
                (regionNAICS['naics'] == '488390') |
                (regionNAICS['naics'] == '336611') |
                (regionNAICS['naics'] == '336612') 
                , 'cluster'] = 50

#Wood Products
regionNAICS.loc[(regionNAICS['naics'] == '321113') |
                (regionNAICS['naics'] == '321114') |
                (regionNAICS['naics'] == '321912') |
                (regionNAICS['naics'] == '321211') |
                (regionNAICS['naics'] == '321212') |
                (regionNAICS['naics'] == '321213') |
                (regionNAICS['naics'] == '321214') |
                (regionNAICS['naics'] == '321219') |
                (regionNAICS['naics'] == '321911') |
                (regionNAICS['naics'] == '321918') |
                (regionNAICS['naics'] == '321920') |
                (regionNAICS['naics'] == '321999') |                
                (regionNAICS['naics'] == '321992') 
                , 'cluster'] = 51

regionNAICS


# # Remove local industries (NAICS that do not fit into economic cluster)

# In[5]:


tradedcluster_naics = regionNAICS.loc[regionNAICS['cluster'] != 0]

tradedcluster_naics.dtypes


# In[6]:


tradedcluster_naics


# In[7]:


tradedcluster_naics.set_index('cluster')
tradedcluster_naics.dtypes


# # Import economic cluster .csv for Indexing

# In[8]:


cluster_index = pd.read_csv(r"G:\My Drive\BCarney\DataAnalysis\CBP_2017\NAICS_AllDigits\USClusterMapping_EconomicClusters.csv", index_col = 'cluster')
cluster_index


# # Sum employment by cluster

# In[9]:


clusters = tradedcluster_naics.groupby('cluster').sum()
clusters


# # Left Join Index with Economic Cluster Totals

# In[10]:


clusters_joined = pd.merge(cluster_index, clusters, how= "left", left_on='cluster', right_on='cluster')
region_clustertotal = clusters_joined[['description', 'emp']]
region_clustertotal


# # Export to .csv

# In[11]:


region_clustertotal.to_csv(r"G:\My Drive\BCarney\DataAnalysis\CBP_2017\NAICS_AllDigits\DVRPC_region\region_clustertotal.csv")


# In[ ]:




