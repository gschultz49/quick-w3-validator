<h1>This tool is designed to quickly validate many student's directories for CS 1300, using the w3 validation API</h1>

# Installation
<p>
    You will need to install the Python requests library to use this.
    <pre>pip install requests</pre>
    (This project is written in Python 3.5.2)
</p>

# Usage  
<p>
    This project can be ran in 2 ways. 
    <br><br>
    To validate .html files in a single directory, at the root of the directory such that (to validate one.html, two.html)
</p>
<pre>
        root_dir
        |
        |-- one.html
        |
        |-- two.html
        |
        |-- images (other directories...)
        |   |--photo1.jpg
        
</pre>
<p>
    To run the validator on an individual directory:
    <br>
    <pre>python indivdual_validate.py /absolute/path/to/students/dir</pre>
    <br>
    You can choose to show the JSON output per file by passing a 'True' to the displayOutput in the Individual_Validate instantiation 
</p>
<p>
    To run the validator on all the directories outputted from CMS, run
    <pre>python group_directory_validate.py /absolute/path/to/CMS/dir</pre>
    <br>
    By default, this unzips the directory, then validates it.

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
