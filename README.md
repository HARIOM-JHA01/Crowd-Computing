# Crowd-Computing
# Data Estimation and Mean Calculation

This Python script allows you to enter a list of data points, trim the outliers, and calculate the mean of the remaining values. It utilizes the `statistics` module to calculate the mean.

## Prerequisites

To run this script, you need to have Python installed on your machine.

## How to Use

1. Clone the repository or download the `crowdComputing.py` file.

2. Open a terminal or command prompt and navigate to the directory where the `crowdComputing.py` file is located.

3. Run the script by executing the following command:
   python crowdComputing.py

4. Enter the data points one by one when prompted. To continue entering data, enter `1`. To end data entry, enter `0`.

5. The script will calculate the mean of the trimmed data points and display the result.

## Customization

You can modify the code to suit your needs. For example, you can change the trim percentage by modifying the `trim_value` variable.

```python
trim_value = int(0.1 * len(estimates))

Feel free to explore and customize the code based on your requirements.
