import pandas as pd



def parse_data():
    for_sheet_names=pd.ExcelFile(r'file.xlsx')
    sheet_names=for_sheet_names.sheet_names

    total_districts=0
    data=pd.read_excel(r'file.xlsx',skiprows=[0,1,2,4])
    data = data.fillna(method='ffill', axis=0)

    complete_output=[]
    for sheet_name in sheet_names:
        output_dict={}
        output_dict['province']=sheet_name
        district_and_local_level_list=[]
        data=pd.read_excel(r'file.xlsx',sheet_name=sheet_name,skiprows=[0,1,2,4])
        data = data.fillna(method='ffill', axis=0)
        df=pd.DataFrame(data,columns=['District'])
        unique_districts=list(df.District.unique())
        df2 = pd.DataFrame(data, columns=['District', 'Local Level Name'])
        for district in unique_districts:
            district_dict={}
            district_dict['district']=district
            filtered_data=df2['Local Level Name'].where(df2['District'] == district)
            filtered_with_not_null_values=filtered_data.dropna()
            final_list=filtered_with_not_null_values.values.tolist()
            final_list.pop()
            district_dict['local_level']=final_list
            district_and_local_level_list.append(district_dict)

        output_dict['info']=district_and_local_level_list
        complete_output.append(output_dict)
        total_districts+=len(unique_districts)

    return complete_output

