#!/bin/bash

DB_USER="your username"
DB_PASS="your password"
DB_NAME="sqlchapters"

# Exporting the schema
mysqldump -u "$DB_USER" -p"$DB_PASS" --no-data "$DB_NAME" > schema.sql

# Exporting the data
mysqldump -u "$DB_USER" -p"$DB_PASS" --no-create-info "$DB_NAME" > data.sql

echo "Database export completed"
