''' Import base modules, colors, and Scraper '''
import os
import sys
import time
from colors import bcolors
from local_scrape import LocalValidator

'''
    Designed for use on the aggregation of CMS files output, not individual directories
'''

def group_validate(root_path, milestone):
    for dirname in os.listdir(root_path):
        if not dirname.startswith('.'):
            CMSdir = os.path.join(root_path, dirname)
            studentWorkDir = os.path.join(CMSdir, milestone + "-" + dirname)
            try:  
                LocalValidator(studentWorkDir)
            except:
                print (bcolors.WARNING + "Directory empty or misformatted :( " + bcolors.ENDC)


if __name__ == '__main__':
    if len (sys.argv) >= 2:
        group_validate(sys.argv[1], sys.argv[2]) 