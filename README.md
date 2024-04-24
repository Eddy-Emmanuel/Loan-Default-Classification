# Loan-Default-Classification
Loan default classification is the process of categorizing loans based on the likelihood of the borrower failing to repay them according to the agreed terms. It’s a crucial aspect of risk management in lending institutions. By accurately classifying loans into categories such as “low risk,” “medium risk,” or “high risk,” in our case “risk” or “No risk” Lenders can make informed decisions about loan approvals, interest rates, and the allocation of resources.

This classification is useful for several reasons:

1. Risk Management: It helps lenders assess the level of risk associated with each loan. Loans classified as high risk may require stricter terms or collateral, while low-risk loans may receive more favorable terms.

2. Profitability: By identifying and managing high-risk loans effectively, lenders can minimize losses due to defaults and improve overall profitability.

3. Regulatory Compliance: Many financial regulations require institutions to maintain certain levels of capital reserves based on the riskiness of their loan portfolios. Accurate classification ensures compliance with these regulations.

4. Customer Segmentation: It allows lenders to tailor their products and services to different customer segments based on risk profiles, thereby optimizing their offerings and attracting the right customers.

5. Portfolio Monitoring: Classification enables ongoing monitoring of loan portfolios, helping lenders identify early warning signs of potential defaults and take proactive measures to mitigate risks.


## Project Overview:

This project is a loan default classification system built using FastAPI and SQLAlchemy. It aims to predict whether a loan applicant is likely to default on their loan based on various features.

## Overview

The project consists of the following components:

- **main.py**: The main FastAPI application file containing API routes and logic.
- **config**: Directory containing configuration files.
- **database**: Directory containing database-related files.
- **model**: Directory containing machine learning model-related files.
- **routes**: Directory containing FastAPI route files.
- **service**: Directory containing service files.
- **Loan_default_Classification.ipynb**: Jupyter Notebook used for model development.
- **README.md**: This file, providing an overview of the project.
- **database.db**: SQLite database file.
- **output_1.png**, **output_2.png**, **output_3.png**, **output_4.png**: Output images or graphs generated during the project.
- **requirements.txt**: Text file listing the project dependencies.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/Eddy-Emmanuel/Loan-Default-Classification.git
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Ensure you have Python installed on your system.
2. Navigate to the project directory.
3. Run the FastAPI application:

    ```bash
    uvicorn main:app --reload
    ```

4. Once the server is running, you can access the API documentation and test the endpoints by visiting [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) in your browser.

## Contributing

Contributions are welcome! If you would like to contribute to this project, please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the [MIT License](LICENSE).

---

Feel free to customize it further based on your specific project details and requirements!
