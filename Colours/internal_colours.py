# Internal Janome colour code to various thread codes.

order = (
  "Janome",
  "Madeira Rayon",
  "Robison-Anton Rayon",
  "Sulky Rayon",
  "Brother Embroidery",
  "Robison-Anton Polyester",
  "Isacord Polyester"
  )

groups = {
  "Brother Embroidery": {
    0x01: 900,
    0x02: 1,
    0x06: 515,
    0x08: 612,
    0x10: 843,
    0x15: 804,
    0x29: 614,
    0x2e: 808,
    0x35: 348,
    0x3f: 86,
    0x2d: 330,
    0x34: 337,
    0x45: 328,
    0x48: 126,
  },
  "Isacord Polyester": {
    0x01: 20,
    0x02: 15,
    0x06: 5513,
    0x08: 2830,
    0x10: 761,
    0x15: 3652,
    0x27: 2504,
    0x29: 2910,
    0x2d: 6133,
    0x2e: 5944,
    0x34: 1312,
    0x35: 832,
    0x3c: 3900,
    0x3f: 2520,
    0x45: 546,
    0x48: 811,
  },
  "Janome": {
    0x01: 2,
    0x02: 1,
    0x03: 239,
    0x06: 226,  # also 269
    0x07: 232,
    0x09: 201,
    0x0a: 202,
    0x0b: 236,
    0x0d: 3,
    0x0e: 2,
    0x11: 211,
    0x15: 209,  # also 228
    0x19: 227,
    0x1a: 207,  # also 230
    0x1b: 229,
    0x1e: 232,
    0x21: 202,
    0x24: 238,
    0x26: 211,
    0x2a: 225,
    0x2c: 246,
    0x2d: 246,
    0x2e: 226,  # also 248
    0x2f: 249,
    0x33: 253,
    0x34: 235,
    0x35: 238,
    0x47: 273,
    0x48: 274,
    0x4e: 224,
  },
  "Madeira Rayon": {
    0x01: 1000,
    0x02: 1001,
    0x03: 1024,
    0x04: 1278,
    0x05: 1393,
    0x06: 1170,
    0x08: 1032,
    0x0a: 1037,
    0x0b: 1126,
    0x0c: 1242,
    0x0d: 1025,
    0x0e: 1043,
    0x0f: 1330, # 1011
    0x10: 1084,
    0x12: 1020,
    0x13: 1105,
    0x14: 1181,
    0x15: 1232, # also 1132
    0x17: 1001,
    0x18: 1360,
    0x1a: 1028,
    0x1c: 1375,
    0x1f: 1315,
    0x20: 1165,
    0x21: 1037,
    0x22: 1272,
    0x23: 1105,
    0x25: 1068,
    0x26: 1232, # also 1116
    0x27: 1188,
    0x28: 1383,
    0x29: 1334,
    0x2a: 1147,
    0x2b: 1086,
    0x2c: 1106,
    0x2d: 1194,
    0x2e: 1370,
    0x31: 1185,
    0x32: 1396,
    0x34: 1221,
    0x35: 1255,
    0x36: 1136,
    0x37: 1192,
    0x38: 1385,
    0x3a: 1000,
    0x3b: 1360,
    0x3c: 1134,
    0x3d: 1029,
    0x3e: 1049,
    0x3f: 1354,
    0x40: 1309,
    0x41: 1181,
    0x42: 1156,
    0x43: 1249, # 1101
    0x44: 1270,
    0x45: 1065, # 1196
    0x46: 1025,
    0x48: 1155,
    0x49: 1248,
    0x4a: 1146,
    0x4b: 1250,
    0x4c: 1335,
    0x4d: 1138,
    0x4e: 1055,
  },
  "Robison-Anton Polyester": {
    0x01: 5596,
    0x0f: 5586,
    0x20: 5769,
    0x27: 5800,
    0x3c: 5684,
    0x42: 5802,
    0x43: 5508,
    0x4a: 5536,
  },
  "Robison-Anton Rayon": {
    0x16: 2321,
    0x1d: 2529,
    0x42: 2572,
  },
  "Sulky Rayon": {
    0x01: 1005,
    0x02: 1001,
    0x03: 1024,
    0x06: 1051,
    0x07: 1289,
    0x08: 1032,
    0x0a: 1037,
    0x0c: 1042,
    0x0e: 1005,
    0x10: 1127,
    0x12: 1259,
    0x15: 1193,
    0x1a: 1143,
    0x1c: 1201,
    0x27: 1192,
    0x29: 1255,
    0x2d: 1156,
    0x2e: 1174,
    0x34: 1181,
    0x35: 1055,
    0x3b: 2125,
    0x3c: 1042,
    0x3d: 1134,
    0x3e: 1279,
    0x3f: 1511,
    0x42: 1179,
    0x45: 1227,
    0x48: 1238,
  },
}

def convert_to_csv(path):

    import csv
    
    f = open(path, "w")
    w = csv.writer(f)
    w.writerow(("Internal",) + order)
    
    rows = map(lambda x: [x], range(0x50))
    
    for group in order:
    
        colours = groups[group]
        for row in rows:
    
            i = row[0]
            colour = colours.get(i, "")
            row.append(colour)
    
    for row in rows:
        w.writerow(row)
    
    f.close()
