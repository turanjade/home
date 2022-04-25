from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import numpy as np


url_rg = "https://www.researchgate.net/profile/Ran-Tu-3"
url_gs = 'https://scholar.google.com/citations?user=ueR4KsUAAAAJ&hl=en'
#st.write("check out this [link](%s)" % url)

st.title('Welcome! This is Ran Tu')

#st.sidebar.header('Dictionary')
  
#if st.sidebar.button('Return to home'):
#  st.title(' ')

st.sidebar.header('Dictionary')
genre = st.sidebar.radio(
     "Direct to:",
     ('Home', 'Education', 'Working experience', 'Projects', 'Teaching', 'Studnets', 'Publication'))

if genre == 'Home':
  st.title(' ')
if genre == 'Education':
  st.subheader('Education')
  st.write('1. 2016-2020, PhD, Civil Engineering, University of Toronto')
  st.write(str('   '+ 'Supervisor: Marianne Hatzopoulou'))
  st.write(' ')
  st.write('2. 2014-2016, Master of Science, Civil Engineering, Virginia Tech')
  st.write(str('   '+ 'Supervisor: Hesham Rakha'))
  st.write(' ')
  st.write('3. 2013-2014, Exchange, Civil Engineering, EPFL')
  st.write(' ')
  st.write('4. 2010-2014, Bachelor of Engineering, Civil Engineering, Tongji University')
  st.write(str('   '+ 'Supervisor: Chao Yang'))

if genre == 'Working experience':
  st.subheader('Working experience')
  st.write('1. 2021-current, Associate Professor, School of Transportation, Southeast University')
  st.write('2. 2020, Postdoctoral fellow, Civil Engineering, University of Toronto')

if genre == 'Projects':
  with st.expander("Current projects"):
    st.write("1. Eco-driving Guidance Decision Modelling Based on Drivers' Dynamic Cognitive Behaviour, National Natural Science Foundation of China (Young Scholar), PI, 2022-2024")
    st.write("2. Eco-driving Guidance Based on the Heterogeneity of Drivers’ Cognitive Workload, Natural Science Foundation of Jiangsu Province (Young Scholar), PI, 2021-2024")
    st.write("3. Modify Drivers' behaviour to Adapt for Lower Emissions, National Key R&D Program of China, Co-PI, 2021-2024")
    st.write("4. Dynamic Optimization of Electric Bus Services with Energy Consumption Uncertainties, FAW-Volkswagen China Environmental Protection Foundation Automotive Environmental Innovation Leading Program, PI, 2022-2023")          
  with st.expander('Past projects'):
    st.write('1. Eco-Score: environmental evaluation of driving operations, NSERC of Canada, Participation, 2019-2020')

if genre == 'Teaching':
  st.subheader('Courses')
  st.write("2nd-year undergraduate in the major of transportation, Transportation Management")
    
if genre == 'Students':
  st.write(' ')

  
