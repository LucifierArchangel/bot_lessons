import json

class UsersController:
	def __init__(self, filepath):
		print('__init__')

		self.filepath = filepath
		self.open_data()

	def open_data(self):
		self.users = open(self.filepath, 'r').read()
		self.users = json.loads(self.users)

	def save_data(self):
		users_str = json.dumps(self.users)

		open(self.filepath, 'w').write(users_str)

	def add_user(self, username, user_id, ref):
		if self.user_does_not_exist(user_id):
			db_id = len(self.users) + 1

			user = {
				'id': db_id,
				'username': username,
				'user_id': user_id,
				"balance": 0.0,
				'ref': ref
			}

			self.users.append(user)

			self.save_data()

	def user_does_not_exist(self, user_id):
		for user in self.users:
			if user['user_id'] == user_id:
				return False

		return True


