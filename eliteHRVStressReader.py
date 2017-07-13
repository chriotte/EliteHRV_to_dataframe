#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 29 16:07:20 2017

@author: christopher
"""
import importhrv as imp
path = 'data/eliteHRV/export/'
df = imp.importDriveData(path, "*.txt")

df.reset_index().plot(x="time", y=['interval in seconds'])
