import streamlit  as st 
import pandas as pd 
import plotly.express as px


def rate_calc(confirmed, deaths, recovered):
	st.title('Recovery & Death Rates')
	cz = confirmed.copy()
	dz = deaths.copy()
	rz = recovered.copy()
	cx = modify_df(cz)
	dx = modify_df(dz)
	rx = modify_df(rz)
	rate_df = pd.DataFrame()
	rate_df['Country'] = cx['Country/Region']
	rate_df['confirmed'] = cx[cx.columns[-1]]
	rate_df['deaths'] = dx[dx.columns[-1]]
	rate_df['recovered'] = rx[rx.columns[-1]]
	rate_df['death_rate'] = (rate_df['deaths'] /rate_df['confirmed']) *100
	rate_df['recovered_rate']= (rate_df['recovered'] / rate_df['confirmed']) * 100
	cz = cz.groupby('Country/Region').sum()
	cz = cz.reset_index()
	st.write('''
		### INFO :

		I have used the following formulas for calculations. 

		Recovery Rate = Recovered / Confirmed Cases before the last X days

		Death Rate = Deaths / Confirmed Cases before the last X days

		You can make custom selection of the number of Days (X) using the slider below.

		''')
	n = st.slider('Select No of Days : ',3,10,5)
	st.success(f'You have chosen to Plot the Recovery Rate of the past {n} days')
	st.subheader(f'Recovery Rates for the past {n} days')
	recovery_rate_n(rate_df,n,cz)
	q= st.slider('Select No of Days : ',3,50,5)
	st.success(f'You have chosen to Plot the Death Rate of the past {q} days')
	st.subheader(f'Death Rates for the past {q} days')
	death_rate_n(rate_df,q,cz)


def modify_df(cz):
	cz.drop(['Province/State','Lat','Long'], axis=1, inplace=True)
	cc = cz.groupby('Country/Region').sum()
	cc=cc.reset_index()	
	return cc


def recovery_rate_n (rate_df,n,cz):
	cz['rec'] = rate_df['recovered']	
	m = n+1
	cz['Recovery Rate in Percentage'] = (cz[cz.columns[-1]]/cz[cz.columns[-m]]) * 100		
	cz = cz.sort_values(by='rec', ascending=False)
	cz['Recovery Rate in Percentage'] = cz['Recovery Rate in Percentage'].apply(lambda x : '%.2f' %x)
	fig = px.bar(cz[:20], x='Recovery Rate in Percentage', y='Country/Region', orientation='h', text='Recovery Rate in Percentage',color_discrete_sequence=['blue'],width=800,height=600)	
	st.plotly_chart(fig,use_container_width=True)
	

def death_rate_n (rate_df,q,cz):
	cz['dea'] = rate_df['deaths']	
	m = q+1
	cz['Death Rate in Percentage'] = (cz[cz.columns[-1]]/cz[cz.columns[-m]]) * 100	
	cz = cz.sort_values(by='dea', ascending=False)
	cz['Death Rate in Percentage'] = cz['Death Rate in Percentage'].apply(lambda x : '%.2f' %x)
	fig2 = px.bar(cz[:20], x='Death Rate in Percentage', y='Country/Region', orientation='h', text='Death Rate in Percentage',color_discrete_sequence=['red'],width=800,height=600)	
	st.plotly_chart(fig2,use_container_width=True)
	
	
	

	
	





