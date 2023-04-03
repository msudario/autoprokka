# Autoprokka is a script that runs prokka command line for each file in folder input. 

It gives as the locustag name as the first genus uppercase letter + the species name, save the file in a new folder named results_prokka in the same direcctory as the input.<p>
Simple run in your terminal: <code>python path/to/script.py</code>     with the options and go grab a coffe <p>
options:<p>
  -h, --help       show this help message and exit<p>
  -g , --genus     the genus of the species i.e: Dickeya<p>
  -i , --input     path to the fasta files i.e: <code>home/usr/Desktop/folder_with_your_files or ~/Desktop/folder_with_your_files</code>

Exemple of running it: <code>python ~/Desktop/scripts/autoprokka/autoprokka.py -g Klebsiella -i ~/Desktop/teste</code>
#
* In the case that the informations are not present in the fasta file it gives the name of the file as the locus tag
* Must run it in terminal/enviroment with prokka installed
