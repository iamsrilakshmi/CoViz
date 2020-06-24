import streamlit as st
import plotly.express as px
import pandas as pd

def percent_pie(c):
	st.title("TODAY'S TOP 10 COUNTRIES")
	high_to_low_confirmed2 = c.sort_values(by='confirmed', ascending=False).reset_index()
	high_to_low_confirmed2.drop('index', axis=1, inplace=True)
	hl = high_to_low_confirmed2.copy()
	if st.checkbox('Show Table'):
		st.write(hl[:10])
	high_to_low_recovered2 = c.sort_values(by='recovered', ascending=False).reset_index()
	high_to_low_recovered2.drop('index', axis=1, inplace=True)
	high_to_low_deaths2 = c.sort_values(by='deaths', ascending=False).reset_index()
	high_to_low_deaths2.drop('index', axis=1, inplace=True)
	high_to_low_active3= c.sort_values(by='active', ascending=False).reset_index()
	high_to_low_active3.drop('index', axis=1, inplace=True)
	fig = px.pie(high_to_low_confirmed2[:10], values='confirmed', names='Country',
	             title='Country Wise Percentage of Confirmed Cases',
	             hover_data=['active'], height=600, width=850,color_discrete_sequence=px.colors.qualitative.G10)
	fig.update_traces(textposition='inside', textinfo='percent+label')
	st.plotly_chart(fig)
	fig2 = px.pie(high_to_low_recovered2[:10], values='deaths', names='Country',
	             title='Country Wise Percentage of Unfortunate Deaths',
	             hover_data=['recovered'], height=600, width=850,color_discrete_sequence=px.colors.qualitative.Plotly)
	fig2.update_traces(textposition='inside', textinfo='percent+label')
	st.plotly_chart(fig2)
	fig3 = px.pie(high_to_low_deaths2[:10], values='recovered', names='Country',
	             title='Country Wise Percentage of Recovered People',
	             hover_data=['active'], height=600, width=850,color_discrete_sequence=px.colors.qualitative.G10)
	fig3.update_traces(textposition='inside', textinfo='percent+label')
	st.plotly_chart(fig3)
	fig4 = px.pie(high_to_low_active3[:10], values='active', names='Country',
	             title='Country Wise Percentage of Currently Active Cases',
	             hover_data=['recovered'], height=600, width=850,color_discrete_sequence=px.colors.qualitative.Plotly)
	fig4.update_traces(textposition='inside', textinfo='percent+label')
	st.plotly_chart(fig4)
