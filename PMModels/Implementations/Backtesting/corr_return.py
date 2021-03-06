# -*- coding: utf-8 -*-
#!/usr/bin/env python
'''
Name: Beier (Benjamin) Liu
Date: 7/5/2018

Remark:
Python 3.6 is recommended
Before running please install packages *numpy, scipy, matplotlib
Using cmd line py -3,6 -m pip install [package_name]
'''
import os, time, logging
import copy, math
import functools, itertools
import numpy as np
from Implementations.compute_mean import *
from Implementations.compute_var import *

'''===================================================================================================
File content:
provide optimization target function fitness_sharpe, like cost
==================================================================================================='''

def corr_return(R_1, R_2, method='spearman', freq='annually'):
	'''==============================================================================================
	Arguments:
	R_1 	-- list, past expected returns of strategy 1
	R_2 	-- list, past expected returns of strategy 2
	rf 	--	double, risk-free return rate

	Returns:
	res -- double, u=(mean-rf)/sqrt(var)
	=============================================================================================='''
	# Preparation Phrase
	res = 0.0;

	# Handling Phrase

	# Checking Phrase
	return res

