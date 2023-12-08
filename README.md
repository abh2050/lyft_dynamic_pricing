![image](https://github.com/abh2050/lyft_dynamic_pricing/assets/44420081/20a91a05-e2cb-4d0b-b874-3dfac7ac9562)
# Lyft Trip Cost Predictor

This project is a Lyft trip cost predictor powered by a Linear Regression model. It allows users to estimate the cost of a Lyft trip based on various input parameters, including trip distance, pickup day of the week, pickup hour, and whether it is during peak hours.

## app
https://lyftdynamic.streamlit.app/

## Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Deployment](#deployment)
  - [Local Deployment](#local-deployment)
  - [Cloud Deployment (Heroku)](#cloud-deployment-heroku)
- [Contributing](#contributing)
- [License](#license)

## Getting Started

### Prerequisites

Before running the Lyft Trip Cost Predictor, you need to have the following software and dependencies installed:

- Python (3.6+)
- pip
- Streamlit
- scikit-learn
- joblib
- numpy
- pandas

You can install the required Python packages by running:

```bash
pip install -r requirements.txt
```bash
https://lyftdynamic.streamlit.app/

Installation
Clone the repository to your local machine:
bash
Copy code
git clone https://github.com/yourusername/lyft-trip-cost-predictor.git
Change into the project directory:
bash
Copy code
cd lyft-trip-cost-predictor
Usage
Train the Linear Regression model by running the provided Jupyter Notebook or your own data preparation and model training process.

Save the trained model as linear_regression_model.joblib in the project directory.

Run the Streamlit app to use the Lyft Trip Cost Predictor:

bash
Copy code
streamlit run streamlit_app.py
Input the trip parameters, including trip distance, pickup day of the week, pickup hour, and whether it is during peak hours.

Click the "Predict Cost" button to get the estimated trip cost.

Deployment
Local Deployment
To run the Streamlit app locally, follow these steps:

Ensure you have installed the required dependencies (see Prerequisites).

Run the Streamlit app from the project directory:

https://lyftdynamic.streamlit.app/

bash
Copy code
streamlit run streamlit_app.py
Access the app in your web browser at http://localhost:8501.
Cloud Deployment (Streamlit Sharing)
To deploy the Streamlit app on the Streamlit Sharing platform, you can follow Streamlit Sharing's specific deployment instructions. Please refer to the Streamlit Sharing documentation for details.

Contributing
Contributions are welcome! If you have ideas for improvements or find any issues, please open an issue or submit a pull request.

License
This project is licensed under the MIT License - see the LICENSE file for details.




