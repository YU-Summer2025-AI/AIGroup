#!/bin/sh

# This script will be executed by the postgres entrypoint before any .sql files
echo "------ Running Python pre-processing script ------"

# The script and data are all in /docker-entrypoint-initdb.d/
python3 /docker-entrypoint-initdb.d/rename_columns.py

echo "------ Python script finished ------"