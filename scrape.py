from google_play_scraper import reviews, Sort
import pandas as pd

result, _ = reviews(
    'com.duolingo', 
    lang='en',    
    country='us',  
    sort=Sort.NEWEST,
    count=9000
)

# Convert to DataFrame
df = pd.DataFrame(result)[["content", "score"]]
df.columns = ["review", "rating"]

df.to_csv('duolingo_review.csv', index=False)

print("Scraping finished! Data saved as genshin_reviews_balanced.csv")
