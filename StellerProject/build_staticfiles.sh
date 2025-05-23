#!/bin/bash

# Debug information
echo "Current directory: $(pwd)"
ls -la

# Use the correct Python path in Vercel
export PATH="/opt/python/3.9.16/bin:$PATH"

# Install dependencies
python3 -m pip install -r requirements.txt

# Create staticfiles directory if it doesn't exist
mkdir -p staticfiles

# Run collectstatic with noinput flag and verbosity
cd /vercel/path0/StellerProject
python3 manage.py collectstatic --noinput --verbosity 2

# Set proper permissions for static files
chmod -R 755 staticfiles

# Show contents of staticfiles directory
echo "Contents of staticfiles directory:"
ls -la staticfiles/
ls -la staticfiles/imgs/

# Remove the curl test since we're in a build environment
echo "Static files collection completed" 