import json

def generate_insights(threat_counts):
    insights = []
    for threat, count in threat_counts.items():
        if count > 10:
            insights.append(f"High frequency of {threat} detected: {count} occurrences.")
    return insights

if __name__ == "__main__":
    with open("../data/threat_counts.json", 'r') as infile:
        threat_counts = json.load(infile)
    insights = generate_insights(threat_counts)
    with open("../data/insights.json", 'w') as outfile:
        json.dump(insights, outfile)
    print("Generated Insights:")
    for insight in insights:
        print(insight)
