import os
import json
from tqdm import tqdm
import csv
import datetime as dp
from datetime import datetime, timedelta

folder = './Messenger_Group_1/' #Replace with your folder name

files = os.listdir(folder+'data') #'data' folder contains message JSON files

if '.DS_Store' in files:
    files.remove('.DS_Store')

with open(folder+'output.csv', 'a') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['Date','Week','Month','Year','Time','Sender'])

for filename in tqdm(files):
    if filename.startswith('message'):
        data = json.load(open(folder+'/data/'+filename, 'r'))
        for message in data['messages']:
            try:
                dt = dp.datetime.fromtimestamp(message['timestamp_ms'] / 1000)
                wd = dt-timedelta(days=dt.weekday())

                year = dt.strftime('%Y')
                month = dt.strftime('%B')
                week = wd.strftime('%Y-%m-%d')
                date = dt.strftime('%Y-%m-%d')
                time = dt.strftime('%H:%M:%S')
                
                sender = message['sender_name']
                first_name = sender.split(' ')[0]
                content = message['content']
                
                if year < '2021':
                    with open(folder+first_name+'.txt','a') as txt_file:
                        txt_file.write(content+' ')
                    
                    with open(folder+'output.csv', 'a') as csv_file:
                        writer = csv.writer(csv_file)
                        writer.writerow([date,week,month,year,time,first_name])

            except KeyError:
                pass
