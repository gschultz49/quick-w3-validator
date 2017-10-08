''' Import base modules '''
import sys
import os
import json
import time
import platform
import zipfile
import shutil
import requests
from colors import bcolors

'''
    Designed for use on non-empty, individual directories to evaluate the .html and .php files on the root directory. 
    WARNING there is no caching, so you could get 403'd quickly if you run this validator repeatedly, use sparingly. 
'''

class Individual_Validate():
    def __init__(self, root_path, displayOutput=False, unzip=True):
        self.show_output = displayOutput
        self.error_descriptions = []
        self.root = root_path
        self.html_validator_url = 'http://validator.w3.org/check'
        self.headers = {'Content-Type': 'text/html; charset=utf-8'}
        
        if unzip == True: 
            self.unzip(root_path)
        self.validate(self.root)

    '''
        Unzips the single .zip files in a student's directory
     '''
    def unzip(self, root_path):
        print (bcolors.OKGREEN + "\nUnzipping Website in: {}".format(self.root) + bcolors.ENDC)
        for file in os.listdir(root_path):
            if file.endswith(".zip"):
                zip_loc = os.path.join(root_path, file)
        
        zip_ref = zipfile.ZipFile(zip_loc, 'r')
        zip_ref.extractall(root_path)
        zip_ref.close()

        # don't know why this seems to happen, remove excess directories for macOS
        if "Darwin" in platform.platform():
            rmv_dir = root_path
            if "__MACOSX" in os.listdir(rmv_dir):
                rmv_macOS = os.path.join(rmv_dir, "__MACOSX")
                shutil.rmtree(rmv_macOS)

        # Update root directory to location of unzipped folder. NOTE THERE IS A PROBLEM 
        # IF THEY DON'T ZIP THEIR FOLDER CORRECTLY
        incorrectly_Zipped_folder = 0
        for singleDirectory in os.listdir(root_path):
            # assuming a zip file, an unzipped folder, and a rationale until something is wrong
            if incorrectly_Zipped_folder > 3:
                print (bcolors.FAIL + "THIS FOLDER IS NOT ZIPPED CORRECTLY, MANUALLY CHECK" + bcolors.ENDC)
            if '.' not in singleDirectory:
                newRelativeLocation = os.path.join(root_path, singleDirectory)
                self.root = os.path.join(root_path, newRelativeLocation)
                print ("Update root dir: {}".format(self.root))
            incorrectly_Zipped_folder +=1
                

    '''
        Validates a directory (html files need to be on the root level of this directory)
    '''
    def validate(self, root_path):
        print (bcolors.OKGREEN + "\nValidating {}".format(self.root) + bcolors.ENDC)
        for filename in os.listdir(root_path):
            fullFilePath = os.path.join(root_path, filename)
            if fullFilePath.endswith(".html") or fullFilePath.endswith(".php") :
                print ("\n\tExamining file: {}".format(filename))
                
                # Read in raw html 
                data = open(fullFilePath , 'rb').read()
                # Send to validator, output comes back as JSON
                output = requests.post('https://validator.w3.org/nu/?out=json', headers=self.headers, data=data).json()
                
                # Print out the error messages if they exist
                for entry in output["messages"]:
                    # Ignore PHP related errors (needs more testing)
                    if "<?php" not in entry["extract"]:    
                        # If a valid HTML error, print it out
                        if entry["type"] == "error":
                            self.error_descriptions.append(entry["message"])
                            print ("\t\t" + bcolors.FAIL + "ERROR FOUND!" + bcolors.ENDC)
                            print ("\t\t" + entry["message"])
                
                # If you want to see the raw JSON output for each file, pass a 'True' into the class initializer, 
                # This is NOT enabled by default
                if self.show_output: 
                    print ("Displaying file's output...")
                    print("\t\t+"+json.dumps(output, indent=4, sort_keys=True))
                
                
        # No errors in this directory
        if len(self.error_descriptions) == 0:
            print ("\n" + bcolors.OKGREEN + "No errors found!" + bcolors.ENDC)
        
        # Don't hurt the w3 server too much ;) 
        time.sleep(2)
        
if __name__ == '__main__':
    if len (sys.argv) >= 2:
        Individual_Validate(sys.argv[1], displayOutput=False)  
        
