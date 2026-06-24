# Amazon Laptop Recommendation & Market Analysis Dashboard

## 📌 Project Overview

This project focuses on extracting and analyzing Amazon laptop data to understand product performance, customer preferences, pricing patterns, and sales trends.

The dataset was created by scraping Amazon laptop listings and extracting detailed product information from individual product pages. A Streamlit dashboard was then developed to provide interactive analysis, comparisons, and insights.

---

## 🎯 Objectives

* Extract laptop product information from Amazon listings.
* Perform exploratory data analysis on pricing, ratings, discounts, and sales.
* Identify factors influencing laptop purchases.
* Build an interactive dashboard for analysis and comparison.
* Provide insights for customers and market researchers.

---

## 📊 Dataset Information

* Extracted information from 100 laptop products.
* Collected product-level details using HTML extraction and web scraping techniques.
* Dataset includes:

  * Product Name
  * Brand
  * Series
  * Price
  * Discount Percentage
  * Average Rating
  * Rating Count
  * Quantity Sold Last Month
  * Processor Details
  * Product URL
  * Additional Laptop Specifications

---

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Streamlit
* Plotly
* Matplotlib
* Seaborn
* BeautifulSoup
* HTML Parsing

---

## 🚀 Dashboard Features

### 1️⃣ Data Overview & Analysis

Provides a high-level summary of the laptop market.

#### Key Performance Indicators (KPIs)

* Total Products
* Average Price
* Average Ratings
* Average Quantity Sold

#### Visualizations

* Correlation Heatmap
* Top 5 Sold Laptop Series Distribution
* Price vs Quantity Sold Trend
* Price Category Distribution Based on Quantity Sold
* Top 5 Best-Selling Products

---

### 2️⃣ Comparative Analysis

Users can select any two laptops and compare them side by side.

#### Comparison Metrics

* Product Price
* Average Rating
* Quantity Sold Last Month
* Discount Percentage
* Price Comparison Scatter Plot

This feature helps users make informed purchasing decisions by evaluating products across multiple dimensions.

---

### 3️⃣ Ratings Analysis

#### A. Processor-Based Analysis

* Average Ratings by Processor Type
* Average Quantity Sold by Processor Type

#### B. Processor Brand Insights

Relationship between:

* Ratings
* Rating Counts
* Quantity Sold

Visualizations include:

* Average Quantity Sold vs Rating Counts
* Average Ratings by Processor Brand

#### C. Laptop Series Insights

Relationship between:

* Ratings
* Rating Counts
* Quantity Sold

Visualizations include:

* Average Quantity Sold vs Rating Counts
* Average Ratings by Laptop Series

---

### 4️⃣ URL Analysis

This feature allows users to analyze any laptop product from the extracted dataset by providing its URL.

#### Output Includes

* Product KPIs
* Product Specifications
* Price Information
* Ratings Information
* Sales Information

This creates a quick product intelligence tool for individual laptop analysis.

---

### 5️⃣ Wrap-Up & Business Insights

#### Key Findings

* Numerical factors alone are not the primary drivers of laptop sales.
* Quantity sold shows very weak correlation with:

  * Price
  * Discount Percentage
  * Customer Ratings
* Product specifications and features appear to have a greater impact on purchasing decisions.
* Customers are increasingly willing to spend more for improved performance and features.
* A noticeable market shift is observed from lower-priced laptops toward premium-priced laptops.

---

## ⚠️ Limitations

* Dataset contains only 100 products.
* Sales information is available for a single month.
* Long-term trend analysis cannot be performed.
* Predictive forecasting is not reliable with the available data.
* Results should be interpreted as indicative market insights rather than definitive conclusions.

---
## 🌐 Live Dashboard

Explore the interactive Streamlit dashboard here:

🔗 [Amazon Laptop Recommendation Dashboard](https://amazon-laptop-analysis-dashboard-tuorxz2bwdrriv6twrwywn.streamlit.app/)

The dashboard contains five interactive modules:

1. Data Overview & Analysis
2. Comparative Analysis
3. Ratings Analysis
4. URL-Based Product Analysis
5. Business Insights & Wrap-Up

Users can explore KPIs, visualizations, laptop comparisons, processor-based analysis, and product-specific insights through an interactive interface.

----
## 💡 Future Improvements

* Larger product dataset
* Automated data refresh pipeline
* Machine Learning recommendation system
* Time-series sales tracking
* Sentiment analysis using customer reviews
* Personalized laptop recommendations

---

## 👩‍💻 Author

Harshita Sahu

Data Analytics | Data Science | Machine Learning

Built as an end-to-end data analytics project involving web scraping, data analysis, visualization, and dashboard development.
