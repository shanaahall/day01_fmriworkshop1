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

def main():
    #load in all the global variables prepro needs, rightnow this is just the path to the data
    basedir='/Users/shanahall/Desktop/fMRI_Workshop/Data_task'
    prepro(basedir)
    
main()