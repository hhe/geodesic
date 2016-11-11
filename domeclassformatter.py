import csv, math

unique_holes = []
reflected_holes = []
retroreflectors = []
barcode = []

def stringify(array):
  strarray = []
  for i in xrange(len(array)):
    strarray += [('\n__' if i%3==0 else '') + '{%.5ff, %.5ff, %.5ff}' % array[i]]
  return ','.join(strarray).replace(' ','').replace('_',' ').replace('0000f','f').replace('00f','f').replace('0f','f')

with open('606Holes_highp.csv', 'rb') as csvfile:
  reader = csv.reader(csvfile)
  for row in reader:
    vec = tuple(float(i) for i in row)
    if abs(vec[0]*vec[0]+vec[2]*vec[2] - 0.519795722186) < 1e-5:
      barcode += [vec]
    elif abs(vec[2]) < 1e-10:
      if abs(vec[0]) < 0.185:
        retroreflectors += [vec]
      else:
        unique_holes += [vec]
    elif vec[2] > 0:
      reflected_holes += [vec]

retroreflectors = sorted(retroreflectors, lambda a, b: 1 if a[0] > b[0] else -1)
barcode = sorted(barcode, lambda a, b: 1 if math.atan2(a[2], a[0]) > math.atan2(b[2], b[0]) else -1)

open('DomeModel.h','w').write("""#pragma once
#include "DataTypes.h"

static const int NUM_DOME_HOLES = 598;
static const int NUM_DOME_RETROREFLECTORS = 3;
static const int NUM_DOME_BARCODE_DOTS = 5;

static const float domeRetroreflectors[3][3] = {%s
};

// TODO! manually sort by theta, lol. It's going to be wrong when generated.
static const float domeBarcodeDots[5][3] = {%s
};

static const float domeHolesUnique[18][3] = {%s
};

static const float domeHolesReflected[290][3] = {%s
};

inline Vector3f GetDomeHole(int index) {
  if (index < 580) {
    const float* vec = domeHolesReflected[index %% 290];
    return Vector3f(vec[0], vec[1], index < 290 ? -vec[2] : vec[2]);
  }
  return Vector3f(domeHolesUnique[index - 580]);
}

inline Vector3f GetDomeRetroreflector(int index) {
  return Vector3f(domeRetroreflectors[index]);
}

inline Vector3f GetDomeBarcodeDot(int index) {
  return Vector3f(domeBarcodeDots[index]);
}

// Warning:
// this function should be updated if the order inside domeRetroreflectors is changed
inline Vector3f GetDomeCenter() {
  return Vector3f(domeRetroreflectors[1]);
}
""" % (
  stringify(retroreflectors),
  stringify(barcode),
  stringify(unique_holes),
  stringify(reflected_holes),
))

# with open('606HolesScaled - Copy.txt', 'rb') as fin:
  # y = fin.readlines()
  #yy = [r for r in y if re.search('-[\d\.]+f},$', r) is None and re.search(',0.f},$', r) is not None]
  # print len(yy)
  # i = 0
  # for row in yy:
    # i += 1
    # f.write(row)
    # if i%3==0:
      # f.write('\n');


# f = open('DomeModel.cpp', 'wb')
# f.write("""
# // CSG file generated from FreeCAD 0.16.6704 (Git)
# union() {
# """)
# with open('606HolesScaled - Copy.txt', 'rb') as fin:
  # y = fin.readlines()
  # yy = [r for r in y if re.search('-[\d\.]+f},$', r) is None and re.search(',0.f},$', r) is not None]
  # print len(yy)
  # i = 0
  # for row in yy:
    # i += 1
    # f.write(row)
    # if i%3==0:
      # f.write('\n');

# f.write("""
# }
# """)
