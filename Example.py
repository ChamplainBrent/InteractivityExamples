import altair as alt
from vega_datasets import data
import streamlit as st

source = data.seattle_weather()

brush = alt.selection_interval(encodings=['x'])

bars = alt.Chart().mark_bar().encode(
    x='month(date):O',
    y='mean(precipitation):Q',
    opacity=alt.condition(brush, alt.OpacityValue(1), alt.OpacityValue(0.3)),
).add_params(
    brush
)

line = alt.Chart().mark_rule(color='firebrick').encode(
    y='mean(precipitation):Q',
    size=alt.SizeValue(3)
).transform_filter(
    brush
)

c = alt.layer(bars, line, data=source)

st.altair_chart(c, use_container_width=True
