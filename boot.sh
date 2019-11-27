#!/bin/sh -e

# start service discovery task in the background
if [ "$SERVICE_URL" != "" ]; then
    python -c "from lockoncrm_common.container import register; register()" &
fi

# run web server
exec gunicorn -b 0.0.0.0:5003 --log-level=debug --access-logfile - --error-logfile - app:app --workers 3 --timeout 120
