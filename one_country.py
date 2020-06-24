import streamlit as st 
import numpy as np 
import pandas as pd 
import plotly.express as px 


def select_your_country(confirmed, deaths, recovered, c ):
	c5 = confirmed.copy()
	d5 = deaths.copy()
	r5 = recovered.copy()
	cc = c.copy()	
	n = st.slider('Select No.of Days to Visualise',5,60,10)
	countries = cc.Country.values.tolist()	
	country_sel = st.selectbox('Select Your Country', countries)
	st.success(f'You have chosen to Plot the data of the past {n} days of {country_sel} ')
	df = df_process(c5,country_sel)
	df2 = df_process(d5,country_sel)
	df3 = df_process(r5,country_sel)
	df['deaths'] = df2['values']
	df['recovered'] = df3['values']
	df.rename(columns={'values':'confirmed'}, inplace=True)
	df['active'] = df['confirmed']-df['deaths']-df['recovered']
	dff = df.copy()
	dff['date'] = pd.to_datetime(dff.date)
	if st.checkbox('Show Table'):
		dff = dff.sort_values(by='date', ascending=False)
		st.write(dff)
	st.header(f'Data Visualization of {country_sel}')
	cu = 'confirmed'
	du = 'deaths'
	ru = 'recovered'
	au = 'active'
	st.subheader(f'Confirmed Cases in the past {n} days in {country_sel} ')
	show_graph2(dff,n,cu)
	st.subheader(f'Unfortunate Deaths in the past {n} days in {country_sel} ')
	show_graph2(dff,n,du)
	st.subheader(f'People Recovered in the past {n} days in {country_sel} ')
	show_graph2(dff,n,ru)
	st.subheader(f'Current/Active Cases in the past {n} days in {country_sel} ')
	show_graph2(dff,n,au)
	st.header('RATE OF GROWTH/DECLINE')
	st.header(f'Everyday Data in {country_sel}')
	st.subheader(f'Day by Day - New Confirmed Cases in {country_sel}')
	rate_of_growth(c5,country_sel,n,cu)
	st.subheader(f'Day by Day - New Death Cases in {country_sel}')
	rate_of_growth(d5,country_sel,n,du)
	st.subheader(f'Day by Day - New Recovered Cases in {country_sel}')
	rate_of_growth(r5,country_sel,n,ru)


def df_process(df,country_sel) :
	df.drop(['Province/State','Lat','Long'], axis=1, inplace=True)
	df.rename(columns={'Country/Region':'Country'}, inplace=True)
	one_co = df[df.Country==country_sel]
	one_co = one_co.groupby('Country').sum().reset_index()
	your_country =one_co.T.reset_index()
	your_country = your_country[1:]
	your_country.columns=['date','values']
	return your_country


def show_graph2(df, n,cu):
	past_graph = px.line(df[-n:], x='date',y=cu)
	past_graph.update_traces(mode="markers+lines")
	st.plotly_chart(past_graph)


def rate_of_growth(c5,country_sel,n,cu):
	c9= c5.copy()
	c9 = c9.groupby('Country').sum() 
	c9=c9.diff(axis=1)	
	c9=c9.reset_index()
	one_co = c9[c9.Country==country_sel]
	one_co_T = one_co.T
	one_co_T=one_co_T[2:]
	one_co_T.columns=[cu]
	st.bar_chart(one_co_T[-n:])

