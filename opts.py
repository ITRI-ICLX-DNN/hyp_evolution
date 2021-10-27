from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import argparse
import os
import numpy as np

class opts(object):
    def __init__(self):
        self.parser = argparse.ArgumentParser()

        # basic experiment setting
        self.parser.add_argument('--evolve',
                                 type=str,
                                 default='False', 
                                 help='generations to evolve')
        self.parser.add_argument('--hyp', 
                                 type=str, 
                                 default='./hyp.scratch.yaml',
                                 help='hyperparameters path')

        self.parser.add_argument('--number', 
                                 type=float, 
                                 default=1,
                                 help='')

		
		

    def parse(self, args=''):
        if args == '':
            opt = self.parser.parse_args()
        else:
            opt = self.parser.parse_args(args)

        
        return opt
