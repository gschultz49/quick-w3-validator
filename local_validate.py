''' Import base modules '''
import sys
import os
import json
import time
import requests
from colors import bcolors

'''
    Designed for use on individual directories to evaluate the .html files on the root directory. 
    WARNING there is no caching, so you could get 403'd quickly if you run this validator repeatedly, use sparingly. 
'''

class LocalValidator():
    def __init__(self, root_path, displayOutput=False):
        self.show_output = displayOutput
        self.error_descriptions = []
        self.root = root_path
        self.html_validator_url = 'http://validator.w3.org/check'
        self.headers = {'Content-Type': 'text/html; charset=utf-8'}

        print (bcolors.OKGREEN + "\nValidating {}".format(self.root) + bcolors.ENDC)
        self.validate(root_path)

    '''
        Validates a directory (html files need to be on the root level of this directory)
    '''
    def validate(self, root_path):
        print (os.listdir(root_path))
        for filename in os.listdir(root_path):
            
            fullFilePath = os.path.join(root_path, filename)
            
            if fullFilePath.endswith(".html"):
                print ("Entering")
                print ("The fullFilePath: {}".format(fullFilePath))
                print ("\n\tExamining file: {}".format(filename))
                
                # read in raw html and send to it to the w3 validator
                data = open(fullFilePath , 'rb').read()
                
                # output comes back as JSON
                output = requests.post('https://validator.w3.org/nu/?out=json', headers=self.headers, data=data).json()
                
                # print out the error messages if they exist
                for entry in output["messages"]:
                    if entry["type"] == "error":
                        self.error_descriptions.append(entry["message"])
                        print ("\t" + bcolors.FAIL + "ERROR FOUND!" + bcolors.ENDC)
                        print ("\t" + entry["message"])
                
                # if you want to see the raw JSON output for each file, pass a 'True' into the class initializer, 
                # this is NOT enabled by default
                if self.show_output: 
                    print ("Displaying file's output...")
                    print(json.dumps(output, indent=4, sort_keys=True))
                
                
        # no Errors in this directory
        if len(self.error_descriptions) == 0:
            print ("\t" + bcolors.OKGREEN + "No errors found!" + bcolors.ENDC)
        
        # Don't hurt the w3 server too much ;) 
        time.sleep(2)
        
if __name__ == '__main__':
    if len (sys.argv) >= 2:
        LocalValidator(sys.argv[1])  # python local_scrape.py /path/to/students/work
