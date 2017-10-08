import os
import sys

class createGradingPage():
    def __init__(self, root_path, file_template, grading_file_name):
        self.setupWriteData(root_path, file_template, grading_file_name)

    def setupWriteData(self,destination, file_template, grading_file_name):
        template = open(file_template, "r")
        lines = template.readlines()
        # Find grading template within the entire template
        for index in range(len(lines)):
            if "================================8<----------------------------------" in lines[index]:
                gradingResponse = lines[index+1:]
                break
        
        netIDs = self.getNetIDS(destination)
        # print (gradingResponse)
        self.generateGradingFile(destination, netIDs, gradingResponse, grading_file_name)
    

    # Get the netIDs for each of the graders students        
    def getNetIDS(self, root_path):
        netIDs=[]
        for dir in os.listdir(root_path):
            netIDs.append(dir)
        return netIDs
    
    # actually writes the grading file 
    def generateGradingFile(self,destination, netIDs, grading_template, grading_file_name):
        file = open(os.path.join(destination, grading_file_name), 'w+')
        for id in netIDs:
            file.write("<p> {} </p>\n".format(id))
            for line in grading_template:
                file.write(line)
            file.write("\n\n\n")
        file.close()

if __name__ == "__main__":
    createGradingPage(sys.argv[1], sys.argv[2], sys.argv[3])

# python organize_grading.py <CMSdir> <kyles_template> <grading_response_name.html> 
# ex: python organize_grading.py /Users/gschultz49/Downloads/Submissions\ 2 /Users/gschultz49/Downloads/p2m2-grade-template.md  p2m2_response.html
        
    
