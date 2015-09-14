#!/bin/sh

echo "Loading calendar..."
cat fullcalendar/demos/DEVPLOY_EVENTS
load_calendar.py --generate
git add -p
git commit
git push
