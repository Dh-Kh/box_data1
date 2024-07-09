# Country Data to Excel Exporter

This Python script fetches country information (name, capital, and flag) from the REST Countries API and exports it to an Excel file ("data.xlsx").

## Features

* Fetches country data from the [REST Countries API](https://restcountries.com).
* Exports the data neatly into an Excel file with columns for name, capital, and flag.

## Usage

1. **Clone or download the repository:**

   ```bash
    git clone https://github.com/Dh-Kh/box_data1.git

    python3 -m venv venv

    source venv/bin/activate (or . venv/bin/activate)

    pip install -r requirements.txt

    python3 main.py
   ```

## Project Structure
    ```bash
    .
    ├── __init__.py
    ├── main.py
    ├── Readme.md
    └── requirements.txt
    ```