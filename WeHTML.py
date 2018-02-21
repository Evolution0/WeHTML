import os

def Start():
	print ""
	print "WeHTML initially made by Aidan Welch"
	print ""

	print("This is a tool for converting HTML code into code usable with Wemos.")
	raw_input("Press Enter(Return) to continue...")
	FindFile()


def FindFile():
	location = raw_input("Input your file's location: ")
	if len(location) < 1:
		print ("You didn't type anything")
		FindFile()
	else:
		 #Opens the file and finds it
		 file = open(location, "r")
		 print "Following will be the first 4 characters of " + os.path.basename(location) + ":"
		 print file.read(4)
		 unanswered = True
		 while unanswered == True:
		 	answer = raw_input("Type Y if correct or N if false: ")
		 	if answer.upper() == "Y":
		 		GetHTML(location)
		 		unanswered = False
		 	elif answer.upper() == "N":
		 		FindFile()
		 		unanswered = False
		 	else:
		 		unanswered = True


def file_len(location):  #credit for this goes to https://www.safaribooksonline.com/library/view/python-cookbook/0596001673/ch04s07.html
	num_lines = 0
	for line in open(location).xreadlines( ):
		num_lines += 1
	print("I counted " + str(num_lines) + " lines")
	return(num_lines)

def GetHTML(location):
	#must reopen file because everytime file is read it saves cursor position
	lineCount = file_len(location)
	file = open(location, "r")
	newfile = open(raw_input("Where should the new file(include the name for the file in the path) be saved: "), "w")

	client = raw_input("What is the name of the variable holding your WI-FI client: ")
	i = 0
 	while i < lineCount:
 		print(i)
 		if i == lineCount - 1:
 			newfile.write(client + ".println(\"" + file.readline() + "\"); \n")
 		else:
 			newfile.write(client + ".println(\"" + file.readline()[:-1] + "\"); \n")
 		i += 1

 	print("Done!")
	unanswered = False

Start() #starting Start()