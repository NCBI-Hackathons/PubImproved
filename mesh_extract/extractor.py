#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  9 11:09:25 2019

@author: nidhi rastogi
"""

import csv

    


with open('../data_ingestion/MeSH/output/mesh_labels_narrower_broader.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = '\n')
    term = []
    label = []
    narrower = []
    broader = []
    line_count = 0
    
    for column in csv_reader:
        if line_count == 0:
            print(f'Column names are {"[, .]".join(column)}')
           
            line_count += 1
        else:
            for row in column:
                if '|' in row:
                    lst = row.split("|")
                    stringcount = len(lst)
                    if stringcount == 4:
                        #print (row)
                        term.append(lst[0])
                        label.append(lst[1])
                        narrower.append(lst[2])
                        broader.append(lst[3])
                        #print(line_count, f'\t{term} {label} {narrower} {broader}')
            #print(column)
            line_count += 1
    print(f'Processed {line_count} lines.')