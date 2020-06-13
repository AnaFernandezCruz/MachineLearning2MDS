import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm

sns.set(rc={'figure.figsize': (50, 10)})


def show_value_datetime(df, value):
    df[value].plot()
    plt.show()


def create_data_time(df):
    df['datetime'] = pd.to_datetime((df.Ano * 10000 + df.Mes * 100 + df.Dia).apply(str), format='%Y%m%d')
    return df


def show_est(df, group, value):
    sns.boxplot(data=df, x=group, y=value)
    plt.show()


if __name__ == '__main__':
    df_temp = pd.read_csv('./dataset/clean_4452_datosclima.csv')

    df_temp = create_data_time(df_temp)

    show_value_datetime(df_temp, 'TMed')
    show_est(df_temp, 'Mes', 'TMed')

    wft_ciclo, wft_tend = sm.tsa.filters.hpfilter(df_temp['TMed'])
    df_temp['tend'] = wft_tend

    df_temp[['TMed', 'tend']].plot(fontsize=12)
    legend = plt.legend()
    legend.prop.set_size(14)
    plt.show()

    descomposicion = sm.tsa.seasonal_decompose(df_temp['TMed'], model='additive', period=30)
    fig = descomposicion.plot()
    plt.show()

