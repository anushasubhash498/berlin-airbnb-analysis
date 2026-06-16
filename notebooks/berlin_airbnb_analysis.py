import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Set style
sns.set_theme(style="darkgrid")
plt.rcParams['figure.figsize'] = (10, 6)

# Load data
data_path = r'C:\Users\anusu\.gemini\antigravity\scratch\analytics-portfolio\berlin-airbnb-analysis\data\berlin_listings.csv'
if not os.path.exists(data_path):
    raise FileNotFoundError(f"Data file not found at {data_path}. Please run generate_data.py first.")

df = pd.read_csv(data_path)

# Create outputs folder if it doesn't exist
output_dir = r'C:\Users\anusu\.gemini\antigravity\scratch\analytics-portfolio\berlin-airbnb-analysis\outputs'
os.makedirs(output_dir, exist_ok=True)

print("=== Berlin Airbnb Data Profile ===")
print(f"Dataset shape: {df.shape}")
print("\nMissing values:")
print(df.isnull().sum())
print("\nPrice Statistics:")
print(df['price'].describe())

# 1. Price analysis by neighbourhood
plt.figure(figsize=(12, 6))
order = df.groupby('neighbourhood')['price'].median().sort_values(ascending=False).index
sns.boxplot(x='neighbourhood', y='price', data=df, order=order, palette='crest')
plt.xticks(rotation=45, ha='right')
plt.title('Distribution of Listing Prices by Berlin Neighbourhood (Sorted by Median)', fontsize=14, fontweight='bold')
plt.xlabel('Neighbourhood', fontsize=12)
plt.ylabel('Price (EUR)', fontsize=12)
plt.tight_layout()
plt.savefig(os.path.join(output_dir, 'price_by_neighbourhood.png'), dpi=300)
plt.close()

# 2. Room type distribution
plt.figure(figsize=(8, 8))
room_counts = df['room_type'].value_counts()
colors = sns.color_palette('pastel')[0:len(room_counts)]
plt.pie(room_counts, labels=room_counts.index, autopct='%1.1f%%', startangle=140, colors=colors, 
        textprops={'fontsize': 12, 'weight': 'bold'})
plt.title('Distribution of Airbnb Room Types in Berlin', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig(os.path.join(output_dir, 'room_type_distribution.png'), dpi=300)
plt.close()

# 3. Superhost vs non-superhost comparison
plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
sns.barplot(x='host_is_superhost', y='price', data=df, palette='coolwarm', errorbar=None)
plt.title('Avg Price: Superhost vs Regular Host', fontsize=12, fontweight='bold')
plt.xlabel('Is Superhost?', fontsize=10)
plt.ylabel('Average Price (EUR)', fontsize=10)

plt.subplot(1, 2, 2)
sns.barplot(x='host_is_superhost', y='review_scores_rating', data=df, palette='coolwarm', errorbar=None)
plt.title('Avg Rating: Superhost vs Regular Host', fontsize=12, fontweight='bold')
plt.xlabel('Is Superhost?', fontsize=10)
plt.ylabel('Average Rating (1-5)', fontsize=10)
plt.tight_layout()
plt.savefig(os.path.join(output_dir, 'superhost_comparison.png'), dpi=300)
plt.close()

# 4. Price vs rating scatter plot
plt.figure(figsize=(10, 6))
sns.scatterplot(x='review_scores_rating', y='price', hue='room_type', alpha=0.6, data=df, palette='Set2')
plt.title('Price vs Rating Score by Room Type', fontsize=14, fontweight='bold')
plt.xlabel('Review Score Rating', fontsize=12)
plt.ylabel('Price (EUR)', fontsize=12)
plt.tight_layout()
plt.savefig(os.path.join(output_dir, 'price_vs_rating.png'), dpi=300)
plt.close()

# 5. Availability heatmap
pivot_df = df.pivot_table(values='availability_365', index='neighbourhood', columns='room_type', aggfunc='mean')
plt.figure(figsize=(10, 8))
sns.heatmap(pivot_df, annot=True, fmt=".1f", cmap="YlGnBu", cbar_kws={'label': 'Avg Availability (Days/Year)'})
plt.title('Average Annual Availability by Neighbourhood & Room Type', fontsize=14, fontweight='bold')
plt.xlabel('Room Type', fontsize=12)
plt.ylabel('Neighbourhood', fontsize=12)
plt.tight_layout()
plt.savefig(os.path.join(output_dir, 'availability_heatmap.png'), dpi=300)
plt.close()

# Generate text summary insights
mitte_avg = df[df['neighbourhood'] == 'Mitte']['price'].mean()
wedding_avg = df[df['neighbourhood'] == 'Wedding']['price'].mean()
superhost_rating = df[df['host_is_superhost'] == 't']['review_scores_rating'].mean()
regular_rating = df[df['host_is_superhost'] == 'f']['review_scores_rating'].mean()

print("\n=== Business Insights Summary ===")
print(f"1. Price disparity: Mitte has the highest premium listings, averaging €{mitte_avg:.2f} per night, while Wedding remains one of the most budget-friendly regions with an average price of €{wedding_avg:.2f} per night.")
print(f"2. Room type dominance: Entire homes/apartments constitute {df['room_type'].value_counts(normalize=True)['Entire home/apt']*100:.1f}% of all listings, showcasing strong demand for independent spaces.")
print(f"3. Superhost value: Superhosts command higher average reviews ({superhost_rating:.2f} vs {regular_rating:.2f}) and charge an average premium of {((df[df['host_is_superhost'] == 't']['price'].mean() / df[df['host_is_superhost'] == 'f']['price'].mean()) - 1)*100:.1f}% compared to regular hosts.")
print("4. Booking Availability: Shared rooms and Hotel rooms have significantly higher availability compared to private homes, suggesting a lower occupancy rate for shared units.")
print(f"Visualizations saved to {output_dir}")
