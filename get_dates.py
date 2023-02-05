from bs4 import BeautifulSoup
import os
import pandas as pd
from datetime import datetime

base_path = r'C:\Users\jer43\OneDrive\Desktop\cash_5'
all_files = os.listdir(base_path)

data = []

for file_path in all_files:

    file_path = os.path.join(base_path, file_path)

    with open(file_path, 'r') as f:
        html = f.read()

    soup = BeautifulSoup(html, 'html.parser')
    for tr in soup.find_all('tr'):
        tds = tr.find_all('td')
        if len(tds) == 4 and 'Double Play' not in tds[2].text:
            date = tds[0].text.strip()
            balls = [ball.text for ball in tds[1].find_all('span', class_='ball')]

            payout = tds[2].text.strip().replace('$', '')
            payout = int(payout)

            date_object = datetime.strptime(date, '%Y %b %d')
            date = date_object.strftime('%Y-%m-%d')
            
            if 'Double' not in payout:
                data.append({'date': date, 'balls': balls, 'payout': payout})

df = pd.DataFrame(data)
print(df)
