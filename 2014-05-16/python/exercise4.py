from larcc import *

def diagram2cell(diagram,master,cell):
   mat = diagram2cellMatrix(diagram)(master,cell)
   diagram =larApply(mat)(diagram)  
   
   """
   # yet to finish coding
   V, CV1, CV2, n12 = vertexSieve(master,diagram)
   masterBoundaryFaces = boundaryOfChain(CV,FV)([cell])
   diagramBoundaryFaces = lar2boundaryFaces(CV,FV)
   """
   V = master[0] + diagram[0]
   offset = len(master[0])
   CV = [c for k,c in enumerate(master[1]) if k != cell] + [
         [v+offset for v in c] for c in diagram[1]]
   master = V, CV
   return master