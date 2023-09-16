import pandas as pd

def filter_data():
    filepath = '../data/SYB65_329_202209_Labour Force and Unemployment.csv'
        
    df = pd.read_csv(filepath, delimiter=',', encoding='utf-8')
        
    df = df.drop(columns='Region/Country/Area')
    df = df.rename(columns={'Unnamed: 1': 'Region/Country/Area'})
    
    # filter to countries 'United States of America' and 'Indonesia'
    df = df[df['Region/Country/Area'].isin(['United States of America', 'Indonesia'])]
    
    # find male and female labour participation rates
    labour_df = df[(df['Series'].isin(['Labour force participation - Male',
                                       'Labour force participation - Female',
                                       'Labour force participation - Total']))]
      
    labour_df = labour_df[['Region/Country/Area', 'Year', 'Series', 'Value']]
    
    labour_df = pd.pivot_table(labour_df,
                               values = 'Value',
                               index = ['Region/Country/Area', 'Year'],
                               columns = 'Series').reset_index()
    
    labour_df.to_csv('../data/labour.csv', encoding='utf-8', index=False)
    
    # find male and female

if __name__ == '__main__':
    filter_data()
