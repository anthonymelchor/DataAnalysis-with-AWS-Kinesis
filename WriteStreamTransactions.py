import boto3
import json
import time
import pandas as pd
import uuid
import sys

df = pd.read_csv('transactions.csv')

df.columns

print(df.head())

#Trx fraudulent
df_filter =  df[df['class'] == 1]
print(df_filter.count)

name_stream = 'StreamTransactions'
kinesis = boto3.client('kinesis')

for index, row in df.iterrows():
    
    record = {
        'id_trx' : str(uuid.uuid4()),
        'v1' : row['v1'],
        'v2' : row['v2'],
        'v3' : row['v3'],
        'v4' : row['v4'],
        'v5' : row['v5'],
        'class' : int(row['class'])
    }
    
    kinesis.put_record(
		StreamName = name_stream,
		Data = json.dumps(record),
	    PartitionKey = str(uuid.uuid4())
	)
	
    print('Transacción enviada a Kinesis Data Streams : ' + str(record))