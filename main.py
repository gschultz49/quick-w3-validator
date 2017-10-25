import os
import sys
from organize_grading import createGradingPage
from group_validate import group_directory_validate

''' This is the main runner for this whole project '''
def addQuotesToNames(arg):
    return ''+arg+''

if __name__ == "__main__":
    CMSdir = sys.argv[1] 
    Kyle_template = sys.argv[2]
    # this should be a .html file
    grading_file_name = sys.argv[3]
    
    createGradingPage(addQuotesToNames(CMSdir), addQuotesToNames(Kyle_template), addQuotesToNames(grading_file_name))
    group_directory_validate(CMSdir)
    # ex: python main.py /Users/gschultz49/Downloads/Submissions\ 2 /Users/gschultz49/Downloads/p2m2-grade-template.md  p2m2-response.html