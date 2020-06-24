import streamlit as st
import plotly.express as px
import pandas as pd

def mapping(c,confirmed, deaths, recovered):
	st.title('GEOGRAPHICAL MAP VISUALIZATION ')
	cc = c.copy()	
	c5 = confirmed.copy()
	d5 = deaths.copy()
	r5 = recovered.copy()
	countries = cc.Country.values
	dd = pd.read_csv('https://raw.githubusercontent.com/iamsrilakshmi/CoViz/master/wikipedia-iso-country-codes.csv')
	dd.sort_values(by = 'Country', inplace = True)
	df2 = pd.DataFrame()
	df2['Country'] = dd['Country']
	df2['iso_alpha'] = dd['iso_alpha']
	filtered_iso = df2[df2['Country'].isin(countries)]
	filtered_iso = filtered_iso.reset_index()
	filtered_iso.drop(['index'], axis=1,inplace=True)
	fi = filtered_iso.copy()
	map_df = pd.merge(cc, fi, on='Country')
	c5.rename(columns={'Country/Region':'Country'},inplace=True)
	d5.rename(columns={'Country/Region':'Country'},inplace=True)
	r5.rename(columns={'Country/Region':'Country'},inplace=True)
	cu = 'confirmed'
	du = 'deaths'
	ru = 'recovered'
	au = 'active'
	ct = 'Total Confirmed Cases'
	dt = 'Total Unfortunate Deaths' 
	rt = 'Total People Recovered'
	at = 'Total Active Cases'
	ctt = "Today's Confirmed Cases"
	dtt = "Today's Unfortunate Deaths" 
	rtt = 'People Recovered Today'
	map_plot(map_df,cu,ct)
	map_plot(map_df,du,dt)
	map_plot(map_df,ru,rt)
	map_plot(map_df,au,at)
	st.title("New Cases - Today")
	map_today(c5,fi,ctt)
	map_today(d5,fi,dtt)
	map_today(r5,fi,rtt)


def map_plot(map_df, col,ta):
	fig= px.choropleth(map_df, locations="iso_alpha",
                    color=col, hover_name="Country", 
                    color_continuous_scale=px.colors.sequential.Rainbow, 
                    width=800,height=500,title = ta)
	st.plotly_chart(fig)

def map_today(c5,fi,ctt):
	c9= c5.copy()	
	c9 = c9.groupby('Country').sum()
	c9=c9.diff(axis=1)
	c9=c9.reset_index()
	c9 = pd.merge(c9,fi, on='Country')
	col = c9[c9.columns[-2]]		
	fig5 = px.scatter_geo(c9, locations="iso_alpha", color=col,
	                     hover_name="Country", size=col,
	                     projection="natural earth", width=850,height=500,size_max=60,
	                     color_continuous_scale=px.colors.sequential.Rainbow, title = ctt)
	st.plotly_chart(fig5)






	
	

