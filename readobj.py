#!/usr/bin/env python3

import sys

__author__ = 'Bhupendra Aole'
__version__ = '0.1.0'

class Obj3D:
    def __init__( self, filename ):
        self.vertices = []
        self.faces = []

        f = open( filename )
        line=f.readline()
        while line:
            line = line.strip()
            if len(line)>2:
                # vertices
                if line[:2]=='v ':
                    vec=[float(x) for x in line[2:].split()]
                    self.vertices.append( vec )
                
                # faces
                elif line[:2]=='f ':
                    cs = line[2:].split()
                    face = []
                    for i in cs:
                        c = i.split('/')
                        face.append( int( c[0] )-1 )
                    self.faces.append( face )
                    
            # read next line
            line=f.readline()

obj = Obj3D( 'testdata\cube.obj' )

print( 'Vertices:' )
for v in range( len( obj.vertices ) ):
    print( v, obj.vertices[v] )

print( '\nFaces:' )
for f in range( len( obj.faces ) ):
    print( str( f+1 ), obj.faces[f] )
    