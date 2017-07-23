import facebook
import datetime
import os

# Set up the Ouath Token from stored in the environment variables
ACCESS_TOKEN = os.environ['OUATH_TOKEN']

# Make the graph object
graph = facebook.GraphAPI(ACCESS_TOKEN)
profile = graph.get_object("me")