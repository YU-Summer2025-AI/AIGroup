# Stage 1: The "builder" stage to prepare the data
# This stage runs Python independently during the 'docker build' process.
FROM python:3.9-slim AS builder

# Set a working directory inside the builder stage
WORKDIR /app


# Copy your python script and the raw data into the builder
COPY clean_data.py .
COPY raw_data/ ./raw_data/

# Run the python script to modify the CSV files in place.
# This is the "independent" run of your script. It happens now, during the build.
RUN python clean_data.py

# Stage 2
FROM postgres:latest

# Copy your database initialization script
COPY 01_extract.sql /docker-entrypoint-initdb.d/
COPY 02_a_transform_matches.sql /docker-entrypoint-initdb.d/
COPY 02_b_transform_members.sql /docker-entrypoint-initdb.d/
COPY 03_load.sql /docker-entrypoint-initdb.d/

# Copy the MODIFIED CSV data from the 'builder' stage into the final image.
# The source path (/app/raw_data/) is from the builder stage defined above.
COPY --from=builder /app/raw_data/ /docker-entrypoint-initdb.d/raw_data/

