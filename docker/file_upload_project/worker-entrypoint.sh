#!/bin/sh

until cd /app/file_upload_project
do
    echo "Waiting for server volume..."
done

# run a worker :)
celery -A file_upload_project worker --loglevel=info --concurrency 1 -E
