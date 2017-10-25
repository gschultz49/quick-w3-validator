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
    <pre> python main.py abs/path/to/CMS/downloads  abs/path/to/grading/template  grading_file/_name.ext </pre>
</p>
<p> indiviudual folder validation can be used in the form
    <pre> python main.py abs/path/to/individual/folder </pre>
</p>


# Warnings
<p>
    We DO NOT want to overload w3's validation servers, frequent use of these scripts in a short period of time (generally 150 requests in 2 hours) can lead to a 403 or request forbidden error. Use this tool sparingly and at your own risk.

</p>

# Other
<p>
    This script works on both macOS and windows 10, however, colorful terminal output only works on macOS and Linux.
</p>
