from larcc import *

def diagram2cell(diagram,master,cell):
   mat = diagram2cellMatrix(diagram)(master,cell)
   diagram =larApply(mat)(diagram)
   
   V1,CV1 = master
   # Remove the cell specified from master
   CV1 = [c for k,c in enumerate(CV1) if k != cell]
   # Combine vertices and cells
   V,CV1,CV2,n12 = vertexSieve((V1,CV1),diagram)

   return V, CV1+CV2