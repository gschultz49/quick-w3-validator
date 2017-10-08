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
        self.err_files ={}
        self.root = root_path
        self.html_validator_url = 'http://validator.w3.org/check'
        self.headers = {'Content-Type': 'text/html; charset=utf-8'}
        self.toValidate =[]
        self.netID = os.path.basename(root_path)
        
        if unzip == True: 
            self.unzip(root_path)
        
        self.absoluteFilePaths(root_path)
        self.validate()

    '''
        Unzips the single .zip file in a student's directory
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
        
        
    '''Controller for the validation'''   
    def validate(self):
        print (bcolors.OKGREEN + "\nValidating Student:{}".format(self.root) + bcolors.ENDC)
        for file in self.toValidate:
            self.runValidation(file)
            time.sleep(0.5)

        # No errors in this student
        if len(self.error_descriptions) == 0:
            print ("\n\t" + bcolors.OKGREEN + "No errors found!" + bcolors.ENDC)
        
    ''' Actually validates this students particular files'''
    def runValidation(self, fullFilePath):
        print ("\n\tExamining file: {}".format(fullFilePath))
        
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
                    # self.err_files.append(os.path.basename(fullFilePath))
                    if self.netID in self.err_files:
                        self.err_files[self.netID].add(os.path.basename(fullFilePath))
                    else:
                        self.err_files[self.netID] = {os.path.basename(fullFilePath)}

                    print ("\t\t" + bcolors.FAIL + "ERROR FOUND!" + bcolors.ENDC)
                    print ("\t\t" + entry["message"])
        
        # If you want to see the raw JSON output for each file, pass a 'True' into the class initializer, 
        # This is NOT enabled by default
        if self.show_output: 
            print ("Displaying file's output...")
            print("\t\t+"+json.dumps(output, indent=4, sort_keys=True))
        
    '''recurses through directory and gets .html or .php files for validation'''
    def absoluteFilePaths(self,directory):
        for dirpath,_,filenames in os.walk(directory):
            for f in filenames:
                if f.endswith(".html") or f.endswith(".php"):
                    self.toValidate.append(os.path.abspath(os.path.join(dirpath, f)))
                    # yield os.path.abspath(os.path.join(dirpath, f))
                
if __name__ == '__main__':
    if len (sys.argv) >= 2:
        Individual_Validate(sys.argv[1], displayOutput=False, )  
        
