from flask import Flask, render_template
import pandas as pd
import datetime

app = Flask(__name__)


@app.route('/')
def index():
    # Hopkins data
    death_df = pd.read_csv(
        'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv')
    confirmed_df = pd.read_csv(
        'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv')
    recovered_df = pd.read_csv(
        'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv')
    country_df = pd.read_csv(
        'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/web-data/data/cases_country.csv')
    country_df.columns = map(str.lower, country_df.columns)
    confirmed_df.columns = map(str.lower, confirmed_df.columns)
    death_df.columns = map(str.lower, death_df.columns)
    recovered_df.columns = map(str.lower, recovered_df.columns)

    confirmed_total = int(country_df['confirmed'].sum())
    deaths_total = int(country_df['deaths'].sum())
    recovered_total = int(country_df['recovered'].sum())
    active_total = int(country_df['active'].sum())

    last_update = datetime.datetime.strptime(
        country_df['last_update'].values[0], '%Y-%m-%d %H:%M:%S').strftime('%e de %B de %Y a las %H:%M')
    pais = ['Spain']
    spain_df = country_df.loc[country_df['country_region'].isin(pais)]

    deaths_spain = int(spain_df['deaths'].sum())
    confirmed_spain = int(spain_df['confirmed'].sum())
    recovered_spain = int(spain_df['recovered'].sum())
    active_spain = int(spain_df['active'].sum())

    return render_template('index.html',
                           confirmed_total=formatnum(confirmed_total),
                           deaths_total=formatnum(deaths_total),
                           recovered_total=formatnum(recovered_total),
                           active_total=formatnum(active_total),
                           confirmed_spain=formatnum(confirmed_spain),
                           deaths_spain=formatnum(deaths_spain),
                           recovered_spain=formatnum(recovered_spain),
                           active_spain=formatnum(active_spain),
                           last_update=last_update,
                           country_df=country_df,                      
                           )


# Formato numeros
def formatnum(num):
    return '{0:,}'.format(num)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
