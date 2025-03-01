import requests
import json
from datetime import datetime, timedelta
import os

def lambda_handler(event, context):
    # Get environment variables
    host = os.environ['OPENSEARCH_ENDPOINT']  # e.g., https://your-domain.region.es.amazonaws.com
    index_pattern = os.environ.get('INDEX_PATTERN', 'filebeat01-*')

    # Calculate cutoff date (start of today in UTC)
    now = datetime.utcnow()
    cutoff_date = now.strftime('%Y.%m.%d')  # Convert to YYYY.MM.DD format for index matching

    # List all indices
    url = f"{host}/_cat/indices/{index_pattern}?format=json"
    headers = {"Content-Type": "application/json"}

    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        print(f"Failed to fetch indices: {response.text}")
        return {'statusCode': response.status_code, 'body': json.dumps(response.text)}

    indices = response.json()

    # Identify indices older than today
    indices_to_delete = []
    for index in indices:
        index_name = index['index']
        
        # Extract date part from index name (assuming it ends with YYYY.MM.DD)
        parts = index_name.split('-')
        if len(parts) >= 2:
            index_date = parts[-1]
            try:
                index_datetime = datetime.strptime(index_date, '%Y.%m.%d')
                if index_datetime.strftime('%Y.%m.%d') < cutoff_date:
                    indices_to_delete.append(index_name)
            except ValueError:
                continue  # Skip indices without a valid date

    # Delete old indices
    for index_name in indices_to_delete:
        delete_url = f"{host}/{index_name}"
        delete_response = requests.delete(delete_url, headers=headers)

        if delete_response.status_code == 200:
            print(f"Deleted index: {index_name}")
        else:
            print(f"Failed to delete index {index_name}: {delete_response.text}")

    return {
        'statusCode': 200,
        'deleted_indices': indices_to_delete
    }
