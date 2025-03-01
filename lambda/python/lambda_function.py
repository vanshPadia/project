import requests
import json
from datetime import datetime, timedelta
import os

def lambda_handler(event, context):
    # Get environment variables
    host = os.environ['OPENSEARCH_ENDPOINT']  # e.g. https://your-domain.region.es.amazonaws.com
    index_pattern = os.environ.get('INDEX_PATTERN', 'filebeat01-*')
    time_unit = os.environ.get('TIME_UNIT', 'minutes')  # Can be 'days', 'hours', or 'minutes'
    time_value = int(os.environ.get('TIME_VALUE', '2'))  # Default: 2 minutes

    # Calculate the cutoff timestamp
    now = datetime.utcnow()
    if time_unit == 'days':
        cutoff_time = now - timedelta(days=time_value)
    elif time_unit == 'hours':
        cutoff_time = now - timedelta(hours=time_value)
    elif time_unit == 'minutes':
        cutoff_time = now - timedelta(minutes=time_value)
    else:
        raise ValueError(f"Invalid time unit: {time_unit}. Must be 'days', 'hours', or 'minutes'")

    cutoff_timestamp = cutoff_time.strftime('%Y-%m-%dT%H:%M:%S.%fZ')  # Convert to ISO format

    # Construct the Delete by Query payload
    delete_query = {
        "query": {
            "range": {
                "@timestamp": {  # Adjust this field name if necessary
                    "lt": cutoff_timestamp  # Deletes logs older than the cutoff time
                }
            }
        }
    }

    # Perform delete operation
    url = f"{host}/{index_pattern}/_delete_by_query"
    headers = {"Content-Type": "application/json"}
    
    response = requests.post(url, headers=headers, data=json.dumps(delete_query))
    
    if response.status_code == 200:
        result = response.json()
        deleted_docs = result.get('deleted', 0)
        print(f"Deleted {deleted_docs} logs older than {time_value} {time_unit}.")
    else:
        print(f"Failed to delete logs: {response.text}")

    return {
        'statusCode': response.status_code,
        'body': json.dumps(response.json())
    }
