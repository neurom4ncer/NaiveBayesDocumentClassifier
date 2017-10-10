#Elizabeth E. Esterly & Danny Byrd
#visualizations.py
#last updated 10/04/2017
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

####confusionMatrix########
# takes a dataframe and prints to a text file
# m ::: a 2-d array (matrix)
def confusionMatrix(df):
	np.savetxt('confusion.txt', df.values, fmt='%d')
	return

####betaAccuracyEvaluation##########
# betaVal ::: adjust weight of prior and evaluate performance
def betaAccuracyEvaluation(betaVal):
	accuracy = None
	return accuracy

###plotBetaAccuracies######
# betas  :::  a list of beta values to be evaluated
def plotBetaAccuracies(betas):
	accuracies = []
	for b in betas:
		accuracies.append(betaAccuracyEvaluation(b))
	plt.plot(betas, accuracies)
	plt.savefig("leTest.jpg")
	plt.show()

