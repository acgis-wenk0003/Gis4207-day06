import arcpy

mxd = arcpy.mapping.MapDocument('MappingEx.mxd')

df = arcpy.mapping.ListDataFrames(mxd)


for frame in df:
    for layer in arcpy.mapping.ListLayers(frame):

        # Group layers
        if layer.isGroupLayer:
            for child in arcpy.mapping.ListLayers(layer):

                desc = arcpy.Describe(child)

                try:
                    if desc.shapeType == "Point":
                        layer.visible = True
                        child.visible = True
                        #print 'set {} group layer and {} layer to visible'.format(layer.name, child.name)

                except AttributeError:
                    pass #print "Error: {} does not have shapeType attribute".format(desc)

        # Regular layers
        else:
            try:
                if desc.shapeType == "Point":
                    layer.visible = True
                    #print 'set {} layer to visible'.format(layer.name)

            except AttributeError:
                pass #print "Error: {} does not have shapeType attribute".format(desc)





arcpy.RefreshTOC()
arcpy.RefreshActiveView()

del mxd