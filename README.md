![image](https://github.com/abh2050/lyft_dynamic_pricing/assets/44420081/20a91a05-e2cb-4d0b-b874-3dfac7ac9562)

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat&logo=python&logoColor=white&link=https://www.python.org/)
![Pandas](https://img.shields.io/badge/Pandas-1.3.4-blue?style=flat&logo=pandas&logoColor=white&link=https://pandas.pydata.org/)
![NumPy](https://img.shields.io/badge/NumPy-1.21.2-blue?style=flat&logo=numpy&logoColor=white&link=https://numpy.org/)
![Matplotlib](https://img.shields.io/badge/Matplotlib-3.4.3-blue?style=flat&logo=matplotlib&logoColor=white&link=https://matplotlib.org/)
![scikit-learn](https://img.shields.io/badge/scikit_learn-0.24.2-blue?style=flat&logo=scikit-learn&logoColor=white&link=https://scikit-learn.org/stable/)
![Machine Learning](https://img.shields.io/badge/Machine_Learning-Project-green?style=flat&link=https://en.wikipedia.org/wiki/Machine_learning)
![Data Visualization](https://img.shields.io/badge/Data_Visualization-Analysis-yellow?style=flat&link=https://en.wikipedia.org/wiki/Data_visualization)

# Lyft Trip Cost Predictor

## Introduction
Welcome to the Lyft Trip Cost Predictor project! This tool uses a Linear Regression model to provide estimates for Lyft trip costs. It factors in trip distance, day of the week, pickup hour, and peak hour status. Dynamic pricing, also known as surge pricing, is a flexible pricing strategy employed by companies like Lyft to adjust the cost of rides in real-time based on demand and supply conditions. This approach is particularly prevalent in the ride-sharing industry, where the availability of drivers and the demand from riders can fluctuate significantly throughout the day.

The core idea behind dynamic pricing is to balance the market by incentivizing more drivers to come online during times of high demand, such as rush hours, bad weather, or special events, by increasing potential earnings. Conversely, during periods of low demand, prices may decrease to attract more riders. This system not only helps in managing the availability of rides but also ensures a steady supply of drivers by aligning their incentives with market needs.

Dynamic pricing algorithms take into account various factors, including the number of active riders and drivers, historical data, location, time of day, and special events, to calculate fare adjustments. This approach allows Lyft to provide reliable service even during peak demand times while also maximizing efficiency and profitability.

For users, dynamic pricing means that the cost of a ride can vary depending on when and where they are booking it. While it ensures higher availability of rides, it also requires users to be more aware of timing and circumstances to potentially avoid higher fares during surge pricing periods.

## Live Application
Experience the tool in action: [Lyft Dynamic Streamlit App](https://lyftdynamic.streamlit.app/)

## Table of Contents
- [Introduction](#introduction)
- [Live Application](#live-application)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Deployment](#deployment)
  - [Local Deployment](#local-deployment)
  - [Cloud Deployment (Streamlit Sharing)](#cloud-deployment-streamlit-sharing)
- [Model Training](#model-training)
- [Contributing](#contributing)
- [License](#license)

## Getting Started

### Prerequisites
Before using the Lyft Trip Cost Predictor, ensure you have the following installed:
- Python 3.6 or higher
- pip (Python package installer)
- Streamlit
- scikit-learn
- joblib
- numpy
- pandas

Install all required Python packages using:
```bash
pip install -r requirements.txt
```

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/lyft-trip-cost-predictor.git
   ```
2. Navigate to the project directory:
   ```bash
   cd lyft-trip-cost-predictor
   ```

## Usage
1. Train the Linear Regression model using the provided Jupyter Notebook or your data preparation and model training process.
2. Save the trained model as `linear_regression_model.joblib` in the project directory.
3. Launch the Streamlit app:
   ```bash
   streamlit run streamlit_app.py
   ```
4. Input the trip parameters and click "Predict Cost" to get an estimate.

## Deployment

### Local Deployment
1. Ensure all prerequisites are met.
2. Run the Streamlit app:
   ```bash
   streamlit run streamlit_app.py
   ```
3. Access the app at http://localhost:8501.

### Cloud Deployment (Streamlit Sharing)
Follow Streamlit Sharing's deployment instructions available in their documentation for cloud deployment.

## Model Training
The model training process involves preprocessing the dataset, training a Linear Regression model, and evaluating its performance. Key steps include:

- Loading the dataset.
- Converting dates to datetime format.
- Calculating trip duration.
- Creating features for day of the week and hour of the day.
- Identifying peak hours.
- Preparing the dataset for the model.
- Splitting data into training and testing sets.
- Training the Linear Regression model.
- Predicting on the test set and calculating RMSE.
- Analyzing model coefficients and intercept.

The model achieves an RMSE of 5.4999, indicating its predictive accuracy. Further details and code snippets are included in the project files.
#### The Linear Regression model has been trained to predict the cost of a Lyft trip based on trip distance, pickup day of the week, pickup hour, and whether it is peak hour. The model's performance is summarized by an RMSE of 5.4999.
Here are the model's parameters:
- The coefficients for each feature are:
- Trip Distance: 3.3400
- Pickup Day of the Week: 1.1566
- Pickup Hour: 0.0462
- Is Peak Hour: -0.5061
- The intercept of the model is 3.0928.
- These parameters indicate how much each unit increase in the respective feature will affect the trip cost, holding other features constant. The negative coefficient for the peak hour suggests that, all else being equal, trips during peak hours are associated with a slightly lower cost, which may seem counterintuitive and could be an area for further investigation.

## Contributing
Contributions are always welcome! If you have suggestions or encounter issues, feel free to open an issue or submit a pull request.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
