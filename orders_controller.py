import json

def __init__(self, filepath):
		print('__init__')

		self.filepath = filepath

	def open_data(self):
		self.users = open(self.filepath, 'r').read()
		self.users = json.loads(self.users)

	def save_data(self):
		users_str = json.dumps(self.users)

		open(self.filepath, 'w').write(users_str)