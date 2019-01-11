import pandas as pd
pd.set_option('display.width', 1000)
import os
os.chdir('/')

mapfile = '/users/nmtarr/documents/ranges/ybcu_circles'
title = 'Yellow-billed cuckoo occurrences from GBIF - any month'
mapfile2 = '/Users/nmtarr/Documents/RANGES/ybcu_circles'

def MapPolygonsFromSHP(map_these, title):
    """
    Displays shapefiles on a simple CONUS basemap.  Maps are plotted in the order
    provided so put the top map last in the listself.

    NOTE: The shapefiles have to be in WGS84 CRS.

    (list, str) -> displays maps, returns matplotlib.pyplot figure

    Arguments:
    map_these -- list of paths for shapefiles you want to display in CONUS.
    title -- title for the map.

    Example:
    >>MapPolygonsFromSHP(['/users/nmtarr/documents/ranges/ybcu_circles'],
                        'ybcu occurrences')
    """
    # Packages needed for plotting
    import matplotlib.pyplot as plt
    from mpl_toolkits.basemap import Basemap
    import numpy as np
    from matplotlib.patches import Polygon
    from matplotlib.collections import PatchCollection
    from matplotlib.patches import PathPatch

    # Basemap
    fig = plt.figure(figsize=(12,8))
    map = Basemap(projection='aea', resolution='c', lon_0=-95.5, lat_0=39.5,
                  height=3400000, width=5000000)
    map.drawcoastlines(color='grey')
    map.drawstates(color='grey')
    map.drawcountries(color='grey')
    map.fillcontinents(color='green',lake_color='aqua')
    map.drawmapboundary(fill_color='aqua')

    for mapfile in map_these:
        # Add shapefiles to the map
        map.readshapefile(mapfile, 'mapfile', drawbounds=True, linewidth=2)
        ## Code for extra formatting -- filling in polygons setting border color
        #patches = []
        #for info, shape in zip(map.mapfile_info, map.mapfile):
        #    patches.append(Polygon(np.array(shape), True))
        #ax.add_collection(PatchCollection(patches, facecolor= 'y', edgecolor='k',
        #                                  linewidths=.5, zorder=2))

    fig.suptitle(title, fontsize=20)
    fig.show()
    return fig

MapPolygonsFromSHP(map_these=[mapfile, mapfile2], title=title)
