import aiml

AI = aiml.Kernel()
AI.verbose(False)
AI.setPredicate("secure", "yes")
AI.learn("startup.xml")
AI.respond("LOAD AIML B")
while True:
	print AI.respond(raw_input(">"))




