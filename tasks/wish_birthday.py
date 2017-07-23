from constants import *

class Birthday_Wisher(object):

	def __init__(self):
		self.today = datetime.datetime.now().strftime("%m-%d").split('-')

	# Validate if the current date is present in the birthday key of friend object
	def validate(self, friend):
		if friend.has_key('birthday'):
			date_array = friend['birthday'].split('/')
			if date_array[0] ==  self.today[0] and date_array[1] == self.today[1]:
				return True
		return False

	# Wish birthday to all friends
	def wish_birthday(self):
		friend_list = graph.get_object("me/friends?fields=birthday,name")
		for friend in friend_list['data']:
			if self.validate(friend):
				graph.put_object(friend['id'], "feed", message = "Happy Birthday! Have fun :D")
				print "Wished your friend: " + friend['name']

instance = Birthday_Wisher()
instance.wish_birthday()