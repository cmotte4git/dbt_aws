import os
import boto3
import duckdb


# create a connection to a file called 'file.db'
con = duckdb.connect("dev.db")


# Path to your Parquet file
parquet_file = 's3://dev-data-redshift/dvf_full.parquet'

# Describe the Parquet file to get the schema
describe_result = con.execute(f"DESCRIBE SELECT * FROM '{parquet_file}'").fetchall()

# Map DuckDB types to Redshift types
type_mapping = {
    'BOOLEAN': 'BOOLEAN',
    'TINYINT': 'SMALLINT',
    'SMALLINT': 'SMALLINT',
    'INTEGER': 'INTEGER',
    'BIGINT': 'BIGINT',
    'FLOAT': 'FLOAT4',
    'DOUBLE': 'FLOAT8',
    'DECIMAL': 'DECIMAL',
    'VARCHAR': 'VARCHAR',
    'DATE': 'DATE',
    'TIMESTAMP': 'TIMESTAMP'
}

# Create the CREATE TABLE statement
table_name = 'dvf_full'
create_table_sql = f"CREATE TABLE {table_name} (\n"

for column in describe_result:
    column_name = column[0]
    duckdb_type = column[1]
    redshift_type = type_mapping.get(duckdb_type, 'VARCHAR')
    create_table_sql += f"    {column_name} {redshift_type},\n"

# Remove the trailing comma and close the statement
create_table_sql = create_table_sql.rstrip(',\n') + "\n);"

# Print the CREATE TABLE statement
print(create_table_sql)