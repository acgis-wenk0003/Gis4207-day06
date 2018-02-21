import arcpy

outtext = open(r'C:\acgis\GIS4207-GIS-Customization\day06\Lab06a\ChrisWandMorganH\LayerVisibility.txt','w')

mxd = arcpy.mapping.MapDocument('MappingEx.mxd')

df = arcpy.mapping.ListDataFrames(mxd)

text = ""
for i in df:
    for j in arcpy.mapping.ListLayers(i):
        text += str(i.name) + "\t" + str(j.name) + "\t" + str(j.visible) + "\n"
del mxd

outtext.write(str(text))
outtext.close()


