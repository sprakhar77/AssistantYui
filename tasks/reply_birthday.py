from constants import *

class Reply_Birthday(object):
	def __init__(self, message):
		self.message = message
		self.birthday = datetime.datetime.strptime('1996-11-15', '%Y-%m-%d')
	def check_date(post):
		post_date = datetime.datetime.strptime(post['created_time'],
					 '%Y-%m-%dT%H:%M:%S+0000')
		return post_date.date() == self.birthday.date()  

	def reply_to_post(self):
		feeds = graph.get_object('me?fields=feed')
		for post in feed:
			if check_date(post):
				graph.put_like(post['id'])
				graph.put_comment(post['id'], self.message)
		
instance = Reply_Birthday('Thank You! :D')
instance.reply_to_post()