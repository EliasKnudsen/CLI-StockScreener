# Stock Screener CLI

Stock Screener CLI is a small program to scan the market for diffrent stocks.

This program scrapes the data from finviz. This makes the program highly unstable if changes are made.

## Installation

Use git [git](https://github.com/) to install Stock Screener CLI.

```bash
git clone https://github.com/EliasKnudsen/CLI-StockScreener
```
In order to use the program, you will need to install the dependencies
```
pip install -r /path/to/requirements.txt
```

## Usage

```terminal
python3 get_data.py
```

You can save filters, load filters and run a single scan.

All scans will be exported as csv to the ```/Exports``` folder.

Loaded scans will also be saved as a date when it was performed. You can use the diffrent dates to compare diffrences in the market.
