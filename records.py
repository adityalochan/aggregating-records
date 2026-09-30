import json
from pathlib import Path
import requests

SOURCE_URL = "https://api.tvmaze.com/shows?page=0"
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
        genres = record["genres"]

        for genre in genres:
            counts[genre] = counts.get(genre, 0) + 1
    return counts

def total_shows(records):
    return len(records)

def average_rating_language(records):
    sum , count = 0, 0
     
    for record in records:
        rating = record["rating"]["average"]

        if rating is not None:
            count += 1
            sum += rating
    return sum / (len(records) - count)   


def build_summary(records):
    # Combine the aggregations into one dict ready to write.
    summary = {}
    summary["shows_per_genre"] = shows_per_genre(records)
    summary["total_shows"] = total_shows(records)
    summary["average_rating_language"] = average_rating_language(records)
    return summary


def write_summary(summary, path):
    # Write the summary to a JSON file
    OUTPUT.write_text(json.dumps(summary, indent=2), encoding="utf-8")
    with open(path, "w") as f:
        json.dump(summary, f)

def main():
    records = fetch_records(SOURCE_URL)
    summary = build_summary(records)
    write_summary(summary, OUTPUT)

if __name__ == "__main__":
    main()