import arcpy

mxd = arcpy.mapping.MapDocument("MappingEx.mxd")

mxd.title = 'arcpy.mapping module exercise'
mxd.author = 'Chris and Morgan'
mxd.credits = 'David Viljoen'
mxd.summary = 'Practice Python code'
mxd.tags = 'arcpy.mapping, python, gis4207'

mxd.saveACopy(r"C:\acgis\GIS4207-GIS-Customization\day06\lab06\MapEx2.mxd")

del mxd