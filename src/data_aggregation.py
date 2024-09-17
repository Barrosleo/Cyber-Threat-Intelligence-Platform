import requests
import json

def fetch_threat_data(api_url, headers):
    response = requests.get(api_url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def aggregate_data(sources):
    aggregated_data = []
    for source in sources:
        data = fetch_threat_data(source['api_url'], source['headers'])
        if data:
            aggregated_data.extend(data)
    return aggregated_data

if __name__ == "__main__":
    sources = [
        {
            "api_url": "https://api.threatintelligenceplatform.com/v1/threats",
            "headers": {"Authorization": "Bearer YOUR_API_KEY"}
        },
        {
            "api_url": "https://api.anotherthreatsource.com/v1/threats",
            "headers": {"Authorization": "Bearer YOUR_API_KEY"}
        }
    ]
    aggregated_data = aggregate_data(sources)
    with open("../data/aggregated_data.json", 'w') as outfile:
        json.dump(aggregated_data, outfile)
    print(f"Aggregated {len(aggregated_data)} threat intelligence entries.")
