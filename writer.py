import csv

# f = open('606holes40_cone.csg', 'wb')
f = open('606holes30_cone.csg', 'wb')
f.write("""
// CSG file generated from FreeCAD 0.16.6704 (Git)
union() {
""")
with open('mats.csv', 'rb') as csvfile:
  spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
  for row in spamreader:
    rr=[float(x) for x in row]
    # rr[3]*=2./3.
    # rr[7]*=2./3.
    # rr[11]*=2./3.
    # print ', '.join(row)
    # print [float(x) for x in row]

    # # Cylindrical holes best for CNC
    # f.write("""
# multmatrix([[%lf, %lf, %lf, %lf], [%lf, %lf, %lf, %lf], [%lf, %lf, %lf, %lf], [0,0,0,1]]){
# cylinder($fn = 0, $fa = 12.000000, $fs = 2.000000, h = 14.0, r1 = 3.0, r2 = 3.0, center = false);
# }
# """ % tuple(float(x) for x in rr))
    # ratio = rr[11] / 194.6666667
    ratio = 0 if rr[11] < 7.5 else 1  # use 10 instead of 7.5 for 40cm dome
    # r1 = ratio*2.025 + (1-ratio)*2.25  # use 2.7 instead of 2.025 for 40cm dome
    # r2 = ratio*4.905 + (1-ratio)*2.25  # use 5.4 instead of 4.905 for 40cm dome
    r1 = ratio*2 + (1-ratio)*2.25  # use 2.7 instead of 2 for 40cm dome
    r2 = ratio*5 + (1-ratio)*2.25  # use 5.4 instead of 5 for 40cm dome
    # print r1
    # print r2
    # If 3D printing, we can go with conical holes
    f.write("""
multmatrix([[%lf, %lf, %lf, %lf], [%lf, %lf, %lf, %lf], [%lf, %lf, %lf, %lf], [0,0,0,1]]){
cylinder($fn = 0, $fa = 12.000000, $fs = 2.000000, h = 10.0, r1 = %lf, r2 = %lf, center = false);
}
""" % tuple([float(x) for x in rr] + [r1, r2]))

f.write("""
}
""")