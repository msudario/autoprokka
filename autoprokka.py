#!/usr/bin/env python3
# coding: utf-8

import os
import subprocess
import argparse


parser = argparse.ArgumentParser(
    description='running autoPROKKA')


parser.add_argument('-g', '--genus', metavar='', type=str, required=True,
                    help='the genus of the species i.e: Dickeya')
parser.add_argument('-i', '--input', metavar='', type=str, required=True,
                    help='path to the files i.e: home/usr/Desktop/myfiles')



args = parser.parse_args()

folder_input = os.path.expanduser(f'{args.input}') 
genus = f'{args.genus}'

extensoes = ['.fna', '.faa', '.fasta']

def run_prokka(folder_input): 
    os.chdir(folder_input)

    caminho_nova_pasta = os.path.join(folder_input, 'results_autoprokka')

    for arquivos in os.listdir(folder_input):
        for extensao in extensoes:
            if arquivos.endswith(extensao): 
                with open(os.path.join(folder_input, arquivos), "r") as file:
                    first_line = file.readline().split()
                    if 'coverage' in first_line:
                            locus_tag = arquivos.replace(">","").replace("(", "").replace(")", "").replace(";","").replace(",","").replace("/","").replace("|","").replace("\\","").replace("[","").replace("]","").replace('.','').replace('-', '').replace('fasta', '').replace('fna', '').replace('faa', '')
                            print(f"could not find the {arquivos} species/strain's names, changed to file's name")
                            strain = locus_tag
                            command_line = ['prokka', '--outdir', os.path.join(caminho_nova_pasta, f'{strain}'), '--genus',
                            f'{genus}', '--prefix', f'{locus_tag}', '--locustag', f'{locus_tag}', f'{arquivos}']
                            
                            subprocess.call(command_line)
                            
                    elif first_line[5] == 'chromosome' or first_line[5] == 'contig' or first_line[5] == 'complete':
                            locus_tag = first_line[1][0] + first_line[2]
                            strain = first_line[4].replace(">","").replace("(", "").replace(")", "").replace(";","").replace(",","").replace("/","").replace("|","").replace("\\","").replace("[","").replace("]","").replace('.','').replace('-', '').replace('fasta', '').replace('fna', '').replace('faa', '')
                            command_line = ['prokka', '--outdir', os.path.join(caminho_nova_pasta, f'{strain}'), '--genus',
                            f'{genus}', '--prefix', f'{locus_tag}', '--locustag', f'{locus_tag}', f'{arquivos}']
        
                            subprocess.call(command_line)
                    else: 
                            locus_tag = first_line[1][0] + first_line[2]
                            strain = arquivos.replace(">","").replace("(", "").replace(")", "").replace(";","").replace(",","").replace("/","").replace("|","").replace("\\","").replace("[","").replace("]","").replace('.','').replace('-', '').replace('fasta', '').replace('fna', '').replace('faa', '')
                            command_line = ['prokka', '--outdir', os.path.join(caminho_nova_pasta, f'{strain}'), '--genus',
                            f'{genus}', '--prefix', f'{locus_tag}', '--locustag', f'{locus_tag}', f'{arquivos}']
        
                            subprocess.call(command_line)
      

def make_dir(folder_input) :
    os.chdir(folder_input)

    if 'results_autoprokka' not in os.listdir():
        os.mkdir('results_autoprokka')  
    else: 
        print('Error - results_autoprokka already exists') 
        return 

    
def process_files(folder_input):
    make_dir(folder_input)
    run_prokka(folder_input)

if __name__ == '__main__':
    process_files(folder_input)
