import arcpy

mxd = arcpy.mapping.MapDocument("MappingEx.mxd")

mxd.title = 'arcpy.mapping module exercise'
mxd.author = 'Chris and Morgan'
mxd.credits = 'David Viljoen'
mxd.summary = 'Practice Python code'
mxd.tags = 'arcpy.mapping, python, gis4207'

try:
    mxd.save()
except Exception as e:
    print e.message
del mxd