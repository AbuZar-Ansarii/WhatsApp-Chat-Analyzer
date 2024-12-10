import pandas as pd
import re
import string

def process(data):
    pattern = r"\d{2}/\d{2}/\d{2}, \d{1,2}:\d{2}\u202f[ap]m"
    chat = re.split(pattern, data)[1:]
    dates = re.findall(pattern, data)
    date = []
    for i in dates:
        date.append(i.split(',')[0])
    name = []
    for i in chat:
        name.append(i.split(':')[0])
    df = pd.DataFrame({'Name': name, 'Date': date, 'Chat': chat})
    df['Date'] = pd.to_datetime(df['Date'])
    df["Month"] = df["Date"].dt.month
    df["Day"] = df["Date"].dt.day
    df["Year"] = df["Date"].dt.year
    df.drop(0, inplace=True)
    df.reset_index()

    return df
def clear_df(text):
        return text.translate(str.maketrans('', '', string.punctuation))


print(process("20/10/23, 11:06 am - Arham: UNIT 2 PME.pdf (file attached)"))