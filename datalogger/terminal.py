import argparse
import sys

def QuoteHelpText():
	print "\t Name: \t quote"
	print "\t Args: \t [symbol]"
	print "\t Func: \t Gets quote data for the ticker/symbol passed."
	

def QueryCommand(tokens):
	qt = query.QueryTool()
	
	# Type of query.
	type = tokens[1]
	
	if len(tokens) < 3:
		print "Usage: "
		QuoteHelpText()
	else:
		if type == "quote":
			s = []
			s.append(tokens[2])

			qt.GetQuotes(s)
	
	return

def HelpText():
	print "TD Ameritrade API Query Tool"
	print "Version 0.0.1"
	print "Program Name: " + "'" + "query" + "'" + "\n\n"
	
	print "Command List:"
	print "** Brackets [] denote required command arguments. **\n"

	return

def Run():
	text = raw_input(">> ")
	type(text)
	
	while text != "quit":
		
		# Break the input into tokens.
		tokens 	= text.split()
		command = tokens[0]
		
		# Do stuff.
		if command == "help":
			HelpText()
		elif command == "query":
			QueryCommand(tokens)
		else:
			print "'" + command + "'" + " is not a valid command."
		
		text = raw_input(">> ")
		type(text)

	print "Program Exit."

	return
	
if __name__ == "__main__":
	# Include the path to the query files.
	sys.path.insert(0, './querytool')
	
	from querytool import query

	Run()