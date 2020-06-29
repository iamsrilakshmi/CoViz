import streamlit as st 
import pandas as pd
import today 
import rates
import bloodgroup
import past
import one_country
import new_cases
import mapviz
import percent
import guide

st.markdown("<h1 style='text-align: center; color: red;'>CoViz</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; color: green;font-weight:bold;'>Corona Virus Visualization - 2020</h2>", unsafe_allow_html=True)
menus = ['Current Updates','Rates', 'Blood Group','Top 10','New Cases', 'Past Patterns','Your Country','Map','Info']
st.sidebar.header('MENU')
menu = st.sidebar.radio('View',menus)
st.sidebar.subheader('Author')
st.sidebar.markdown("### [Sri Lakshmi](https://sites.google.com/view/srilakshmi)")
st.sidebar.info('Machine/ Deep Learning Researcher, Engineer')
st.sidebar.markdown("#### [Contact Author](https://sites.google.com/view/srilakshmi/contact)")

@st.cache(show_spinner = False)
def get_data():
	confirmed = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv')
	deaths = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv')
	recovered = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv')
	return confirmed, deaths, recovered
confirmed, deaths, recovered = get_data()

@st.cache(show_spinner = False)
def country_wise(confirmed, deaths, recovered):
	c = pd.melt(confirmed, id_vars=confirmed.iloc[:, :4], var_name='date', value_name='confirmed')
	d = pd.melt(deaths, id_vars=confirmed.iloc[:, :4], var_name='date', value_name='deaths')
	r = pd.melt(recovered, id_vars=confirmed.iloc[:, :4], var_name='date', value_name='recovered')
	c['deaths']=d['deaths']
	c.drop(['Province/State','Lat','Long'], axis=1, inplace=True) 
	c.rename(columns={'Country/Region':'Country'}, inplace=True)
	c=c.groupby('Country').max().reset_index()
	r.drop(['Province/State','Lat','Long'], axis=1, inplace=True) 
	r.rename(columns={'Country/Region':'Country'}, inplace=True)
	r=r.groupby('Country').mean().reset_index()
	r2=r['recovered'].astype('int')
	r.drop(['recovered'],axis=1,inplace=True)
	r['recovered']=r2.values
	c['recovered'] = r['recovered']
	c['active'] = c['confirmed']-c['deaths']-c['recovered']
	return c 
c = country_wise(confirmed, deaths, recovered)

@st.cache(show_spinner = False)
def date_wise(confirmed, deaths, recovered):
	c2 = pd.melt(confirmed, id_vars=confirmed.iloc[:, :4], var_name='date', value_name='confirmed')
	d2 = pd.melt(deaths, id_vars=confirmed.iloc[:, :4], var_name='date', value_name='deaths')
	r2 = pd.melt(recovered, id_vars=confirmed.iloc[:, :4], var_name='date', value_name='recovered')
	c2['deaths']=d2['deaths']
	c2['recovered']= r2['recovered']
	c2['active'] = c2['confirmed']-c2['deaths']-c2['recovered']
	c2 = c2.groupby('date').sum().reset_index()
	c2.drop(['Lat','Long'], axis=1, inplace=True)
	c2['date'] = pd.to_datetime(c2.date)
	c2 = c2.sort_values(by='date')
	return c2
c2 = date_wise(confirmed, deaths, recovered)


if menu =='Current Updates':
	today.current_updates(c)
elif menu == 'Rates':
	rates.rate_calc(confirmed, deaths, recovered)
elif menu == 'Blood Group':
	bloodgroup.bloodgroupanalysis(confirmed, deaths, recovered)	
elif menu == 'Top 10':
	percent.percent_pie(c)
elif menu == 'Past Patterns':
	past.past_patterns(c2)
elif menu == 'Your Country':
	one_country.select_your_country(confirmed, deaths, recovered,c)
elif menu == 'New Cases':
	new_cases.new_cases_today(confirmed, deaths, recovered)
elif menu == 'Map':
	mapviz.mapping(c,confirmed, deaths, recovered)
elif menu == 'Info':
	guide.from_author()

