''' Import base modules, colors, and Validator '''
import os
import sys
from colors import bcolors
from individual_validate import Individual_Validate

'''
    Designed for use on the aggregation of CMS directories output, not individual directories
'''

def group_directory_validate(root_path):
    for dirname in os.listdir(root_path):
        isEmpty = False
        if not dirname.startswith('.'):
            CMSdir = os.path.join(root_path, dirname)
            
            # edge case if theres a file in the CMS dir
            if os.path.isfile(CMSdir):
                print (bcolors.WARNING +"\nPassing over: {}".format(CMSdir)+ bcolors.ENDC)
                continue

            # If the directory is empty
            if not os.listdir(CMSdir):
                print (bcolors.OKBLUE+"\nEmpty directory:{}".format(CMSdir) + bcolors.ENDC)
                isEmpty = True
            
            # if there's actually content in the directory
            if not os.path.isfile(CMSdir):
                if isEmpty == False:
                    studentWork = os.path.join(CMSdir)
                    Individual_Validate(studentWork)
                       
if __name__ == '__main__':
    if len (sys.argv) >= 2:
        group_directory_validate(sys.argv[1]) 