# Geodesic

### Prerequisites

1. MATLAB R2014b+
2. Python 2.7+
3. FreeCAD 0.16

### Generating the CAD model for manufacturing

1. Run findPoints2.m
2. Run writer.py
3. Open plaindome30.FCStd in FreeCAD
4. Import the generated CSG file 606holes30_cone.csg into the same document
5. Make a cut of (3) - (4)
6. Export resulting shape (as STEP format, etc.)

### Generating C class model of holes

1. Run findPoints2.m
2. Run domeclassformatter.py
