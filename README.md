# autoprokka is a script that runs prokka for each file in folder input
it gives as the locustag name the first genus uppercase letter + first letter of species lowercase + the strain name, save the file in a new folder named results_prokka_strainname
simple run python path/to/script.py -h for the options and go grab a coffe
options:
  -h, --help       show this help message and exit
  -f , --format    Valid PROKKA format i.e: fasta, fna
  -o , --outdir    outdir i.e home/usr/Desktop
  -g , --genus     the genus of the species i.e: Dickeya
  -i , --input     path to the fasta files i.e: home/usr/Desktop/myfiles (do not finish with '/')
  [-s] , --species   species i.e: dadantii (it's not mandatory, particularry I do not recomment using species at all)
