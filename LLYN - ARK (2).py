import bpy

# Gå gjennom alle materialer i scenen
for material in bpy.data.materials:
    print(material.name)
    
    
    
    
import ifcopenshell.util.pset
from ifcopenshell import util
pset_qto = util.pset.PsetQto("IFC4")
pset_qto.get_applicable_names("IfcMaterial")






import bpy
selectedObjects = bpy.context.selected_objects
for obj in selectedObjects:
    partDim = (str(obj.dimensions))
    print(obj.name + partDim)
    
    



import ifcopenshell.util.element

wall = model.by_type("IfcWall")[0]
wall_type = ifcopenshell.util.element.get_type(wall)

# Get all properties and quantities as a dictionary
# returns {"Pset_WallCommon": {"id": 123, "FireRating": "2HR", ...}}
psets = ifcopenshell.util.element.get_psets(wall_type)
print(psets)

# Get all properties and quantities of the wall, including inherited type properties
psets = ifcopenshell.util.element.get_psets(wall)
print(psets)

# Get only properties and not quantities
print(ifcopenshell.util.element.get_psets(wall, psets_only=True))

# Get only quantities and not properties
print(ifcopenshell.util.element.get_psets(wall, qtos_only=True))   
    


    
import bpy

# Hent objektet som representerer bygningen
bygning = bpy.context.object

# Hent volumet af bygningen
volum = bygning.dimensions.x * bygning.dimensions.y * bygning.dimensions.z

# Energieffektivitetsfaktor for oppvarming (f.eks. kWh/m³ per år)
energieffektivitet = 50

# Beregn estimert årlig oppvarmingsenergiforbrug
energiforbrug = volum * energieffektivitet

# Skriv resultatet
print(f"Estimert årlig oppvarmingsenergiforbrug: {energiforbrug} kWh per år")




import bpy

# Hent objektet som representerer bygningen
bygning = bpy.context.object

# Hent data om oppvarmingsbehov (f.eks. i watt per kvadratmeter)
oppvarmingsbehov_per_kvadratmeter = 40

# Hent bygningens areal
areal = bygning.dimensions.x * bygning.dimensions.y

# Beregn det årlige oppvarmingsforbruget
oppvarmingsforbrug = oppvarmingsbehov_per_kvadratmeter * areal * 365  # En forenklet beregning

# Skriv resultatet
print(f"Estimert årlig oppvarmingsforbrug: {oppvarmingsforbrug} wattimer (Wh)")
