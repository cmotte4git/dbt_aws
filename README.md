Welcome to a dbt with redshift project!

### This project computes dvf data

# DDL generation from S3 parquet file -- tableDDL.py 
tableDDL.py is a python script generating table DDL thanks to DuckDB parquet metadata scanner

# top_delta_valeur_fonciere
This dbt model delivers best real estate operations during the last 5 years
It consists of a window function (lag) to compute highest profit for each parcelle_id (unique identifier for a property)
