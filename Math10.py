#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 12:13:48 2021

@author: shibahime
"""

import streamlit as st
import numpy as np
import altair as alt

st.set_page_config(page_title="yuan chai",page_icon=":sparkling_heart:")
st.title(":hatching_chick: :purple_heart: :dango: :blossom: My first app :sparkling_heart: :unicorn_face: :orange_heart: :coconut: :bouquet:")

st.markdown("Yuan Chai, https://github.com/yuanchai9?tab=repositories, Yile Li https://github.com/YileLi2023")

try:
        
    filename = st.file_uploader("put csv", type = "csv")
    
    import pandas as pd
    df = pd.read_csv(filename)
    #st.write(df)
    
    df1 = df.applymap(lambda x: np.nan if x ==" " else x)
    #st.write(df1)

    def can_be_numeric(df1,c):
        try:
            pd.to_numeric(df1[c])
            return True
        except:
            return False
    
    good_cols = [c for c in df1.columns if can_be_numeric(df1,c)]
 
    
    df1[good_cols] = df1[good_cols].apply(pd.to_numeric, axis = 0)
    x_axis = st.selectbox("Choose ana x_value",good_cols)
    y_axis = st.selectbox("Choose ana y_value",good_cols)

    input_range = st.slider('row',0,len(df1),100)

    st.write(f"You have chosen {x_axis} as x_aixs, {y_axis} as y_axis")
    
    achart = alt.Chart(df1).mark_circle().encode(
        x = x_axis,
        y = y_axis,
        color = alt.Color(x_axis, scale=alt.Scale(scheme='pastel2')),
    ).properties(
        width = 400,
        height = 400,
    )
    st.altair_chart(achart, use_container_width=True)

    st.line_chart(df1[good_cols][:50])
    
except ValueError:
    st.write("value ERROR")

