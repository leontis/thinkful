import sys
import argparse
import logging
import csv 
# Set the log output file, and the log level
logging.basicConfig(filename="output.log", level=logging.DEBUG)
 
def put(name, snippet, filename):
    """ Store a snippet with an associated name in the CSV file """
    logging.info("Writing {}:{} to {}".format(name, snippet, filename))
    logging.debug("Opening file")
    with open(filename, "a") as f:
        writer = csv.writer(f)
        logging.debug("Writing snippet to file".format(name, snippet))
        writer.writerow([name, snippet])
    logging.debug("Write sucessful")
    return name, snippet

def get(snippet_name,filename):
	logging.info("Reading {} from {}".format(snippet_name,filename))
	logging.debug("opening file")	
	print "snippet_name is: " + snippet_name
 	print "filename is: " + filename
	with open(filename, "r+") as f:
		reader = csv.reader(f)
		logging.debug("reading snippet from file".format(snippet_name))
		for row in reader:
			if snippet_name in row:
				snippet = " ".join(row)
                snippet=list(snippet)
                print snippet
	logging.debug("Read succesful")
	return snippet
 
def make_parser():
	logging.info("Constructing parser")
	description = "Store and retrieve snippets of text"
	parser = argparse.ArgumentParser(description = description)
	subparsers = parser.add_subparsers(dest="command",help="Available commands")
	#Subparser for the put command
	logging.debug("constructing put subparser")
	put_parser = subparsers.add_parser("put",help="Store a snippet")
	put_parser.add_argument("name",help="The name of the snippet")
	put_parser.add_argument("snippet",help="The snippet text")
	put_parser.add_argument("filename",default = "snippets.csv",nargs="?",help="The snippet filename")

	#Subparser for the get command
	logging.debug("Constructing get subparser")
	get_parser = subparsers.add_parser("get",help="Retrieve a snippet")
	get_parser.add_argument("name",help="The name of the snippet")
	get_parser.add_argument("filename",default = "snippets.csv",nargs="?",help="The snippet filename")

	return parser
 
def main():
    """ Main function """
    logging.info("Starting snippets")
    parser = make_parser()
    arguments = parser.parse_args(sys.argv[1:])
    # Convert parsed arguments from Namespace to dictionary
    arguments = vars(arguments)
    command = arguments.pop("command")

    if command == "get":
    	print "command is '{}'".format(command)
    	snippet_name = arguments.pop("name")
    	file_name = arguments.pop("filename")
    	snippet = get(snippet_name,file_name)
    	print "Retrieved '{}' as '{}'".format(snippet_name, snippet)
    elif command == "put":
        name, snippet = put(**arguments)
        print "Stored '{}' as '{}'".format(snippet, name)
        print "command is '{}'".format(command)
    else:
        print "Command not found"
    return    
 
if __name__ == "__main__":
    main()
    