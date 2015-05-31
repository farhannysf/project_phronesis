import aiml
import os
import os.path
import marshal 

AI = aiml.Kernel()
session = AI.getSessionData("Bob")
if os.path.isfile("standard.brn"):
	print 'Loading brain file...'
	print 'Please wait a moment...'
	AI.bootstrap(brainFile = "standard.brn")
	
	sessionFile = file("Bob.ses", "wb")
	marshal.dump(session, sessionFile)
	sessionFile.close()

	sessionFile = file("Bob.ses", "rb")
	session = marshal.load(sessionFile)
	sessionFile.close()
	for pred,value in session.items():
		AI.setPredicate(pred, value, "Bob")
    

else:	AI.setPredicate("secure", "yes")
AI.bootstrap(learnFiles="startup.xml")
AI.respond("LOAD AIML B")
AI.saveBrain("standard.brn")

print '==================================================='
print '    Welcome to Phronesis chatbot version 0.0.3'
print '  Please start typing to begin your conversation.'
print '==================================================='
print ''
while True:
	print AI.respond(raw_input(">"))





