import os
import hashlib
import urllib2
class DownloadSubs(object):
	def __init__(self, file_name):
		self.file_name = file_name
		self.root = os.getcwd() + '/'
		self.name, self.extension = os.path.splitext(self.root + self.file_name)

	# this hash function receives the name of the file and returns the hash code
	def get_hash(self):
	    readsize = 64 * 1024
	    with open(self.file_name,'rb') as f:
	        size = os.path.getsize(self.file_name)
	        data = f.read(readsize)
	        f.seek(-readsize, os.SEEK_END)
	        data += f.read(readsize)
	    return hashlib.md5(data).hexdigest()

	def download(self):
		header = {'User-Agent' : 'SubDB/1.0 (justcode21/0.1; https://github.com/justcode21/Assistant-Yui)'}
		url = 'http://api.thesubdb.com/?action=download&hash=' + self.get_hash() + '&language=en'
		request = urllib2.Request(url, "", header)
		response = urllib2.urlopen(request).read()
		with open(self.name + '.srt', 'wb') as subtitle:
			subtitle.write(response)


instance = DownloadSubs(raw_input())
print instance.download()

