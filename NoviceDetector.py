import sys
import os
import pandas as pd
import numpy as np

class NoviceDetector(object):
	
	def __init__(self, tbt_datafilename):
		self.tbt_datafilename=tbt_datafilename
		
	def load_data(self, verbose=False):
		self.__data__=pd.read_csv(self.tbt_datafilename, names=range(42))
		self.__nrows__, self.__ncols__=self.__data__.shape
		self.__data__=self.__data__.values.tolist()
	def begin_inspection(self, verbose=False):
		for i in range(self.__nrows__):
			if self.__data__[i][4]=='T':
				if self.__data__[i][5]=='B':
					self.__excID__=self.__data__[i][40]
					tick='B'
				else:
					self.__excID__=self.__data__[i][41]
					tick='S'
				self.__currtimestamp__=self.__data__[i][1]
				j=1
				while(i-j>0):
					if(self.__data__[i-j][40]==self.__excID__ and self.__data__[i-j][5]==tick and self.__data__[i-j][4]!='T'):
						if self.__data__[i-j][4]=='M' and self.__data__[i-j][26]-self__data__[i-j][28]==0:
							print '%s,%s,%s,%s,%s'%(self.__currtimestamp__, self.__data__[i-j][1])
					j=j+1
			
def main():
	filename=sys.argv[1]
	Novice=NoviceDetector(filename)
	Novice.load_data()
	Novice.begin_inspection()

if __name__=='__main__':
	main()
						
		
