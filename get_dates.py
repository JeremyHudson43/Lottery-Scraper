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
        try:
            tds = tr.find_all('td')
            if len(tds) == 4 and 'Double Play' not in tds[2].text:
                date = tds[0].text.strip()
                balls = [ball.text for ball in tds[1].find_all('span', class_='ball')]

                payout = tds[2].text.strip()
                date_object = datetime.strptime(date, '%Y %b %d')
                date = date_object.strftime('%Y-%m-%d')

                if 'Double' not in payout:
                    payout = payout.replace('$', '').replace(',', '')
                    payout = int(payout)

                    ball1, ball2, ball3, ball4, ball5 = balls

                    data.append({'date': date,
                                 'Ball One': ball1,
                                 'Ball Two': ball2,
                                 'Ball Three': ball3,
                                 'Ball Four': ball4,
                                 'Ball Five': ball5,
                                 'payout': payout})

                    print(data)

        except Exception as err:
            print(err)


df = pd.DataFrame(data)
df.to_csv('cash_5.csv', index=False)
