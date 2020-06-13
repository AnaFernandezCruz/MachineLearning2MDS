import xml.etree.ElementTree as ET
import csv
import pandas as pd


def procces_data(member, col):
    try:
        return member.find(col).text
    except:
        return ''


if __name__ == '__main__':
    tree = ET.parse("./dataset/Datosclima.xml")
    root = tree.getroot()

    Resident_data = open('./dataset/datosclima_parse.csv', 'w')

    csvwriter = csv.writer(Resident_data)
    resident_head = []

    count = 0

    for member in root.findall('Datosclima'):
        resident = []
        address_list = []
        if count == 0:
            count = count + 1
            resident_head.append('Id')
            resident_head.append('Indicativo')
            resident_head.append('Ano')
            resident_head.append('Mes')
            resident_head.append('Dia')
            resident_head.append('TMax')
            resident_head.append('TMin')
            resident_head.append('TMed')
            csvwriter.writerow(resident_head)

        #Id = member.find('Id').text
        Id = procces_data(member, 'Id')
        Indicativo = procces_data(member, 'Indicativo')
        Ano = procces_data(member, 'Ano')
        Mes = procces_data(member, 'Mes')
        Dia = procces_data(member, 'Dia')
        TMax = procces_data(member, 'TMax')
        TMin = procces_data(member, 'TMin')
        TMed = procces_data(member, 'TMed')

        resident.append(Id)
        resident.append(Indicativo)
        resident.append(Ano)
        resident.append(Mes)
        resident.append(Dia)
        resident.append(TMax)
        resident.append(TMin)
        resident.append(TMed)
        csvwriter.writerow(resident)

    Resident_data.close()

    df_temp = pd.read_csv('./dataset/datosclima_parse.csv', delimiter=",")

    for indicative in df_temp['Indicativo'].unique():
        df = df_temp.loc[df_temp['Indicativo'] == indicative]
        if not df.isnull().values.any():
            df.to_csv(r'./dataset/clean_' + indicative + '_datosclima.csv', index=False, header=True)
        else:
            df.to_csv(r'./dataset/' + indicative + '_datosclima.csv', index=False, header=True)
