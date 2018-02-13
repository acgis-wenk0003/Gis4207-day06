import arcpy

outfile=open('SaveLayerVis_output.txt',"w")

mxd=arcpy.mapping.MapDocument("MappingEx.mxd")

for df in arcpy.mapping.ListDataFrames(mxd):
    outfile.write(df.name+"\n")
    for layer in arcpy.mapping.ListLayers(mxd,'',df):
        outfile.write("{}".format(layer))
        outfile.write("{}".format(", "+str(layer.visible)+"\n"))

outfile.close()
del mxd
