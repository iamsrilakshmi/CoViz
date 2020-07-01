import streamlit  as st 
import pandas as pd 
import plotly.express as px
import seaborn as sns



def bloodgroupanalysis(confirmed, deaths, recovered):
	st.title('BLOOD GROUP WISE DEATH RATES')
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
	n = st.slider('Select No of Days : ',3,15,10)
	st.success(f'You have chosen to Plot Blood Group wise Death Rate of the past {n} days')
	death_rate_n(rate_df,n,cz)


	
def modify_df(cz):
	cz.drop(['Province/State','Lat','Long'], axis=1, inplace=True)
	cc = cz.groupby('Country/Region').sum()
	cc=cc.reset_index()	
	return cc



def death_rate_n (rate_df,n,cz):
	cz['dea'] = rate_df['deaths']	
	m = n+1
	cz['Death Rate in Percentage'] = (cz[cz.columns[-1]]/cz[cz.columns[-m]]) * 100	
	cz = cz.sort_values(by='dea', ascending=False)
	cz['Death Rate in Percentage'] = cz['Death Rate in Percentage'].apply(lambda x : '%.2f' %x)	
	dr = pd.DataFrame()
	dr['Country'] = cz['Country/Region']
	dr['Death Rate in Percentage'] = cz['Death Rate in Percentage']
	dr = dr.reset_index()	
	bld = pd.read_csv('https://raw.githubusercontent.com/iamsrilakshmi/CoViz/master/blood.csv')
	b = bld.copy()	
	b.set_index('Country', inplace=True)
	b = b.apply(lambda x : x.str.strip(' %'))	
	blood_df = pd.merge(b, dr, on='Country')
	bcd = blood_df.copy()
	blood_df = blood_df[['Country','O+','O-','A+','A-', 'B+','B-','AB+','AB-','Rh-Positive','Rh-Negative','Death Rate in Percentage']]
	cols = blood_df.columns[1:-1]
	cols = cols.tolist()	
	for i in cols:
		blood_df[i] = blood_df[i].astype('float64')
	blood_df['Death Rate in Percentage'] = blood_df['Death Rate in Percentage'].astype('float64')
	Pearson = []
	for i in cols:
		Pearson.append(blood_df[i].corr(blood_df['Death Rate in Percentage']))
	corr_df = pd.DataFrame({
		"Blood Group" : cols,
		"Pearson's r" : Pearson
		})
	st.subheader('Correlation Coefficients of Death Rate vs Blood Group')
	st.write(corr_df)
	st.subheader(f'BLOOD GROUP WISE DEATH RATES for the past {n} days')
	for i in cols:
		st.subheader(f'Death Rate in Percentage vs {i} Blood Group')		
		fig = sns.regplot(x = i, y ='Death Rate in Percentage', data = blood_df )
		st.write(fig,use_container_width=True)
		st.pyplot()
	st.markdown('''### Reference :
	For more information on how blood group determines the coronavirus death rates, 
	do visit [here](https://www.healthline.com/health-news/does-your-blood-type-increase-your-risk-for-coronavirus)
		    ''' )


	
		

	
	








