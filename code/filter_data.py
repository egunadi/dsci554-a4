import pandas as pd

def filter_data():
    filepath = '../data/SYB65_329_202209_Labour Force and Unemployment.csv'
        
    df = pd.read_csv(filepath, delimiter=',', encoding='utf-8')
        
    df = df.drop(columns='Region/Country/Area')
    df = df.rename(columns={'Unnamed: 1': 'Region/Country/Area'})
    
    # filter to countries 'United States of America' and 'Indonesia'
    df = df[df['Region/Country/Area'].isin(['United States of America', 'Indonesia'])]
    
    labour22_df = df[(df['Series'].isin(['Labour force participation - Male',
                                         'Labour force participation - Female'])) 
                        & (df['Year'] == 2022)] 
      
    labour22_df = labour22_df[['Region/Country/Area', 'Series', 'Value']]
    
    labour22_df = pd.pivot_table(labour22_df,
                                 values = 'Value',
                                 index = ['Region/Country/Area'],
                                 columns = 'Series').reset_index()
    
    labour22_df.to_csv('../data/labour22.csv', encoding='utf-8', index=False)

if __name__ == '__main__':
    filter_data()
