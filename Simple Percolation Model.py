# Materials for the elements:

# Polymer Definition
model.Material(name='Polymer')
model.materials['Polymer'].Elastic(table=(2167, 0.33,)) # Young's Modulus (MPa) and Poisson's Ratio 

# Electrolyte Definition
model.Material(name='Electrolyte')
model.materials['Electrolyte'].Elastic(table=(0, 0,)) # Young's Modulus and Poisson's Ratio unsure what it would be for this polymer for Poisson's
model.materials['Electrolyte'].ElectricalConductivity(table=(.000435,),) # Linear Fickian Diffusion was assumed for the ionic conductivity ionic conductivity of the liquid electrolyte is 4.35 mS m−1