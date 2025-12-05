"""
Data Exploration - Flight Delay Prediction
Student: Pooja More
Project ID: AIML024
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def main():
    # Load data
    df = pd.read_csv('data/raw/full_data_flightdelay.csv')
    print(f"Dataset shape: {df.shape}")
    print("\nFirst 5 rows:")
    print(df.head())
    
    # Basic statistics
    print("\nBasic Statistics:")
    print(df.describe())
    
    # Check for missing values
    print("\nMissing Values:")
    print(df.isnull().sum())
    
    # Show column names
    print("\nColumn names:")
    print(df.columns.tolist())
    
    # Create multiple visualizations
    fig, axes = plt.subplots(2, 2, figsize=(15, 12))
    
    # 1. Delay distribution
    df['DEP_DEL15'].value_counts().plot(kind='bar', ax=axes[0,0], color=['green', 'red'])
    axes[0,0].set_title('Flight Delay Distribution')
    axes[0,0].set_xlabel('Delay Status (0=On Time, 1=Delayed)')
    axes[0,0].set_ylabel('Count')
    axes[0,0].tick_params(axis='x', rotation=0)
    
    # 2. Monthly flight distribution
    df['MONTH'].value_counts().sort_index().plot(kind='bar', ax=axes[0,1], color='skyblue')
    axes[0,1].set_title('Flights by Month')
    axes[0,1].set_xlabel('Month')
    axes[0,1].set_ylabel('Number of Flights')
    axes[0,1].tick_params(axis='x', rotation=45)
    
    # 3. Day of week distribution
    df['DAY_OF_WEEK'].value_counts().sort_index().plot(kind='bar', ax=axes[1,0], color='orange')
    axes[1,0].set_title('Flights by Day of Week')
    axes[1,0].set_xlabel('Day of Week (1=Mon, 7=Sun)')
    axes[1,0].set_ylabel('Number of Flights')
    axes[1,0].tick_params(axis='x', rotation=0)
    
    # 4. Distance group distribution
    df['DISTANCE_GROUP'].value_counts().sort_index().plot(kind='bar', ax=axes[1,1], color='purple')
    axes[1,1].set_title('Flights by Distance Group')
    axes[1,1].set_xlabel('Distance Group')
    axes[1,1].set_ylabel('Number of Flights')
    axes[1,1].tick_params(axis='x', rotation=45)
    
    plt.tight_layout()
    plt.savefig('outputs/data_exploration_charts.png', dpi=300, bbox_inches='tight')
    plt.show()
    
    # Additional histogram for plane age
    plt.figure(figsize=(10, 6))
    plt.hist(df['PLANE_AGE'], bins=30, color='lightcoral', alpha=0.7, edgecolor='black')
    plt.title('Distribution of Plane Age')
    plt.xlabel('Plane Age (years)')
    plt.ylabel('Frequency')
    plt.grid(True, alpha=0.3)
    plt.savefig('outputs/plane_age_distribution.png', dpi=300, bbox_inches='tight')
    plt.show()
    
    # Summary statistics visualization
    delay_rate = (df['DEP_DEL15'].sum() / len(df)) * 100
    print(f"\nOverall delay rate: {delay_rate:.2f}%")
    print("\nGraphs saved to outputs/ folder:")
    print("- data_exploration_charts.png")
    print("- plane_age_distribution.png")
    print("\nData exploration completed!")

if __name__ == "__main__":
    main()