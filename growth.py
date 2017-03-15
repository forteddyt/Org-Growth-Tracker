import sys
import os


# A simple print with a system flush afterwards
def printFlush(string = ''):
	print(string)
	sys.stdout.flush()

# Ensures that the pandas, numpy, and matplotlib imports are installed
def checkImports():
	imports = ['numpy', 'pandas', 'matplotlib']

	for package in imports:
		try:
			__import__(package)
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

				__import__(package)
				printFlush("**" + package + " imported.\n\n")			
			else:
				import time
				printFlush(package + " will not be installed.\n\tClosing script...")
				time.sleep(3);
				sys.exit()
		

def main():
	checkImports()	

if __name__ == "__main__":
	main()