import json
import pandas as pd

def analyze_data(data):
    df = pd.DataFrame(data)
    # Example analysis: count occurrences of each threat type
    threat_counts = df['threat_type'].value_counts()
    return threat_counts

if __name__ == "__main__":
    with open("../data/aggregated_data.json", 'r') as infile:
        data = json.load(infile)
    threat_counts = analyze_data(data)
    print("Threat Counts:")
    print(threat_counts)
