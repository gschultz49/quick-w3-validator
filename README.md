<h1>This tool is designed to quickly validate many student's directories for CS 1300, using the w3 validation service</h1>

# Installation
<p>
    You will need to install the Python requests library to use this.
    <pre>pip install requests</pre>
    (This project is written in Python 3.5.2)
</p>

# Usage for TA's


<p>
    Execution should be in this form:
    <pre> python main.py abs/dir/path/to/GroupedCMS/downloads  abs/file/path/to/grading/template.md  grading_file_name.ext </pre>
    This execution will <br>
    1. Unzip all the student's directories from CMS <br>
    2. Validate all HTML and PHP files (given these files are in the root unzipped directory)<br>
    3. Generate a single grading file with the student's netID's and corresponding grading template in a single file of your name choice within the Grouped CMS download folder
</p>

# Usage for Students

<p> Indiviudual folders can also be validated
     <pre> python individual_validate.py abs/path/to/individual/folder </pre>
    Note, this assumes there is a zipped folder at the abs/path/to/individual/folder and will automatically unzip it. To avoid this behavior, change the unzip default parameter in the __main__ to *False* such that <pre> Individual_Validate(sys.argv[1])  --> Individual_Validate(sys.argv[1], unzip=False) </pre>
   
</p>


# Warnings
<p>
    We DO NOT want to overload w3's validation servers, frequent use of these scripts in a short period of time (generally 150 requests in 2 hours) can lead to a 403 or request forbidden error. Use this tool sparingly and at your own risk.

</p>

# Other
<p>
    This script works on both macOS and windows 10, however, colorful terminal output only works on macOS and Linux.
</p>
