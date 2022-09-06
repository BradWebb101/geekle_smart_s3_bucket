from datetime import date
import boto3
import os
import urllib
import pandas as pd
from io import StringIO

def main(event, context):  
    # creates todays date for output file
    today = date.today().strftime("%d%m%Y")
    # calling boto3 client
    s3 = boto3.client('s3')

    # getting bucket and file details from JSON message from lambda trigger
    input_bucket = event['Records'][0]['s3']['bucket']['name']
    file_key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8')

    # getting output bucket (Set as env variable for lambda function in smarts3_bucket_stack)
    output_bucket = os.getenv('destination_bucket')
    output_key = f'{today}_output.csv'

    # importing data to DataFrame
    response = s3.get_object(Bucket=input_bucket, Key=file_key)
    new_file = pd.read_csv(response['Body'])

    # checking if there is an existing file with todays date
    try:
        response = s3.get_object(Bucket=output_bucket, Key=output_key)
        existing_file = pd.read_csv(response['Body'])
        # Can add more logic here
        output_df = pd.concat([existing_file, new_file])

    # if not it will just create one with the single dataframe from the file imported
    except Exception as e:
        output_df = new_file

    # unloading to s3 with new name + possible concat
    with StringIO() as csv_buffer:
        output_df.to_csv(csv_buffer, index=False)
        response = s3.put_object(
            Bucket=output_bucket, Key=output_key, Body=csv_buffer.getvalue()
        )

    # deleting original file 
    s3.delete_object(input_bucket, file_key)