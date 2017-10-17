<h1>This tool is designed to quickly validate many student's directories for CS 1300, using the w3 validation service</h1>

# Installation
<p>
    You will need to install the Python requests library to use this.
    <pre>pip install requests</pre>
    (This project is written in Python 3.5.2)
</p>

# Usage  


<p>
    execution should be in this form:
    <pre> python main.py abs_path_to_CMS_downloads abs_path_to_grading_template grading_file_name </pre>
</p>


# Warnings
<p>
    We DO NOT want to overload w3's validation servers, frequent use of these scripts in a short period of time (generally 150 requests in 2 hours) can lead to a 403 or request forbidden error. Use this tool sparingly and at your own risk.
    <br><br>
    In some instances, student's do not zip a single folder, but an array of files. This will cause an error in the validator which requires <b>manual adjustments</b>. This occurs in the <b>group_directory_validate.py</b>

</p>

# Other
<p>
    This script works on both macOS and windows 10, however, colorful terminal output only works on macOS and Linux.
</p>
