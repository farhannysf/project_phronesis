import aiml
import os 

AI = aiml.Kernel()
AI.setPredicate("secure", "yes")
AI.bootstrap(learnFiles="startup.xml")
AI.respond("LOAD AIML B")
while True:
	print AI.respond(raw_input(">"))




