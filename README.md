Welcome to a dbt with redshift project!

# This project computes dvf data

### Redshift as dbt DBT adapter
A redshift cluster is needed to 

### top_delta_valeur_fonciere
This dbt model delivers best real estate operations during the last 5 years
It consists of a window function (lag) to compute highest profit for each parcelle_id (unique identifier for a property)
