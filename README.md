# Apartment for Rent Classified Data Analysis and Prediction

## Overview

This project involves a comprehensive exploratory data analysis (EDA) and predictive modeling on a dataset containing classified advertisements for apartments for rent. The main objectives are to clean and preprocess the data, perform EDA to gain insights, and build predictive models to estimate apartment rental prices based on various features.

## Dataset

The dataset contains 10,000 records with the following features:

- `id`: Unique identifier of the apartment
- `category`: Category of classified (housing/rent/apartment, etc.)
- `title`: Title text of the apartment ad
- `body`: Body text of the apartment ad
- `amenities`: List of amenities (AC, basketball, cable, gym, internet access, pool, refrigerator, etc.)
- `bathrooms`: Number of bathrooms
- `bedrooms`: Number of bedrooms
- `currency`: Price currency
- `fee`: Fee associated with the apartment
- `has_photo`: Whether the ad has a photo
- `pets_allowed`: Pets allowed (dogs, cats, etc.)
- `price`: Rental price of the apartment
- `price_display`: Display price
- `price_type`: Price in USD
- `square_feet`: Size of the apartment in square feet
- `address`: Address of the apartment
- `cityname`: City where the apartment is located
- `state`: State where the apartment is located
- `latitude`: Latitude of the apartment
- `longitude`: Longitude of the apartment
- `source`: Origin of the classified ad
- `time`: When the classified ad was created (Unix timestamp)

## Data Cleaning and Preprocessing

1. **Missing Values Handling**:
   - Columns with significant missing values (`amenities`, `pets_allowed`, `address`) were examined.
   - Imputed missing values in `pets_allowed` and categorized as binary (0 for no pets, 1 for pets allowed).
   - Missing values in `cityname` and `state` were filled based on latitude and longitude using external address lookup.
   - Created a binary `amenity_class` feature based on the presence of advanced amenities.
   - Dropped unnecessary columns such as `title`, `body`, `currency`, `fee`, `price_display`, `address`, `id`.

2. **Feature Engineering**:
   - Converted categorical features (`bathrooms`, `bedrooms`, `source`, `has_photo`, `amenity_class`, `pets_allowed`) to categorical data types for efficient memory usage and modeling.
   - Extracted date-related features (`hour`, `day`, `month`, `dayofweek`) from the `time` column.
   - Dropped the `category` column as it contained mostly redundant information after initial cleaning.

3. **Data Transformation**:
   - One-hot encoded categorical features (`bathrooms`, `source`).
   - Standardized numerical features (`square_feet`, `hour`, `day`, `dayofweek`) using `StandardScaler`.

## Exploratory Data Analysis (EDA)

- **Descriptive Statistics**: Provided summary statistics for continuous features.
- **Box Plots**: Visualized distributions and identified outliers for numerical features.
- **Bar Plots**: Analyzed the distribution of categorical features like `bedrooms` and `bathrooms`.
- **Geospatial Analysis**: Used scatter plots and maps to explore the geographic distribution of rental prices.
- **Price Analysis**: Identified top cities and states with the highest average rental prices.

## Predictive Modeling

1. **Random Forest Regressor**:
   - Built a pipeline with preprocessing steps and a `RandomForestRegressor`.
   - Evaluated feature importances to identify the most influential features.
   - Achieved a mean squared error (MSE) indicating the model's performance on the test set.

2. **Linear Regression**:
   - Built a pipeline with preprocessing steps and a `LinearRegression` model.
   - Evaluated the coefficients to understand the linear relationship between features and rental prices.
   - Achieved a mean squared error (MSE) indicating the model's performance on the test set.

## Key Findings

- **Feature Importance**: `square_feet`, `hour`, and `bedrooms` were among the most important features in predicting rental prices.
- **Geospatial Insights**: States like California and cities like Barstow and Montenico had the highest rental prices.
- **Model Performance**: Both models provided insights, with Random Forest showing better performance in capturing complex relationships.

## Future Work

- **Model Enhancement**: Explore other machine learning models like Gradient Boosting and XGBoost for potentially better performance.
- **Feature Engineering**: Further refine features, especially those related to location and amenities.
- **Hyperparameter Tuning**: Perform hyperparameter tuning to optimize model performance.

## Conclusion

This project demonstrates the application of data cleaning, preprocessing, exploratory data analysis, and predictive modeling to gain insights and predict rental prices for apartments. The insights and models developed can assist renters and property managers in making informed decisions.

---

For detailed code and analysis, please refer to the provided Jupyter Notebook in 'Apartment For rent' folder, there is also located .csv data derived from https://archive.ics.uci.edu/dataset/555/apartment+for+rent+classified.
