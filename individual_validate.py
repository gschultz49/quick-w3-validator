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
    Designed for validating a non-empty, individual directory, and (possibly) with a .zip file containing the student's website.
    WARNING there is no caching, so you could get 403'd quickly if you run this validator repeatedly, use sparingly. 

    self.
        show_output (Boolean:False) : Show Validation output for each file
        error_descriptions (List) : 
        err_files (Dict) : Tracks which files have errors for this student 
                      ex :  {self.netID : {'err_file1.html', 'err_file2.html} }
        root (String) : Absolute path to the CMS output directory
        html_validator_url (String) : w3 validation service endpoint
        headers (JSON) : Headers for w3 validation
        files_to_validate (List[String]) : .html or .php files that need to be validated for this student
        netID (String) : Student's netID
'''

class Individual_Validate():
    def __init__(self, root_path, display_output=False, unzip=True):
        self.show_output = display_output
        self.error_descriptions = []
        self.err_files ={}
        self.root = root_path
        self.html_validator_url = 'http://validator.w3.org/check'
        self.headers = {'Content-Type': 'text/html; charset=utf-8'}
        self.files_to_validate =[]
        self.netID = os.path.basename(root_path)
        
        if unzip == True: 
            self.unzip(self.root)
        
        self.getAbsFilePathsToValidate(root_path)
        self.validate()

    '''
        Unzips the single .zip file from this student's directory
        root_path (String) : Absolute path to directory containing a zipped file
     '''
    def unzip(self, root_path):
        print (bcolors.OKGREEN + "\nUnzipping Website in: {}".format(self.root) + bcolors.ENDC)
        zipped_file_count = 0
        for file in os.listdir(root_path):
            if file.endswith(".zip"):
                if zipped_file_count > 0 : 
                    assert ("Too many zipped files!")
                else:
                    zip_loc = os.path.join(root_path, file)
                
                zipped_file_count += 1
        
        zip_ref = zipfile.ZipFile(zip_loc, 'r')
        zip_ref.extractall(root_path)
        zip_ref.close()

        # Don't know why this seems to happen, remove __MACOSX directory for macOS
        if "Darwin" in platform.platform():
            rmv_dir = root_path
            if "__MACOSX" in os.listdir(rmv_dir):
                rmv_macOS = os.path.join(rmv_dir, "__MACOSX")
                shutil.rmtree(rmv_macOS)
        
        
    '''
        Controller for the validation, passes each students unzipped directory to the validator
    '''   
    def validate(self):
        print (bcolors.OKGREEN + "\nValidating Student:{}".format(self.root) + bcolors.ENDC)
        for file in self.files_to_validate:
            self.runValidation(file)
            time.sleep(0.5)

        # No errors in this student
        if len(self.error_descriptions) == 0:
            print ("\n\t" + bcolors.OKGREEN + "No errors found!" + bcolors.ENDC)
        
    '''
        Validates an individual file through the w3 validation service
        path_to_file (String) : Absolute path to a students file
    '''
    def runValidation(self, path_to_file):
        print ("\n\tExamining file: {}".format(path_to_file))
        # Read in raw html 
        data = open(path_to_file , 'rb').read()
        # Send to validator, output comes back as JSON
        output = requests.post('https://validator.w3.org/nu/?out=json', headers=self.headers, data=data).json()
        
        # Print out the error messages if they exist
        for entry in output["messages"]:
            # Ignore PHP related errors (needs more testing)
            if "<?php" not in entry["extract"]:    
                # If a valid HTML error, print it out
                if entry["type"] == "error":
                    self.error_descriptions.append(entry["message"])

                    if self.netID in self.err_files:
                        self.err_files[self.netID].add(os.path.basename(path_to_file))
                    else:
                        self.err_files[self.netID] = {os.path.basename(path_to_file)}

                    print ("\t\t" + bcolors.FAIL + "ERROR FOUND!" + bcolors.ENDC)
                    print ("\t\t" + entry["message"])
        
        # If you want to see the raw JSON output for each file, pass a 'True' into display_output, 
        # This is NOT enabled by default
        if self.show_output: 
            print ("Displaying file's output...")
            print("\t\t+"+json.dumps(output, indent=4, sort_keys=True))
        
    '''
        Recurses through directory and gets .html or .php files for validation
        directory (String) : Absolute path to a student's unzipped directory
    '''
    def getAbsFilePathsToValidate(self,directory):
        for dirpath,_,filenames in os.walk(directory):
            for f in filenames:
                if f.endswith(".html") or f.endswith(".php"):
                    self.files_to_validate.append(os.path.abspath(os.path.join(dirpath, f)))
                
if __name__ == '__main__':
    if len (sys.argv) >= 2:
        Individual_Validate(sys.argv[1], display_output=False)  
        
