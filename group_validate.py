''' Import base modules, colors, and Scraper '''
import os
import sys
import time
from colors import bcolors
from local_validate import LocalValidator

'''
    Designed for use on the aggregation of CMS files output, not individual directories
'''

def group_validate(root_path, milestone):
    for dirname in os.listdir(root_path):
        if not dirname.startswith('.'):
            CMSdir = os.path.join(root_path, dirname)
            studentWorkDir = os.path.join(CMSdir, milestone + "-" + dirname)
            try:  
                # If you want to see the terminal output, switch the lines below
                # LocalValidator(studentWorkDir, True)
                
                # To hide terminal output
                LocalValidator(studentWorkDir)
            except:
                # handling edge case of a file in the CMS return 
                if os.path.isfile(CMSdir): 
                    print (bcolors.OKBLUE + "(Skipping this file)" + bcolors.ENDC)
                    continue

                # once here, this means that a CMS returned directory is empty (a non-submission) or the students
                # actual directory is named incorrectly ('submission' rather than 'p2m2-abc123')
                if not os.listdir(CMSdir):
                    print (bcolors.WARNING + "Empty directory: {}".format(CMSdir) + bcolors.ENDC)
                else:
                    print (bcolors.FAIL + "Misformatted directory:{} ".format(CMSdir) + bcolors.ENDC)

if __name__ == '__main__':
    if len (sys.argv) >= 2:
        group_validate(sys.argv[1], sys.argv[2]) 