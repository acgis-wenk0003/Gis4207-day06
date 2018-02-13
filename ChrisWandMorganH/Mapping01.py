import arcpy

mxd= arcpy.mapping.MapDocument('MappingEx.mxd')


values= ["arcpy.mapping module exercises",
        "Chris and Morgan",
        "David Viljoen made me do it",
        "See Description",
        "This document was used for practicing Python coding with the arcpy.mapping module.",
        "arcpy.mapping,python,gis4207"]

mxd.title=values[0]
mxd.author=values[1]
mxd.credits=values[2]
mxd.summary=values[3]
mxd.description=values[4]
mxd.tags=values[5]

try:
    mxd.save()
except Exception as e:
    print e.message

del mxd

