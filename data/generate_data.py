import pandas as pd
import numpy as np
import os

# Set seed for reproducibility
np.random.seed(42)

# Number of rows
n_rows = 1000

# Lists for random choices
neighbourhoods = [
    'Mitte', 'Prenzlauer Berg', 'Kreuzberg', 'Friedrichshain', 
    'Charlottenburg', 'Neukölln', 'Schöneberg', 'Pankow', 
    'Tempelhof', 'Wedding', 'Lichtenberg', 'Steglitz'
]

# Coordinate centers for neighbourhoods to make lat/long realistic
coord_centers = {
    'Mitte': (52.5200, 13.4050),
    'Prenzlauer Berg': (52.5407, 13.4217),
    'Kreuzberg': (52.4986, 13.3918),
    'Friedrichshain': (52.5150, 13.4540),
    'Charlottenburg': (52.5158, 13.2936),
    'Neukölln': (52.4810, 13.4350),
    'Schöneberg': (52.4821, 13.3503),
    'Pankow': (52.5689, 13.4022),
    'Tempelhof': (52.4638, 13.3859),
    'Wedding': (52.5501, 13.3600),
    'Lichtenberg': (52.5323, 13.5065),
    'Steglitz': (52.4578, 13.3216)
}

room_types = ['Entire home/apt', 'Private room', 'Shared room', 'Hotel room']
room_probs = [0.60, 0.36, 0.03, 0.01]

# Base prices for neighbourhoods
base_prices = {
    'Mitte': 110,
    'Prenzlauer Berg': 95,
    'Kreuzberg': 90,
    'Friedrichshain': 85,
    'Charlottenburg': 100,
    'Neukölln': 65,
    'Schöneberg': 80,
    'Pankow': 75,
    'Tempelhof': 70,
    'Wedding': 55,
    'Lichtenberg': 60,
    'Steglitz': 65
}

# Generate columns
data = []
for i in range(1, n_rows + 1):
    listing_id = 10000000 + i
    host_id = 20000000 + np.random.randint(1, 500)
    host_name = f"Host_{host_id % 1000}"
    
    # Superhost flag: 18% chance
    is_superhost = np.random.rand() < 0.18
    host_is_superhost = 't' if is_superhost else 'f'
    
    # Choose neighbourhood
    neigh = np.random.choice(neighbourhoods)
    
    # Generate coordinates with slight deviation
    lat_center, lon_center = coord_centers[neigh]
    latitude = lat_center + np.random.normal(0, 0.01)
    longitude = lon_center + np.random.normal(0, 0.015)
    
    # Room type
    room_type = np.random.choice(room_types, p=room_probs)
    
    # Calculate base price with multiplier for entire home/apt vs shared
    price_mult = 1.0
    if room_type == 'Entire home/apt':
        price_mult = 1.4
    elif room_type == 'Private room':
        price_mult = 0.7
    elif room_type == 'Shared room':
        price_mult = 0.4
    elif room_type == 'Hotel room':
        price_mult = 1.8
        
    # Superhost markup
    superhost_mult = 1.1 if is_superhost else 1.0
    
    # Random deviation in price
    price = int(base_prices[neigh] * price_mult * superhost_mult * np.random.uniform(0.7, 1.4))
    
    minimum_nights = np.random.choice([1, 2, 3, 5, 7, 30], p=[0.4, 0.3, 0.15, 0.08, 0.05, 0.02])
    number_of_reviews = int(np.random.exponential(scale=35))
    
    # Ratings: superhosts have higher average ratings
    if number_of_reviews > 0:
        if is_superhost:
            rating = round(np.random.uniform(4.6, 5.0), 2)
        else:
            rating = round(np.random.uniform(3.8, 4.9), 2)
    else:
        rating = np.nan
        
    availability_365 = np.random.randint(0, 365)
    calc_listings = np.random.choice([1, 2, 3, 4, 10], p=[0.75, 0.12, 0.06, 0.04, 0.03])
    instant_bookable = 't' if np.random.rand() < 0.45 else 'f'
    
    name = f"Charming {room_type} in {neigh}"
    
    data.append([
        listing_id, name, host_id, host_name, host_is_superhost, neigh, 
        room_type, price, minimum_nights, number_of_reviews, rating, 
        availability_365, latitude, longitude, calc_listings, instant_bookable
    ])

columns = [
    'id', 'name', 'host_id', 'host_name', 'host_is_superhost', 'neighbourhood', 
    'room_type', 'price', 'minimum_nights', 'number_of_reviews', 'review_scores_rating', 
    'availability_365', 'latitude', 'longitude', 'calculated_host_listings_count', 'instant_bookable'
]

df = pd.DataFrame(data, columns=columns)

# Create directory if it doesn't exist
os.makedirs(r'C:\Users\anusu\.gemini\antigravity\scratch\analytics-portfolio\berlin-airbnb-analysis\data', exist_ok=True)
output_path = r'C:\Users\anusu\.gemini\antigravity\scratch\analytics-portfolio\berlin-airbnb-analysis\data\berlin_listings.csv'
df.to_csv(output_path, index=False)
print(f"Generated {n_rows} synthetic listings at {output_path}")
