import sqlalchemy as sqla
class Database:
	def __init(self):
		self.engine = sqla.create_engine("mysql+pymysql://is61-4:na8xwxpz@192.168.3.111/db")
		self.connection = self.engine.connect()

	def get_stats(self):
		query = sqla.text("SELECT * FROM stats")
		response = self.connection.execute(query).all()
		result = []
		for r in response:
			result.append(r._asdict())
		return result

	def add_stats(self, score):
		query = sqla.text("INSERT INTO stats (score) VALUES (:score)")
		query = query.bindparams(sqla.bindparam("score", score))
		self.connection.execute(query)
		self.connection.commit()