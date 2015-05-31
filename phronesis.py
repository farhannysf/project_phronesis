import aiml
import os
import os.path 

AI = aiml.Kernel()
if 	os.path.isfile("standard.brn"):
	print 'Loading brain file...'
	print 'Please wait a moment...'
	AI.bootstrap(brainFile = "standard.brn")

else:	AI.setPredicate("secure", "yes")
	AI.bootstrap(learnFiles="startup.xml")
	AI.respond("LOAD AIML B")
	AI.saveBrain("standard.brn")

print '==================================================='
print '    Welcome to Phronesis chatbot version 0.0.2'
print '  Please start typing to begin your conversation.'
print '==================================================='
print ''
while True:
	print AI.respond(raw_input(">"))





