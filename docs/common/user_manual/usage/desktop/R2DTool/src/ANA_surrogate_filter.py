
def model_distributor(GI,SAM):


	if GI["NumberOfStories"]==1 and GI["StructureType"]=="W1":
		modelName ="SimGpModel"
	elif GI["NumberOfStories"]==2 and GI["StructureType"]=="W1":
		modelName ="SimGpModel2"
	else:
		modelName ="Default"
	return modelName
	