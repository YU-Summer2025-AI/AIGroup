# Stage 1: The final postgres image
FROM postgres:latest

# Copy your database initialization script
COPY 01_extract.sql /docker-entrypoint-initdb.d/
COPY 02_a_transform_matches.sql /docker-entrypoint-initdb.d/
COPY 02_b_transform_members.sql /docker-entrypoint-initdb.d/
COPY 03_load.sql /docker-entrypoint-initdb.d/

# Copy the raw CSV data directly into the final image.
COPY raw_data/ /docker-entrypoint-initdb.d/raw_data/
