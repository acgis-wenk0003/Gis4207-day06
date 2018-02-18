import arcpy

mxd=arcpy.mapping.MapDocument("CURRENT")
infile=open("LayerVisibility.txt")
txtlayers=[]

for line in infile:
        split=line.strip('\n').split(',')
        txtlayers.append(split)
for df in arcpy.mapping.ListDataFrames(mxd):
    for layer in arcpy.mapping.ListLayers(mxd,'',df):
        for txtlayer in txtlayers:
            if layer.name==txtlayer[1]:
                if layer.visible!=txtlayer[2]:
                    layer.visible=txtlayer[2]
                else:
                    continue
            else:
                continue
infile.close()
del mxd
arcpy.RefreshActiveView()
arcpy.RefreshTOC()