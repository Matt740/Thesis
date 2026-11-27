from abaqus import *
from abaqusConstants import *
import regionToolset
import mesh
import job

# 1. Initializing Model
model = mdb.Model('PercModel')


# 2. Generating Unpercolated Mesh

# Want to generate a mesh of elements that is a prism of hexahedral elements

Lx = 4 * 10^-4
Ly = 4 * 10^-4
Lz = 4 * 10^-4

h = .1 * 10^-6

nelemx = round(Lx/h)
nelemy = round(Ly/h)
nelemz = round(Lz/h)

Real_Lx = h * nelemx
Real_Ly = h * nelemy
Real_Lz = h * nelemz

# Create rectangular prism
sketch = model.ConstrainedSketch(
    name='BlockSketch',
    sheetSize=100.0
)

sketch.rectangle(
    point1=(0.0, 0.0),
    point2=(Lx, Ly)
)

part = model.Part(
    name='Block',
    dimensionality=THREE_D,
    type=DEFORMABLE_BODY
)

part.BaseSolidExtrude(
    sketch=sketch,
    depth=Lz
)

del model.sketches['BlockSketch']

# Assign hexahedral element type
elemType = mesh.ElemType(
    elemCode=C3D8,
    elemLibrary=STANDARD
)

part.setElementType(
    regions=(part.cells,),
    elemTypes=(elemType,)
)

# Seed the edges
part.seedPart(
    size=min(Lx/n, Ly/n, Lz/n),
    deviationFactor=0.1,
    minSizeFactor=0.1
)

# Generate mesh
part.generateMesh()

# Create assembly instance
assembly = model.rootAssembly
assembly.Instance(
    name='Block-1',
    part=part,
    dependent=ON
)

# Save model
mdb.saveAs(pathName='HexMesh.cae')




# 3. Material definition:

# Polymer Definition
model.Material(name='Polymer')
model.materials['Polymer'].Elastic(table=(2167, 0.33,)) # Young's Modulus (MPa) and Poisson's Ratio 

# Electrolyte Definition
model.Material(name='Electrolyte')
model.materials['Electrolyte'].Elastic(table=(0, 0,)) # Young's Modulus and Poisson's Ratio unsure what it would be for this polymer for Poisson's
model.materials['Electrolyte'].ElectricalConductivity(table=(.000435,),) # Linear Fickian Diffusion was assumed for the ionic conductivity ionic conductivity of the liquid electrolyte is 4.35 mS m−1

