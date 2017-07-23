from constants import *

# Class to bulk post to all groups in which you are a admin
class Bulk_Posting(object):

	def __init__(self, message):
		self.message = message

	def send_message(self):
		group_list = graph.get_object("me?fields=groups,id,name")
		for group in group_list['groups']['data']:
			graph.put_object(group['id'], "feed", message = self.message)
			
message = raw_input("Enter your message\n")
instance = Bulk_Posting(message)
instance.send_message()