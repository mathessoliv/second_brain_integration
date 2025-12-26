from dotenv import load_dotenv
load_dotenv('.env')

from notion_manager import get_data_of_database
import pandas as pd


data = get_data_of_database()

clean_list = [
    {
        'Cicle Name': item['properties']['Cicle Name']['title'][0]['plain_text'],
        'Status': item['properties']['Status']['select']['name']
    }
    for item in data['results']
]

df = pd.DataFrame(clean_list)

print(df['Status'].value_counts())



