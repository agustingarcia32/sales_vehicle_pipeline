# sales_vehicle_pipeline

## Overview
This Pipeline porcesses sales vehicle data using a CSV. These data were transformed using Pyspark, ensuring their integrity and quality for subsequent exploratory analysis using Power BI graphics. 

## Project Structure
```
sales_vehicle_pipelne/
|-- data/
|   |-- raw/
|   |   |-- car_prices.csv
|   |-- processed/
|       |-- sales_processed.csv
|-- src/
|   |-- extract.py
|   |-- transform.py
|-- powerbi/
|   |-- Higher_profit_per_brand.png
|   |-- Top_10_Cars_Sold.png
|   |-- Total_Cars_Sold_and_Money.png
|-- README.md
```

## Scripts Description
- **extract.py**: Extracts raw data from the csv.
- **transform.py**: Cleans and processes raw data.


## Output
The final processed data is saved in the `data/processed/` folder and analyzed in the `powerbi/` folder.
