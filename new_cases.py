import streamlit  as st 
import pandas as pd 
import plotly.express as px


def new_cases_today(confirmed, deaths, recovered):
	st.title('NEW CASES')
	n = st.slider('Choose the number of Countries to View ',5,25,10)
	st.success(f"You have chosen to View Top {n} Countries")
	cc = confirmed.copy()
	dd = deaths.copy()
	rr = recovered.copy()
	cu = 'confirmed'
	du = 'deaths'
	ru = 'recovered'
	color1 = '#D81B60'
	color2 = '#B71C1C'
	color3 = '#1B5E20'		
	st.subheader(f'Top {n} -  New Confirmed Cases')
	new_create(cc, cu,color1,n)
	st.subheader(f'Top {n} -New Deaths')
	new_create(dd, du,color2,n)
	st.subheader(f'Top {n} Countries in which People Recovered Today')
	new_create(rr, ru,color3,n)


def new_create(col, col_name,colorr,n):
	new1 = col.copy()
	new2 = new1[new1.columns[-1]] - new1[new1.columns[-2]] 	
	new3 = pd.DataFrame()
	new3['Country'] = new1['Country/Region']
	new3[col_name] = new2.values
	new3 = new3.sort_values(col_name).tail(n)	
	fig = px.bar(new3, x=col_name, y='Country', orientation='h', text=col_name,color_discrete_sequence=[colorr],width=800,height=600)	
	st.plotly_chart(fig)