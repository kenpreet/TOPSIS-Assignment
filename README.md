# TOPSIS Assignment

This repository contains the complete implementation of the **TOPSIS (Technique for Order Preference by Similarity to Ideal Solution)** method as part of an academic assignment.

The project includes:
- A Google Colab notebook demonstrating the TOPSIS algorithm
- A Python package published on PyPI
- A command-line interface (CLI)
- A Flask-based web service for TOPSIS

---

## 1. Methodology (TOPSIS)

TOPSIS is a multi-criteria decision-making technique used to rank alternatives based on their distance from an ideal best and an ideal worst solution.

The steps involved are:

1. Construct the decision matrix  
2. Normalize the decision matrix  
3. Apply weights to each criterion  
4. Determine the ideal best and ideal worst values  
5. Calculate the distance of each alternative from ideal solutions  
6. Compute the TOPSIS score  
7. Rank the alternatives based on the TOPSIS score  

A higher TOPSIS score indicates a better alternative.

---

## 2. Result Table

After applying the TOPSIS method, the output contains:
- Original criteria values
- **Topsis Score** for each alternative
- **Rank** of each alternative

The alternative with **Rank 1** is considered the best option.

The result table is generated in the Google Colab notebook and also through the web service.

---

## 3. Python Package (PyPI)

The TOPSIS algorithm is implemented as a Python package and published on **PyPI**.

### Installation

```bash
pip install topsis-kenpreet-102303365

#Command line usage
topsis <input_file.csv> "<weights>" "<impacts>" <output_file.csv>
#Example
topsis data.csv "1,1,1,1,1" "+,+,-,+,+" result.csv

Input Requirements

Input file must be a CSV file

First column contains alternative names

Remaining columns must be numeric

Number of weights must match number of criteria

Impacts must be either + or -

4. Web Service (Flask Application)

A web-based TOPSIS service is developed using Flask.

Features

Upload CSV file

Enter weights and impacts

Validate email ID

Execute TOPSIS on the server

Display the TOPSIS result table directly on the web page

Workflow

User uploads a CSV file

User provides weights and impacts

Server runs the TOPSIS algorithm

Result table is generated and displayed on the same web page

The web service eliminates the need for command-line usage and improves usability.

5. Tools & Technologies Used

Python

Google Colab

Pandas, NumPy

Flask

PyPI

GitHub

6. Conclusion

This project demonstrates a complete end-to-end implementation of the TOPSIS method, including:

Algorithm implementation

Packaging and distribution

Command-line interface

Web-based service
