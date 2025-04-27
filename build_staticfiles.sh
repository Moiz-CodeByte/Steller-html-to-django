#!/bin/bash

# Debug information
echo "Current directory: $(pwd)"
ls -la

# Install dependencies
pip install -r requirements.txt

# Run collectstatic with noinput flag and verbosity
python manage.py collectstatic --noinput --verbosity 2

# Show contents of staticfiles directory
echo "Contents of staticfiles directory:"
ls -la staticfiles/
ls -la staticfiles/css/ 