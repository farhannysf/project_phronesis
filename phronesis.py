import aiml
import os
import os.path
import marshal 

AI = aiml.Kernel()
session = AI.getSessionData("Phronesis")
if os.path.isfile("Phronesis.brn"):
	print 'Loading brain file...'
	print 'Please wait a moment...'
	AI.bootstrap(brainFile = "Phronesis.brn")
	
	sessionFile = file("Phronesis.ses", "wb")
	marshal.dump(session, sessionFile)
	sessionFile.close()

	sessionFile = file("Phronesis.ses", "rb")
	session = marshal.load(sessionFile)
	sessionFile.close()
	for pred,value in session.items():
		AI.setPredicate(pred, value, "Phronesis")
    

else:	AI.setPredicate("secure", "yes")
AI.bootstrap(learnFiles="startup.xml")
AI.respond("LOAD AIML B")
AI.saveBrain("Phronesis.brn")

sessionFile = file("Phronesis.ses", "wb")
marshal.dump(session, sessionFile)
sessionFile.close()

sessionFile = file("Phronesis.ses", "rb")
session = marshal.load(sessionFile)
sessionFile.close()
for pred,value in session.items():
	AI.setPredicate(pred, value, "Phronesis")

print '====================================================================='
print '            Welcome to Phronesis chatbot version 0.0.4'
print '   This program was developed by Farhan Yusuf and Penske Williano'
print '          Please start typing to begin your conversation.'
print '====================================================================='
print ''
while True:
	print AI.respond(raw_input(">"))



