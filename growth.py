import sys
import os


# A simple print with a system flush afterwards
def printFlush(string = ''):
	print(string)
	sys.stdout.flush()

# Ensures that the pandas, numpy, and matplotlib imports are installed
# Imports them with a local name specified by the dictionary
def checkImports():
	imports = {'numpy':'np', 'pandas':'py', 'matplotlib':'mp'}

	print(sys.version)

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
		

# There is currently no way to obtain GitHub Audit Log's through GitHub's API, 
# so this function will prompt user to specify the Audit Log filepath
# Audit Logs should be .csv files
def getAuditLog():
	from tkinter import Tk
	from tkinter import filedialog

	root = Tk()

	root.withdraw() # we don't want a full GUI, so keep the root window from appearing
	file_path = filedialog.askopenfilename() # show an "Open" dialog box and return the path to the selected file
	print(file_path)

	pass

def preProcess():
	checkImports()
	printFlush("Select the GitHub Audit Log .csv file")
	getAuditLog()

def main():
	preProcess()

if __name__ == "__main__":
	main()