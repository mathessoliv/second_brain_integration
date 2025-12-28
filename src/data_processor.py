from dotenv import load_dotenv
load_dotenv('.env')

from notion_manager import get_sprints, get_bi_backlog
from utils import logger
import pandas as pd


def format_data():

    data_sprints = get_sprints()
    data_bi_backlog = get_bi_backlog()

    try:
        clean_sprints_list = [
        {
            'Cicle Name': item['properties']['Cicle Name']['title'][0]['plain_text'],
            'Status': item['properties']['Status']['select']['name']
        }
        for item in data_sprints['results']
    ]

    except Exception as e:
        logger.error(f"Sprint data is null or malformed: {e}")

    try:
        clean_bi_backlog_list = [
            {
                'Task': item['properties']['Task']['title'][0]['plain_text'],
                'Status': item['properties']['Subject']['select']['name']
            }
            for item in data_bi_backlog['results']
        ]

    except Exception as e:
        logger.error(f"BI Backlog data is null or malformed: {e}")

    df_sprints = pd.DataFrame(clean_sprints_list)
    df_bi_backlog = pd.DataFrame(clean_bi_backlog_list)

    name_df_sprints = df_sprints['Cicle Name'].value_counts()
    count_df_bi_backlog = df_bi_backlog['Status'].value_counts().to_dict()
    
    tasks_in_backlog = {}

    for cicle_name in name_df_sprints.items():
        sprint_name = cicle_name[0]

    for index, row in df_bi_backlog.iterrows():
        tasks_in_backlog[row['Task']] = row['Status']

    return sprint_name, tasks_in_backlog

def generate_message():
    sprint_name, tasks_in_backlog = format_data()
    
    message =  f"""Olá, <b>Matheus</b>!👋 Seu status do Notion chegou!🚀\n
    📅<b>Sprint:</b> <code>{sprint_name}</code>\n
    📊<b>BI Backlog Tasks:</b>\n\n"""
    
    for task, status in tasks_in_backlog.items():
        emoji = "🔵" if "Doing" in status else "⚪"
        message += f"{emoji} <b>{task}</b>: <code>{status}</code>\n"
    
    message += "\n\n<i>Gerado automaticamente pelo seu script Python.</i>"

    return message