#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 10:55:57 2017

@author: shanahall
"""

import glob
import os
import shutil


def prepro(basedir):
    print('Data in the path '+basedir)





input=glob.glob('/Users/shanahall/Desktop/fMRI_Workshop/Data/sub-*/func/sub-*bart*.nii.gz')
#glob is twice because glob #1 is the module and glob #2 is the function
#glob produces a list, meaning you can put anything in there. 
print(input[0:10])

x=i'''nput[1]
print('my path is '+x)
y=x.split('/')
sub=y[6]'''

#or more nicely


#for i,x in enumerate(input):  
    #print i,x
    #sub=[]
sub=int(input[0].split('/')[6].split('-')[1])
    #path=os.path.join(basedir,'sub-*','func','sub-*.nii.gz')
    
def prepro(basedir):
    for item in glob.glob(os.path.join(basedir,'sub-*','func','sub-*bart*')):
        output_path=item.strip('.nii.gz')
        #output_path=item.split('.')[0]
        output=output_path+('_brain')
        print output
        os.system('bet %s %s -F'%(item,output))
        #pdb.set_trace()

def main():
    #load in all the global variables prepro needs, rightnow this is just the path to the data
    basedir='/Users/shanahall/Desktop/fMRI_Workshop/Data'
    prepro(basedir)
    
main()