# Duolingo Rating Sentiment Analysis Using Machine Learning

## Overview
This project aims to perform sentiment analysis based on application review data obtained through web scraping. A machine learning model is used to classify sentiment into **positive, negative, and neutral**.

## Getting Started

### 1. Install Dependencies
Run the following command to install all required dependencies using conda:
```bash
# Create a new Conda environment
conda create --name duolingo_sentiment_analysis python=3.9 -y

# Activate the environment
conda activate duolingo_sentiment_analysis

# Install dependencies from the requirements file
pip install -r requirements.txt
```
### 2. Data Scraping

Perform data scraping using scraping.py:
```
python scrape.py
```
The scraped data will be saved in the file dulingo-review.csv.
### 3. Train Model

Open and run the notebook `analisis-sentimen.ipynb` to process the dataset, perform feature extraction, train the model, and evaluate its performance.