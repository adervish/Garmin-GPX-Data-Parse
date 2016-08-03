#!/usr/bin/env python

import gpxpy.parser as parser
import csv
import sys

writer = csv.writer(sys.stdout)


gpx_file = open( 'activity_1284067099.gpx', 'r' )

gpx_parser = parser.GPXParser( gpx_file )
gpx = gpx_parser.parse()
gpx_file.close()

#print gpx.get_points_data()

result = []

#gpx = gpx_parser.get_gpx()

for track in gpx.tracks:
    first_ts = track.segments[0].points[0].time
    last_ts = first_ts
    first_pt = track.segments[0].points[0]
    last_pt = first_pt
    for segment in track.segments:
        for point in segment.points:
            diff =  point.time - last_ts
            diff_start = point.time - first_ts
            writer.writerow([diff.total_seconds() * 10, 
                diff_start.total_seconds() * 10, 
                first_pt.distance_2d(point), 
                last_pt.distance_2d(point)])
            last_ts = point.time
            last_pt = point
#            print 'Point at ({0},{1},{2}) -> {3}'.format( point.time, point.latitude, point.longitude, point.elevation )

#for waypoint in gpx.waypoints:
#    print 'waypoint {0} -> ({1},{2})'.format( waypoint.time, waypoint.name, waypoint.latitude, waypoint.longitude )

#for route in gpx.routes:
#    print 'Route:'
#    for point in route:
#        print 'Point at ({0},{1}) -> {2}'.format( point.latitude, point.longitude, point.elevation )
