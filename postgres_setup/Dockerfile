# Use the official PostgreSQL image as a base
FROM postgres:latest

# Switch to root user to install dependencies
USER root

# Update package lists and install python and pip
# rm -rf /var/lib/apt/lists/* cleans up cache to keep image size down
RUN apt-get update && \
    apt-get install -y python3 python3-pip && \
    rm -rf /var/lib/apt/lists/*

COPY rename_columns.py /docker-entrypoint-initdb.d/

COPY init.sql /docker-entrypoint-initdb.d/

COPY raw_data/ /docker-entrypoint-initdb.d/raw_data/

COPY 01-run-python.sh /docker-entrypoint-initdb.d/

RUN chown -R postgres:postgres /docker-entrypoint-initdb.d/

# Make the shell script executable
RUN chmod +x /docker-entrypoint-initdb.d/01-run-python.sh

USER postgres




