import os
import sys
from colors import bcolors

"""
    This is used for generating a grading template from Kyle's markdown template and the CMS directory output of all the students 
    a grader needs to grade for that week. It generates a file with the netID of the student at the top, and the contents of the
    rubric for each student in 1 big file with a name of your choosing
"""

class createGradingPage():
    
    def __init__(self, root_path, file_template, grading_file_name):
        self.netIDs = []
        self.root = root_path
        self.file_template = file_template
        self.grading_file_full_path = os.path.join(self.root, grading_file_name)
        self.actual_grading_rubric = None

        self.setupWriteData(root_path)
        self.getNetIDS(self.root)
        self.generateGradingFile()
    
    # Splices the TA piece of the template from the student piece
    def setupWriteData(self, destination):
        template = open(self.file_template, "r")
        lines = template.readlines()
        # Find grading template within the entire template
        for index in range(len(lines)):
            if "====================8<----------------------" in lines[index]:
                self.actual_grading_rubric = lines[index+1:]
                return 

    # Get the netIDs for each of the graders students        
    def getNetIDS(self, root_path):
        for dir in os.listdir(root_path):
            self.netIDs.append(dir)
    
    # Actually writes the grading file 
    def generateGradingFile(self):
        print (bcolors.OKGREEN + "\nCreating grading file at: {}".format(self.grading_file_full_path) + bcolors.ENDC)

        final_template = open(self.grading_file_full_path, 'w+')
        for id in self.netIDs:
            final_template.write("<p> {} </p>\n".format(id))
            for line in self.actual_grading_rubric:
                final_template.write(line)
            final_template.write("\n\n\n")
        final_template.close()

if __name__ == "__main__":
    createGradingPage(sys.argv[1], sys.argv[2], sys.argv[3])

# python organize_grading.py <CMSdir> <kyles_template> <grading_response_name.html> 
# ex: python organize_grading.py /Users/gschultz49/Downloads/Submissions\ 2 /Users/gschultz49/Downloads/p2m2-grade-template.md  p2m2_response.html
        
    
