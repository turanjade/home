from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import numpy as np

st.title('Welcome! This is Ran Tu')
if st.sidebar.button('Education'):
  st.header('Education')
  st.subheader('2016-2020, PhD, Civil Engineering, University of Toronto')
  st.subheader('Supervisor: Marianne Hatzopoulou')
  st.write(' ')
  st.subheader('2014-2016, Master of Science, Civil Engineering, Virginia Tech')
  st.subheader('Supervisor: Hesham Rakha')
  st.write(' ')
  st.subheader('2013-2014, Exchange, Civil Engineering, EPFL')
  st.write(' ')
  st.subheader('2010-2014, Bachelor of Engineering, Civil Engineering, Tongji University')
  st.subheader('Supervisor: Chao Yang')
  
if st.sidebar.button('Working experience'):
  st.header('Working experience')
  st.subheader('2021-current, Associate Professor, School of Transportation, Southeast University')
  st.subheader('2020, Postdoctoral fellow, Civil Engineering, University of Toronto')
