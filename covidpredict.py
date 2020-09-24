import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import random
import math
import time 
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn.svm import SVR
from sklearn.metrics import mean_squared_error, mean_absolute_error
import datetime
import operator
plt.style.use('fivethirtyeight')
confirmed_cases=pd.read_csv('time_series_covid19_confirmed_global (1).csv')
confirmed_cases.head()
deaths_reported=pd.read_csv('time_series_covid19_deaths_global.csv')
deaths_reported.head()
recovered_cases=pd.read_csv('time_series_covid19_recovered_global.csv')
recovered_cases.head()
latest_data=pd.read_csv('latest.csv')
latest_data.head()
cols=confirmed_cases.keys()
cols
confirmed=confirmed_cases.loc[:,cols[4]:cols[-1]]
deaths=deaths_reported.loc[:,cols[4]:cols[-1]]
recoveries=recovered_cases.loc[:,cols[4]:cols[-1]]
dates=confirmed.keys()
world_cases=[]
total_deaths=[]
mortality_rate=[]
recovery_rate=[]
total_recovered=[]
total_active=[]

china_cases=[]
italy_cases=[]
us_cases=[]
spain_cases=[]
france_cases=[]
germany_cases=[]
uk_cases=[]
russia_cases=[]
india_cases=[]

china_deaths=[]
italy_deaths=[]
us_deaths=[]
spain_deaths=[]
france_deaths=[]
germany_deaths=[]
uk_deaths=[]
russia_deaths=[]
india_deaths=[]

china_recoveries=[]
italy_recoveries=[]
us_recoveries=[]
spain_recoveries=[]
france_recoveries=[]
germany_recoveries=[]
uk_recoveries=[]
russia_recoveries=[]
india_recoveries=[]

for i in dates:
 confirmed_sum=confirmed[i].sum()
 death_sum=deaths[i].sum()
 recovered_sum=recoveries[i].sum()
 
 world_cases.append(confirmed_sum)
 total_deaths.append(death_sum)
 total_recovered.append(recovered_sum)
 total_active.append(confirmed_sum-death_sum-recovered_sum)
 
 mortality_rate.append(death_sum/confirmed_sum)
 recovery_rate.append(recovered_sum/confirmed_sum)
 
 china_cases.append(confirmed_cases[confirmed_cases['Country/Region']=='China'][i].sum())
 italy_cases.append(confirmed_cases[confirmed_cases['Country/Region']=='Italy'][i].sum())
 us_cases.append(confirmed_cases[confirmed_cases['Country/Region']=='US'][i].sum())
 spain_cases.append(confirmed_cases[confirmed_cases['Country/Region']=='Spain'][i].sum())
 france_cases.append(confirmed_cases[confirmed_cases['Country/Region']=='France'][i].sum())
 germany_cases.append(confirmed_cases[confirmed_cases['Country/Region']=='Germany'][i].sum())
 uk_cases.append(confirmed_cases[confirmed_cases['Country/Region']=='United Kingdom'][i].sum())
 russia_cases.append(confirmed_cases[confirmed_cases['Country/Region']=='Russia'][i].sum())
 india_cases.append(confirmed_cases[confirmed_cases['Country/Region']=='India'][i].sum())
 
 china_deaths.append(deaths_reported[deaths_reported['Country/Region']=='China'][i].sum())
 italy_deaths.append(deaths_reported[deaths_reported['Country/Region']=='Itlay'][i].sum())
 us_deaths.append(deaths_reported[deaths_reported['Country/Region']=='US'][i].sum())
 spain_deaths.append(deaths_reported[deaths_reported['Country/Region']=='Spain'][i].sum())
 france_deaths.append(deaths_reported[deaths_reported['Country/Region']=='France'][i].sum())
 germany_deaths.append(deaths_reported[deaths_reported['Country/Region']=='Germany'][i].sum())
 uk_deaths.append(deaths_reported[deaths_reported['Country/Region']=='Unnited Kingdom'][i].sum())
 russia_deaths.append(deaths_reported[deaths_reported['Country/Region']=='Russia'][i].sum())
 india_deaths.append(deaths_reported[deaths_reported['Country/Region']=='India'][i].sum())
 
 china_recoveries.append(recovered_cases[recovered_cases['Country/Region']=='China'][i].sum())
 italy_recoveries.append(recovered_cases[recovered_cases['Country/Region']=='Italy'][i].sum())
 us_recoveries.append(recovered_cases[recovered_cases['Country/Region']=='US'][i].sum())
 spain_recoveries.append(recovered_cases[recovered_cases['Country/Region']=='Spain'][i].sum())
 france_recoveries.append(recovered_cases[recovered_cases['Country/Region']=='France'][i].sum())
 germany_recoveries.append(recovered_cases[recovered_cases['Country/Region']=='Germany'][i].sum())
 uk_recoveries.append(recovered_cases[recovered_cases['Country/Region']=='United Kingdom'][i].sum())
 russia_recoveries.append(recovered_cases[recovered_cases['Country/Region']=='Russia'][i].sum())
 india_recoveries.append(recovered_cases[recovered_cases['Country/Region']=='India'][i].sum())
 
