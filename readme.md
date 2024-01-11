# Project Overview

This project was developed as a part of IBM Data Engineering Professional Certificate course. In this practice project,the student puts the skills acquired through the course to use and create a complete ETL pipeline for accessing data from a website and processing it to meet the requirements.

## Project Scenario

From IBM's project description:
"An international firm that is looking to expand its business in different countries across the world has recruited you. You have been hired as a junior Data Engineer and are tasked with creating an automated script that can extract the list of all countries in order of their GDPs in billion USDs (rounded to 2 decimal places), as logged by the International Monetary Fund (IMF). Since IMF releases this evaluation twice a year, this code will be used by the organization to extract the information as it is updated.

You have to complete the following tasks for this project:

1. Write a data extraction function to retrieve the relevant information from the required URL.

2. Transform the available GDP information into 'Billion USD' from 'Million USD'.

3. Load the transformed information to the required CSV file and as a database file.

4. Run the required query on the database.

5. Log the progress of the code with appropriate timestamps.
   "

## Project Structure

The repository is organized into the following files and folders:

- `/python/main.py`: Main python file, used for executing functions from imported modules
- `/python/etl_modules/`: Contain all modules for the whole ETL process
- `/files/`: Contains the .csv file, .sqlite file and .txt file (txt for logging)
- `/resources`: A folder containing subfolders with all the images used in the project.
- `/notebooks/etl_project_gdp.ipynb`: Jupyter Notebook for the project

## Technologies

This project uses the following technologies:

- Python
- Pandas
- SQLite3

## Getting Started

To get a local copy up and running, follow the following steps:

1. Clone the repo
   ```sh
   git clone https://github.com/fernandoSantello/ibm-data-engineering-project-1.git
   ```
2. Navigate to the project directory.
3. Run `main.py` to execute the ETL process or view `etl_project_gdp.ipynb` for a step by step guide

## License

Distributed under the MIT License. See `LICENSE` for more information.
