<h1>This tool is designed to quickly validate many student's directories for CS 1300.</h1>

# Installation
<p>
    You will need to install the Python requests library to use this.
    `pip install requests`
    (This project is written in Python 3.5.2)
</p>

# Usage  
<p>
    This project can be ran in 2 ways. 
    <br>
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
    You need to run 
    <br>
    `python local_validate.py /absolute/path/to/students/dir`
    <br>
    You can choose to show the JSON output per file by passing a 'True' to the LocalValidator class instantiation.  

</p>

# Warnings
<p>
    We DO NOT want to overload w3's validation servers, frequent use of these scripts in a short period of time (generally 150 requests in 2 hours) can lead to a 403 or request forbidden error. Use this tool sparingly and at your own risk.
</p>

# Other
<p>
    This script works on both macOS and windows 10, however, colorful terminal output only works on macOS
</p>
