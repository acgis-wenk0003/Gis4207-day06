import arcpy

mxd=arcpy.mapping.MapDocument("CURRENT")

df= arcpy.mapping.ListDataFrames(mxd,"Canada")[0]

for layer in arcpy.mapping.ListLayers(mxd,"",df):
    if layer.name=="Continents" or layer.name== "World Cities":
        arcpy.mapping.RemoveLayer(df,layer)

del mxd
arcpy.RefreshActiveView()
arcpy.RefreshTOC()