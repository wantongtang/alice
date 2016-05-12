import os
import aiml
os.chdir('/usr/local/lib/python2.7/dist-packages/aiml/alice')
alice = aiml.Kernel()
alice.learn("startup.xml")
alice.respond('LOAD ALICE')

while True:
	print alice.respond(raw_input("enter your message>>"))
