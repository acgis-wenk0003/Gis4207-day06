import arcpy

mxd=arcpy.mapping.MapDocument("CURRENT")

df=arcpy.mapping.ListDataFrames(mxd, "world")
mxd.activeView=df[0]