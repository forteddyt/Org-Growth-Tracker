import sys
import os


# A simple print with a system flush afterwards
def printFlush(string = ''):
	print(string)
	sys.stdout.flush()

# Ensures that the pandas, numpy, and matplotlib imports are installed
# Imports them with a local name specified by the dictionary
def checkImports():
	# Module name to be imported mapping to the string which is will be reffered to as
	imports = {'numpy':'np', 'pandas':'py', 'matplotlib':'mp'}

	printFlush(sys.version)

	for module, target in imports.items():
		try:
			globals()[target] = __import__(module)
			printFlush("**" + module + " imported.")
		except ImportError as e:
			printFlush("The " + module + " module is not currently installed on this machine."
					+ "\nThe "+ module + " module is needed in order for this script to run.")
			resp = input("Would you like to install the " + module + " module?\n\t[Y]es or [N]o:")

			# If invalid reponse is given, continuing asking until a valid response is given
			while (resp.upper() != "Y" and resp.upper() != "YES"
				and resp.upper() != "N" and resp.upper() != "NO"):
				resp = input("Invalid response.\nWould you like to install the " + resp + " module?\n\t[Y]es or [N]o: ")
			
			# Install module with pip if the user allows it, exit the script otherwise
			if (resp.upper() == "Y" or resp.upper() == "YES"):
				printFlush("Installing " + module + "...")
				import pip
				pip.main(['install', module])
				printFlush("**" + module + " installed.")

				if(target != ''):
					globals()[target] = __import__(module)
				else:
					__import__(module)
				printFlush("**" + module + " imported.\n\n")
			else:
				import time
				printFlush(module + " will not be installed.\n\tClosing script...")
				time.sleep(3);
				sys.exit()

	printFlush("Modules importing complete!\n")
		

# There is currently no way to obtain GitHub Audit Log's through GitHub's API, 
# so this function will prompt user to specify the Audit Log filepath
# Audit Logs should be .csv files
def getAuditLogTK():
	from tkinter import Tk
	from tkinter import filedialog

	root = Tk()

	root.withdraw() # we don't want a full GUI, so keep the root window from appearing
	
	printFlush("Select the GitHub Audit Log .csv file")

	file_path = filedialog.askopenfilename() # show an "Open" dialog box and return the path to the selected file
	
	# printFlush(file_path)

	return file_path

def getAuditLogFallback():
	filePath = input('Please provide the full path to the .csv Audit Log file:\n')

	# printFlush(filePath)

	return filePath

def getAuditLog():
	try:
		return getAuditLogTK()
	except ImportError as e:
		printFlush("Tkinter installation not found, falling back to console input.")
		return getAuditLogFallback()


def preProcess():
	from pathlib import Path
	
	checkImports()
	
	filePath = getAuditLog()
	file = Path(filePath)
	while not file.is_file():
		printFlush("\n*** Invalid file path -- '" + filePath + "' does not exist.")
		printFlush("*** Trying again...")
		filePath = getAuditLog()
		file = Path(filePath)

def main():
	preProcess()

if __name__ == "__main__":
	main()