world_cases
total_deaths
confirmed_sum
death_sum
recovered_sum
us_cases
india_cases
def daily_increase(data):
 d= []
 for i in range(len(data)):
 if i==0:
 d.append(data[0])
 else:
 d.append(data[i]-data[i-1])
 return d
 #confirmed cases
world_daily_increase = daily_increase(world_cases)
china_daily_increase = daily_increase(china_cases)
italy_daily_increase = daily_increase(italy_cases)
us_daily_increase = daily_increase(us_cases)
spain_daily_increase = daily_increase(spain_cases)
france_daily_increase = daily_increase(france_cases)
germany_daily_increase = daily_increase(germany_cases)
uk_daily_increase = daily_increase(uk_cases)
india_daily_increase = daily_increase(india_cases)

spain_daily_increase
germany_daily_increase

#deaths
world_daily_death = daily_increase(total_deaths)
china_daily_death = daily_increase(total_deaths)
italy_daily_death = daily_increase(total_deaths)
us_daily_death = daily_increase(total_deaths)
spain_daily_death = daily_increase(total_deaths)
france_daily_death = daily_increase(total_deaths)
germany_daily_death = daily_increase(total_deaths)
uk_daily_death = daily_increase(total_deaths)
india_daily_death = daily_increase(total_deaths)

china_daily_death
uk_daily_death

# recoveries
world_daily_recovery = daily_increase(total_recovered)
china_daily_recovery = daily_increase(total_recovered)
italy_daily_recovery = daily_increase(total_recovered)
us_daily_recovery = daily_increase(total_recovered)
spain_daily_recovery = daily_increase(total_recovered)
france_daily_recovery = daily_increase(total_recovered)
germany_daily_recovery = daily_increase(total_recovered)
uk_daily_recovery = daily_increase(total_recovered)
india_daily_recovery = daily_increase(total_recovered)

germany_daily_increase
spain_daily_increase

# deaths
world_daily_death = daily_increase(total_deaths)
china_daily_death = daily_increase(total_deaths)
italy_daily_death = daily_increase(total_deaths)
us_daily_death = daily_increase(total_deaths)
spain_daily_death = daily_increase(total_deaths)
france_daily_death = daily_increase(total_deaths)
germany_daily_death = daily_increase(total_deaths)
uk_daily_death = daily_increase(total_deaths)
india_daily_death = daily_increase(total_deaths)

china_daily_death
uk_daily_death

# recoveries
world_daily_recovery = daily_increase(total_recovered)
china_daily_recovery = daily_increase(total_recovered)
italy_daily_recovery = daily_increase(total_recovered)
us_daily_recovery = daily_increase(total_recovered)
spain_daily_recovery = daily_increase(total_recovered)
france_daily_recovery = daily_increase(total_recovered)
germany_daily_recovery = daily_increase(total_recovered)
uk_daily_recovery = daily_increase(total_recovered)
india_daily_recovery = daily_increase(total_recovered)

india_daily_recovery
world_daily_recovery
unique_countries = list(latest_data['Country_Region'].unique())
unique_countries

