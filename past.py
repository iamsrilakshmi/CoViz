import streamlit  as st 
import plotly.express as px 


def past_patterns(c2):
	st.title('PAST PATTERNS OF THE GLOBAL DATA ')
	if st.checkbox('Choose No of Days '):
		n = st.slider('Select No.of Days to Visualise',5,150,60)
		st.success(f'You have chosen to Plot the Global data of the past {n} days')
		d = 'date'
		cu = 'confirmed'
		du = 'deaths'
		ru = 'recovered'
		au = 'active'
		st.subheader(f'Confirmed Cases in the past {n} days in the World ')
		choose_days(c2,n, d,cu)
		st.subheader(f'Unfortunate Deaths in the past {n} days in the World ')
		choose_days(c2,n, d,du)
		st.subheader(f'People Recovered in the past {n} days in the World ')
		choose_days(c2,n, d,ru)
		st.subheader(f'Current/Active Cases in the past {n} days in the World ')
		choose_days(c2,n, d,au)
	st.subheader('Past Pattern of Confirmed Cases')
	st.line_chart(c2.confirmed)
	st.subheader('Past Pattern of Unfortunate Deaths')
	st.line_chart(c2.deaths)
	st.subheader('Past Pattern of Recovered People')
	st.line_chart(c2.recovered)
	st.subheader('Past Pattern of Active Cases')	
	st.line_chart(c2.active)


def choose_days(c2,n, d,col):
	past_data = px.line(c2[-n:], x=d, y=col)
	st.plotly_chart(past_data)
