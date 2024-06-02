import sqlite3

class Database:
	def __init__(self, db_file):
		self.connection = sqlite3.connect(db_file)
		self.cursor = self.connection.cursor()

	def user_exists(self, user_id):
		with self.connection:
			result = self.cursor.execute("SELECT * FROM `users` WHERE `user_id` = ?", (user_id,)).fetchall()
			return bool(len(result))

	def add_user(self, user_id, referrer_id=None):
		with self.connection:
			if referrer_id != None:
				return self.cursor.execute("INSERT INTO `users` (`user_id`, `referrer_id`) VALUES (?,?)", (user_id, referrer_id,))
			else:
				return self.cursor.execute("INSERT INTO `users` (`user_id`) VALUES (?)", (user_id,))

	def count_reeferals(self, user_id):
		with self.connection:
			return self.cursor.execute("SELECT COUNT(`id`) as count FROM `users` WHERE `referrer_id` =?", (user_id,)).fetchone()[0]

	
	
	
	
	def set_active(self, user_id, active):
		with self.connection:
			return self.cursor.execute("UPDATE `users` SET `active` = ? WHERE `user_id` = ?", (active, user_id,))

	def get_user(self):
		with self.connection:
			return self.cursor.execute("SELECT `user_id`, `active` FROM `users`").fetchall()

	def add_points_ref(self, user_id):
		with self.connection:
			return self.cursor.execute("UPDATE users SET `points` = `points` + 10 WHERE `user_id` = ?", (user_id,))

	def add_click(self, user_id):
		with self.connection:
			return self.cursor.execute("UPDATE users SET `click` = `click` + 1 WHERE `user_id` = ?", (user_id,))

	def get_points(self, user_id):
		with self.connection:
			self.cursor.execute("select points from users where user_id = ?", (user_id,))
			result = self.cursor.fetchone()
			if result:
				return result[0]
			else:
				return 0

	def get_click(self, user_id):
		with self.connection:
			self.cursor.execute("select click from users where user_id = ?", (user_id,))
			result = self.cursor.fetchone()
			if result:
				return result[0]
			else:
				return 0

	def add_user_name(self, user_id, user_name):
		with self.connection:
			return self.cursor.execute("UPDATE `users` SET `user_name` = ? WHERE `user_id` = ?", (user_name, user_id,))

	def get_user_name(self, user_id):
		with self.connection:
			self.cursor.execute("select user_name from users where user_id = ?", (user_id,))
			result = self.cursor.fetchone()
			if result:
				return result[0]
			else:
				return None

	def add_points_sub(self, user_id):
		with self.connection:
			return self.cursor.execute("UPDATE `users` SET `points` = `points` + 50 WHERE `user_id` = ?", (user_id,))


	#Gorillza-sub
	def get_sub_points_added_gorillza(self, user_id):
		with self.connection:
			self.cursor.execute("SELECT `sub_points_added_gorillza` FROM `users` WHERE `user_id` = ?", (user_id,))
			result = self.cursor.fetchone()
			if result:
				return bool(result[0])
			else:
				return False

	def set_sub_points_added_gorillza(self, user_id):
		with self.connection:
			return self.cursor.execute("UPDATE `users` SET `sub_points_added_gorillza` = TRUE WHERE `user_id` = ?", (user_id,))

	#RCSNews-sub
	def get_sub_points_added_rcsnews(self, user_id):
		with self.connection:
			self.cursor.execute("SELECT `sub_points_added_rcsnews` FROM `users` WHERE `user_id` = ?", (user_id,))
			result = self.cursor.fetchone()
			if result:
				return bool(result[0])
			else:
				return False

	def set_sub_points_added_rcsnews(self, user_id):
		with self.connection:
			return self.cursor.execute("UPDATE `users` SET `sub_points_added_rcsnews` = TRUE WHERE `user_id` = ?", (user_id,))

	#Grlchat-sub
	def get_sub_points_added_grlchat(self, user_id):
		with self.connection:
			self.cursor.execute("SELECT `sub_points_added_grlchat` FROM `users` WHERE `user_id` = ?", (user_id,))
			result = self.cursor.fetchone()
			if result:
				return bool(result[0])
			else:
				return False

	def set_sub_points_added_grlchat(self, user_id):
		with self.connection:
			return self.cursor.execute("UPDATE `users` SET `sub_points_added_grlchat` = TRUE WHERE `user_id` = ?", (user_id,))

	#Rcs-sub
	def get_sub_points_added_rcs(self, user_id):
		with self.connection:
			self.cursor.execute("SELECT `sub_points_added_rcs` FROM `users` WHERE `user_id` = ?", (user_id,))
			result = self.cursor.fetchone()
			if result:
				return bool(result[0])
			else:
				return False

	def set_sub_points_added_rcs(self, user_id):
		with self.connection:
			return self.cursor.execute("UPDATE `users` SET `sub_points_added_rcs` = TRUE WHERE `user_id` = ?", (user_id,))

	#YourHypeWave-sub
	def get_sub_points_added_yhw(self, user_id):
		with self.connection:
			self.cursor.execute("SELECT `sub_points_added_yhw` FROM `users` WHERE `user_id` = ?", (user_id,))
			result = self.cursor.fetchone()
			if result:
				return bool(result[0])
			else:
				return False

	def set_sub_points_added_yhw(self, user_id):
		with self.connection:
			return self.cursor.execute("UPDATE `users` SET `sub_points_added_yhw` = TRUE WHERE `user_id` = ?", (user_id,))
			

	#TON Hedge
	def get_sub_points_added_hedge(self, user_id):
		with self.connection:
			self.cursor.execute("SELECT `sub_points_added_hedge` FROM `users` WHERE `user_id` = ?", (user_id,))
			result = self.cursor.fetchone()
			if result:
				return bool(result[0])
			else:
				return False

	def set_sub_points_added_hedge(self, user_id):
		with self.connection:
			return self.cursor.execute("UPDATE `users` SET `sub_points_added_hedge` = TRUE WHERE `user_id` = ?", (user_id,))

	#Ferox
	def get_sub_points_added_richnet(self, user_id):
		with self.connection:
			self.cursor.execute("SELECT `sub_points_added_richnet` FROM `users` WHERE `user_id` = ?", (user_id,))
			result = self.cursor.fetchone()
			if result:
				return bool(result[0])
			else:
				return False

	def set_sub_points_added_richnet(self, user_id):
		with self.connection:
			return self.cursor.execute("UPDATE `users` SET `sub_points_added_richnet` = TRUE WHERE `user_id` = ?", (user_id,))

	#Mush
	def get_sub_points_added_mush(self, user_id):
		with self.connection:
			self.cursor.execute("SELECT `sub_points_added_mush` FROM `users` WHERE `user_id` = ?", (user_id,))
			result = self.cursor.fetchone()
			if result:
				return bool(result[0])
			else:
				return False

	def set_sub_points_added_mush(self, user_id):
		with self.connection:
			return self.cursor.execute("UPDATE `users` SET `sub_points_added_mush` = TRUE WHERE `user_id` = ?", (user_id,))

	#Alteriat
	def get_sub_points_added_alteriat(self, user_id):
		with self.connection:
			self.cursor.execute("SELECT `sub_points_added_alteriat` FROM `users` WHERE `user_id` = ?", (user_id,))
			result = self.cursor.fetchone()
			if result:
				return bool(result[0])
			else:
				return False

	def set_sub_points_added_alteriat(self, user_id):
		with self.connection:
			return self.cursor.execute("UPDATE `users` SET `sub_points_added_alteriat` = TRUE WHERE `user_id` = ?", (user_id,))

	#Ded
	def get_sub_points_added_ded(self, user_id):
		with self.connection:
			self.cursor.execute("SELECT `sub_points_added_ded` FROM `users` WHERE `user_id` = ?", (user_id,))
			result = self.cursor.fetchone()
			if result:
				return bool(result[0])
			else:
				return False

	def set_sub_points_added_ded(self, user_id):
		with self.connection:
			return self.cursor.execute("UPDATE `users` SET `sub_points_added_ded` = TRUE WHERE `user_id` = ?", (user_id,))

	#Shaurma
	def get_sub_points_added_shaurma(self, user_id):
		with self.connection:
			self.cursor.execute("SELECT `sub_points_added_shaurma` FROM `users` WHERE `user_id` = ?", (user_id,))
			result = self.cursor.fetchone()
			if result:
				return bool(result[0])
			else:
				return False

	def set_sub_points_added_shaurma(self, user_id):
		with self.connection:
			return self.cursor.execute("UPDATE `users` SET `sub_points_added_shaurma` = TRUE WHERE `user_id` = ?", (user_id,))

	#Lama
	def get_sub_points_added_lama(self, user_id):
		with self.connection:
			self.cursor.execute("SELECT `sub_points_added_lama` FROM `users` WHERE `user_id` = ?", (user_id,))
			result = self.cursor.fetchone()
			if result:
				return bool(result[0])
			else:
				return False

	def set_sub_points_added_lama(self, user_id):
		with self.connection:
			return self.cursor.execute("UPDATE `users` SET `sub_points_added_lama` = TRUE WHERE `user_id` = ?", (user_id,))

	#Pixel
	def get_sub_points_added_pixel(self, user_id):
		with self.connection:
			self.cursor.execute("SELECT `sub_points_added_pixel` FROM `users` WHERE `user_id` = ?", (user_id,))
			result = self.cursor.fetchone()
			if result:
				return bool(result[0])
			else:
				return False

	def set_sub_points_added_pixel(self, user_id):
		with self.connection:
			return self.cursor.execute("UPDATE `users` SET `sub_points_added_pixel` = TRUE WHERE `user_id` = ?", (user_id,))

	#Raid
	def get_sub_points_added_raid(self, user_id):
		with self.connection:
			self.cursor.execute("SELECT `sub_points_added_raid` FROM `users` WHERE `user_id` = ?", (user_id,))
			result = self.cursor.fetchone()
			if result:
				return bool(result[0])
			else:
				return False

	def set_sub_points_added_raid(self, user_id):
		with self.connection:
			return self.cursor.execute("UPDATE `users` SET `sub_points_added_raid` = TRUE WHERE `user_id` = ?", (user_id,))

	#Elixir
	def get_sub_points_added_elixir(self, user_id):
		with self.connection:
			self.cursor.execute("SELECT `sub_points_added_elixir` FROM `users` WHERE `user_id` = ?", (user_id,))
			result = self.cursor.fetchone()
			if result:
				return bool(result[0])
			else:
				return False

	def set_sub_points_added_elixir(self, user_id):
		with self.connection:
			return self.cursor.execute("UPDATE `users` SET `sub_points_added_elixir` = TRUE WHERE `user_id` = ?", (user_id,))

	#Wenster
	def get_sub_points_added_wenster(self, user_id):
		with self.connection:
			self.cursor.execute("SELECT `sub_points_added_wenster` FROM `users` WHERE `user_id` = ?", (user_id,))
			result = self.cursor.fetchone()
			if result:
				return bool(result[0])
			else:
				return False

	def set_sub_points_added_wenster(self, user_id):
		with self.connection:
			return self.cursor.execute("UPDATE `users` SET `sub_points_added_wenster` = TRUE WHERE `user_id` = ?", (user_id,))

	#Airton
	def get_sub_points_added_airton(self, user_id):
		with self.connection:
			self.cursor.execute("SELECT `sub_points_added_airton` FROM `users` WHERE `user_id` = ?", (user_id,))
			result = self.cursor.fetchone()
			if result:
				return bool(result[0])
			else:
				return False

	def set_sub_points_added_airton(self, user_id):
		with self.connection:
			return self.cursor.execute("UPDATE `users` SET `sub_points_added_airton` = TRUE WHERE `user_id` = ?", (user_id,))
	
	def get_top_referrals(self, limit=10):
		with self.connection:
			return self.cursor.execute("SELECT referrer_id, COUNT(*) AS count FROM users GROUP BY referrer_id ORDER BY count DESC LIMIT ?", (limit,)).fetchall()