country_confirmed_cases=[]
country_death_cases=[]
country_active_cases=[]
country_recovery_cases=[]
country_mortality_rate=[]

no_cases=[]
for i in unique_countries:
 cases=latest_data[latest_data['Country_Region']==i]['Confirmed'].sum()
 if cases>0:
 country_confirmed_cases.append(cases)
 else:
 no_cases.append(i)

for i in no_cases:
 unique_countries.remove(i)
 
#sort countries by the number of confirmed cases
zipped = zip(unique_countries, country_confirmed_cases)
unique_countires=[k for k,v in sorted(zipped,key=operator.itemgetter(1),reverse=True)]
for i in range(len(unique_countries)):
 country_confirmed_cases[i]=latest_data[latest_data['Country_Region']==unique_countries[i]]['Confirmed'].sum()
 country_death_cases.append(latest_data[latest_data['Country_Region']==unique_countries[i]]['Deaths'].sum())
 country_recovery_cases.append(latest_data[latest_data['Country_Region']==unique_countries[i]]['Recovered'].sum())
 country_active_cases.append(country_confirmed_cases[i] - country_death_cases[i] - country_recovery_cases[i])
 country_mortality_rate.append(country_death_cases[i]/country_confirmed_cases[i])
country_df = pd.DataFrame({'Country Name':unique_countries, 'Number of confirmed cases': country_confirmed_cases, 'Number of deaths':country_death_cases,'Number of recoveries':country_recovery_cases,'Mortality rate':country_mortality_rate})
#no.of cases per country/region
country_df.style.background_gradient(cmap='Blues')
unique_provinces = list(latest_data['Province_State'].unique())

province_confirmed_cases=[]
province_country=[]
province_death_cases=[]
province_recovery_cases=[]
province_mortality_rate=[]

no_cases=[]
for i in unique_provinces:
 cases=latest_data[latest_data['Province_State']==i]['Confirmed'].sum()
 if cases > 0:
 province_confirmed_cases.append(i)
 else:
 no_cases.append(i)

for i in no_cases:
 unique_provinces.remove(i)

unique_provinces=[k for k , v in sorted(zip(unique_provinces,province_confirmed_cases),key=operator.itemgetter(1),reverse=True)]
for i in range(len(unique_provinces)):
 province_confirmed_cases[i]=latest_data[latest_data['Province_State']==unique_provinces[i]]['Confirmed'].sum()
 province_country.append(latest_data[latest_data['Province_State']==unique_provinces[i]]['Country_Region'].unique()[0])
 province_death_cases.append(latest_data[latest_data['Province_State']==unique_provinces[i]]['Deaths'].sum())
 province_recovery_cases.append(latest_data[latest_data['Province_State']==unique_provinces[i]]['Recovered'].sum())
 province_mortality_rate.append(province_death_cases[i]/province_confirmed_cases[i])
 
#no. of cases per province/state/city
province_df=pd.DataFrame({'Province/State Name':unique_provinces, 'Country': province_country,'Number of confirmed cases': province_confirmed_cases, 'Number of deaths':province_death_cases,'Number of recoveries':province_recovery_cases,'Mortality rate':province_mortality_rate})
province_df.style.background_gradient(cmap='Reds')

days_since_1_22 = np.array([i for i in range(len(dates))]).reshape(-1, 1)
world_cases = np.array(world_cases).reshape(-1, 1)
total_deaths = np.array(total_deaths).reshape(-1, 1)
total_recovered = np.array(total_recovered).reshape(-1, 1)

days_in_future = 10
future_forcast = np.array([i for i in range(len(dates)+days_in_future)]).reshape(-1, 1)
adjusted_dates = future_forcast[:-10]

start = '1/22/2020'
start_date = datetime.datetime.strptime(start, '%m/%d/%Y')
future_forcast_dates = []
for i in range(len(future_forcast)):
 future_forcast_dates.append((start_date + datetime.timedelta(days=i)).strftime('%m/%d/%Y'))
X_train_confirmed, X_test_confirmed, y_train_confirmed, y_test_confirmed = train_test_split(days_since_1_22, world_cases, test_size=0.36, shuffle=False)
