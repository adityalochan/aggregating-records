# aggregating-records
Python program that retrieves real-world records from a public API, aggregates the data, and writes the results to JSON

## Data source
https://api.tvmaze.com/shows?page=0
Each record represents a TV show and contains information such as the show's name, language, genres, rating,

## Setup
python -m venv .venv
source .venv/bin/activate # Windows: .venv\Scripts\activate
pip install -r requirements.txt

## Run
python records.py

## Example output
{
  "shows_per_genre": {
    "Drama": 154,
    "Comedy": 66,
    "Crime": 57,
    "Action": 55,
    "Thriller": 41
  },
  "total_shows": 240,
  "average_rating_language": 7.584745762711866
}

Drama was the most popular genre with 154 shows
Comedy was the second most popular genre with 66 shows

## Data quirks
- A TV show can belong to multiple genres, so the program loops through the genres for each show
- Some shows have no genres
- Some shows have no average rating 


## Design choices
- A **dictionary** is used to count shows by genre because each genre can be used as a key with its count as the value.

## Known limitations
Results may change when the data returned by TVMaze changes