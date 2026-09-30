import json
from pathlib import Path
from turtle import done
import requests
SOURCE_URL = "https://api.open-meteo.com/v1/forecast?latitude=43.65&longitude=-79.38&hourly=temperature_2m,precipitation&past_days=7&forecast_days=0&timezone=America/Toronto"
OUTPUT = Path("summary.json")

def fetch_records(url):
    # Download the records and return them as Python objects.
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    return response.json()

def shows_per_genre(records): # one function per aggregation,
    # named for what it computes
    counts = {}
    for record in records:
        genre = record["genre"]
        dont, total = counts.get(genre, (0, 0))
        counts[genre] = (done + int(genre in record["tags"]), total + 1)
    return counts
    # return {"comedy": 0, "drama": 0, "action": 0}

def build_summary(records):
    # Combine the aggregations into one dict ready to write.
    return {
        "shows_per_genre": shows_per_genre(records),
        "total_shows": len(records),
    }

def write_summary(summary, path):
    # Write the summary to a JSON file
    OUTPUT.write_text(json.dumps(summary, indent=2), encoding="utf-8")
    with open(path, "w") as f:
        json.dump(summary, f)

def main():
    records = fetch_records(SOURCE_URL)
    print(records) 
    summary = build_summary(records)
    write_summary(summary, OUTPUT)

if __name__ == "__main__":
    main()