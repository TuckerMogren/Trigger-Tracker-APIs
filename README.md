# Trigger-Tracker-APIs
Custom APIs related to development of the iOS app, Trigger Tracker  

Created by Tucker Mogren in September 2021.  

Uses Pyton 3.9 - Slim, see reqpurements.txt for package details. 

DOCKER SETUP:

1. Make sure Docker and Docker Daemon is installed and running
2. Run the following command in terminal: docker build -t trigger_tracker_apis:0.1 .
3. When that ran successfully run, docker run -p 8000:8000 --name trigger-tracker-api trigger_tracker_apis:0.1
4. To stop the container run docker kill trigger-tracker-api