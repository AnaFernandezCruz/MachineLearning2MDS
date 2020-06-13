import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm

sns.set(rc={'figure.figsize': (50, 10)})


def create_data_time(df):
    df['datetime'] = pd.to_datetime((df.ANIO * 10000 + df.MES * 100 + df.DIA).apply(str), format='%Y%m%d')
    return df


def filter_by_name_and_index_time(df, name):
    return df[df['NOMBRE'] == name].set_index('datetime')


def show_value_datetime(df, value):
    df[value].plot()
    plt.show()


def show_est(df, group, value):
    sns.boxplot(data=df, x=group, y=value)
    plt.show()


if __name__ == '__main__':
    df_temp = pd.read_csv('./dataset/Temperatura.csv')

    df_temp = create_data_time(df_temp)

    df = filter_by_name_and_index_time(df_temp, 'NAVACERRADA')

    df['mean_day'] = (df['T01'] + df['T02'] + df['T03'] + df['T04'] + df['T05'] + df['T06'] +
                      df['T07'] + df['T08'] + df['T09'] + df['T10'] + df['T11'] + df['T12'] +
                      df['T13'] + df['T14'] + df['T15'] + df['T16'] + df['T17'] + df['T18'] +
                      df['T19'] + df['T20'] + df['T21'] + df['T22'] + df['T23'] + df['T24']) / 24

    show_value_datetime(df, 'mean_day')
    show_est(df, 'MES', 'mean_day')
    show_est(df, 'ANIO', 'mean_day')

    df = df.dropna() ## OJO !

    wft_ciclo, wft_tend = sm.tsa.filters.hpfilter(df['mean_day'])
    df['tend'] = wft_tend

    df[['mean_day', 'tend']].plot(fontsize=12)
    legend = plt.legend()
    legend.prop.set_size(14)
    plt.show()

    descomposicion = sm.tsa.seasonal_decompose(df['mean_day'], model='additive', period=30)
    fig = descomposicion.plot()
    plt.show()


