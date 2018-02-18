import arcpy

outfile=open('LayerVisibility.txt',"w")

mxd=arcpy.mapping.MapDocument("MappingEx.mxd")

for df in arcpy.mapping.ListDataFrames(mxd):

    for layer in arcpy.mapping.ListLayers(mxd,'',df):
        outfile.write(df.name+",")
        outfile.write("{}".format(layer))
        outfile.write("{}".format(","+str(layer.visible)+"\n"))

outfile.close()
del mxd
