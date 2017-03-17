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

	for package, target in imports.items():
		try:
			globals()[target] = __import__(package)
			printFlush("**" + package + " imported.\n\n")
		except ImportError as e:
			printFlush("The " + package + " package is not currently installed on this machine."
					+ "\nThe "+ package + " package is needed in order for this script to run.")
			resp = input("Would you like to install the " + package + " package?\n\t[Y]es or [N]o:")

			# If invalid reponse is given, continuing asking until a valid response is given
			while (resp.upper() != "Y" and resp.upper() != "YES"
				and resp.upper() != "N" and resp.upper() != "NO"):
				resp = input("Invalid response.\nWould you like to install the " + resp + " package?\n\t[Y]es or [N]o: ")
			
			# Install package with pip if the user allows it, exit the script otherwise
			if (resp.upper() == "Y" or resp.upper() == "YES"):
				printFlush("Installing " + package + "...")
				import pip
				pip.main(['install', package])
				printFlush("**" + package + " installed.")

				globals()[target] = __import__(package)
				printFlush("**" + package + " imported.\n\n")
			else:
				import time
				printFlush(package + " will not be installed.\n\tClosing script...")
				time.sleep(3);
				sys.exit()
		

# There is currently no way to obtain GitHub Audit Log's through GitHub's API, 
# so this function will prompt user to specify the Audit Log filepath
# Audit Logs should be .csv files
def getAuditLog():
	pass

def preProcess():
	checkImports()
	getAuditLog()

def main():
	preProcess()

if __name__ == "__main__":
	main()