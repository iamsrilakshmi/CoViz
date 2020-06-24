import streamlit  as st 
import pandas as pd 
import plotly.express as px


def current_updates(c):
	st.title('CURRENT UPDATES')
	cx = c.confirmed.sum()
	dx = c.deaths.sum()
	rx = c.recovered.sum()
	ax = c.active.sum()
	st.subheader(f'CONFIRMED = {cx} ')
	st.subheader(f'DEATHS = {dx}')
	st.subheader(f'RECOVERED = {rx} ')
	st.subheader(f'ACTIVE = {ax} ')
	n = st.slider('Select No.of Countries to Visualise',5,50,10)
	st.success(f"You have chosen to Plot Today's data of Top {n} Countries")
	high_to_low_confirmed2 = c.sort_values(by='confirmed', ascending=False).reset_index()
	high_to_low_confirmed2 .drop('index', axis=1, inplace=True)
	if st.checkbox('View Tabular Data'):
		st.write(high_to_low_confirmed2)
	high_to_low_recovered2 = c.sort_values(by='recovered', ascending=False).reset_index()
	high_to_low_recovered2.drop('index', axis=1, inplace=True)
	high_to_low_deaths2 = c.sort_values(by='deaths', ascending=False).reset_index()
	high_to_low_deaths2.drop('index', axis=1, inplace=True)
	high_to_low_active3= c.sort_values(by='active', ascending=False).reset_index()
	high_to_low_active3.drop('index', axis=1, inplace=True)
	st.markdown("<h3 style='text-align: center; color: red;font-weight:bold;'>Countries with Maximum Number of Confirmed cases of CoronaVirus </h2>", unsafe_allow_html=True)
	fig1= px.bar(high_to_low_confirmed2[:n], x='Country', y='confirmed',color="confirmed",color_continuous_scale=px.colors.sequential.Bluered,width=800,height=600)
	st.plotly_chart(fig1)
	st.markdown("<h3 style='text-align: center; color: blue;font-weight:bold;'> Countries with High Recovery Rates</h2>", unsafe_allow_html=True)
	fig2= px.bar(high_to_low_recovered2[:n], x='Country', y='recovered',color="recovered",color_continuous_scale=px.colors.sequential.thermal,width=800,height=600)
	st.plotly_chart(fig2)
	st.markdown("<h3 style='text-align: center; color: red;font-weight:bold;'> Countries with High Death Rates</h2>", unsafe_allow_html=True)
	fig3= px.bar(high_to_low_deaths2[:n], x='Country', y='deaths',color="deaths",color_continuous_scale=px.colors.sequential.solar,width=800,height=600)
	st.plotly_chart(fig3)
	st.markdown("<h3 style='text-align: center; color: orangered;font-weight:bold;'> Countries with High Active Cases</h2>", unsafe_allow_html=True)
	fig= px.bar(high_to_low_active3[:n], x='Country', y='active',color="active",color_continuous_scale=px.colors.sequential.Aggrnyl,width=800,height=600)
	st.plotly_chart(fig)
