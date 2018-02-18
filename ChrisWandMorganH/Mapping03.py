import arcpy

mxd= arcpy.mapping.MapDocument("MappingEx.mxd")
print "DataFrame\t Scale\t Extent"
for df in arcpy.mapping.ListDataFrames(mxd):
    print "{}\t {}\t {}, {},  {}, {}".format(df.name, df.scale, df.extent.XMin, df.extent.XMax, df.extent.YMin, df.extent.YMax)

del mxd

