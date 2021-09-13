# Trigger-Tracker-APIs
Custom APIs related to development of the iOS app, Trigger Tracker  

Created by Tucker Mogren in September 2021.  

Uses Pyton 3.9 - Slim, see requirements.txt for package details. 

DOCKER SETUP:
Referenced: https://www.youtube.com/watch?v=2a5414BsYqw
1. Make sure Docker and Docker Daemon is installed and running
2. Navigate to the following directory: Photos/
3. Run the following command in terminal: docker build -t trigger_tracker_photos_apis:0.1 .
4. Navigate to the following directory: Users/
5. Run the following command in terminal: docker build -t trigger_tracker_users_apis:0.1 .
3. When that ran successfully run, docker run -p 8000:8000 --name trigger-tracker-api trigger_tracker_apis:0.1
4. To stop the container run docker kill trigger-tracker-api