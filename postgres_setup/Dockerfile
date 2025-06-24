# Stage 1: The "builder" stage to prepare the data
# This stage runs Python independently during the 'docker build' process.
FROM python:3.9-slim as builder

# Set a working directory inside the builder stage
WORKDIR /app


# Copy your python script and the raw data into the builder
COPY rename_columns.py .
COPY raw_data/ ./raw_data/

# Run the python script to modify the CSV files in place.
# This is the "independent" run of your script. It happens now, during the build.
RUN python rename_columns.py

# --- The builder stage is now complete, and the processed data is in /app/raw_data/ ---


# Stage 2: The final postgres image
# This stage knows nothing about Python. It only receives the processed data.
FROM postgres:latest

# Copy your database initialization script
COPY init.sql /docker-entrypoint-initdb.d/

# Copy the MODIFIED CSV data from the 'builder' stage into the final image.
# The source path (/app/raw_data/) is from the builder stage defined above.
COPY --from=builder /app/raw_data/ /docker-entrypoint-initdb.d/raw_data/