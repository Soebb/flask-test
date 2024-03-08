#!/bin/bash
cd /app
echo "----- Now trying to run gunicorn ------ " 
gunicorn -b 0.0.0.0:5000 --reload --access-logfile - --error-logfile - app:app 
