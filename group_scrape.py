''' Import base modules '''
import os
import sys
import time
from local_scrape import LocalScraper
from colors import bcolors

'''
    Designed for use on the aggregation of CMS files output, not individual directories
'''

def group_validate(root_path, milestone):
    for dirname in os.listdir(root_path):
        if not dirname.startswith('.'):
            CMSdir = os.path.join(root_path, dirname)
            studentWorkDir = os.path.join(CMSdir, milestone + "-" + dirname)
            try:  
                LocalScraper(studentWorkDir)
            except:
                print (bcolors.WARNING + "Directory empty or misformatted :( " + bcolors.ENDC)


if __name__ == '__main__':
    if len (sys.argv) >= 2:
        group_validate(sys.argv[1], "p2m2")  # python local_scrape.py /path/to/CMS/students/directories
        # ex: python group_scrape.py /Users/gschultz49/Desktop/CornellDrive/Junior\ Year/INFO1300TA/p2m2