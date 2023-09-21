class Server:
	
	server = None
	@classmethod
	def get_server(cls):
		if cls.server:
			cls.server = Server()
		
		return cls.server
	
	def init(self):
		pass
