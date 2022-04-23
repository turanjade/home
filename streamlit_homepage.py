from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import numpy as np

st.title('Welcome! This is Ran Tu')

st.sidebar.header('Dictionary')
if st.sidebar.button('Education'):
  st.subheader('Education')
  st.write('2016-2020, PhD, Civil Engineering, University of Toronto')
  st.write('Supervisor: Marianne Hatzopoulou')
  st.write(' ')
  st.write('2014-2016, Master of Science, Civil Engineering, Virginia Tech')
  st.write('Supervisor: Hesham Rakha')
  st.write(' ')
  st.write('2013-2014, Exchange, Civil Engineering, EPFL')
  st.write(' ')
  st.write('2010-2014, Bachelor of Engineering, Civil Engineering, Tongji University')
  st.write('Supervisor: Chao Yang')
  
if st.sidebar.button('Working experience'):
  st.subheader('Working experience')
  st.write('2021-current, Associate Professor, School of Transportation, Southeast University')
  st.write('2020, Postdoctoral fellow, Civil Engineering, University of Toronto')
