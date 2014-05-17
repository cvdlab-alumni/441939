from larcc import *

def multipleDiagram2cell(diagram,master,toRemove,toMerges):
	V,CV = diagram
	# Remove specified cells in toRemove from diagram first
	diagram = V,[cell for k,cell in enumerate(CV) if not (k in toRemove)]
	# Insert diagram all the cells indicated in toMerges
	toMerges = list(sort(toMerges)) # Sorting is required to avoid random renumbering of cells
	for i in xrange(len(toMerges)):
		master = diagram2cell(diagram,master,toMerges[i]-i)
	return master