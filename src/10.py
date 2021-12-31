from aoc import main
import re

INPUT = "position=< 20316, -30055> velocity=<-2,  3>\nposition=<-30043, -30055> velocity=< 3,  3>\nposition=<-19955,  40468> velocity=< 2, -4>\nposition=<-19981, -30055> velocity=< 2,  3>\nposition=< 30386,  30399> velocity=<-3, -3>\nposition=< 30417,  20320> velocity=<-3, -2>\nposition=<-40135, -50209> velocity=< 4,  5>\nposition=< 50586,  -9911> velocity=<-5,  1>\nposition=<-50222,  30399> velocity=< 5, -3>\nposition=<-40108,  30396> velocity=< 4, -3>\nposition=< -9931, -19980> velocity=< 1,  2>\nposition=< 10237, -40139> velocity=<-1,  4>\nposition=<-40106,  10242> velocity=< 4, -1>\nposition=<-30080, -30059> velocity=< 3,  3>\nposition=< -9913,  10249> velocity=< 1, -1>\nposition=< -9895, -30063> velocity=< 1,  3>\nposition=< 30401,  40468> velocity=<-3, -4>\nposition=< 50586,  -9911> velocity=<-5,  1>\nposition=< 30432,  -9912> velocity=<-3,  1>\nposition=<-50223,  50553> velocity=< 5, -5>\nposition=< 30406, -19983> velocity=<-3,  2>\nposition=< 10245, -30064> velocity=<-1,  3>\nposition=<-19956,  50544> velocity=< 2, -5>\nposition=<-40130,  -9903> velocity=< 4,  1>\nposition=<-50179,  20319> velocity=< 5, -2>\nposition=< 50529,  40475> velocity=<-5, -4>\nposition=< 10224,  20316> velocity=<-1, -2>\nposition=< 10269,  40470> velocity=<-1, -4>\nposition=<-50224,  10249> velocity=< 5, -1>\nposition=<-40111, -19985> velocity=< 4,  2>\nposition=< -9894,  40472> velocity=< 1, -4>\nposition=< 30399,  10240> velocity=<-3, -1>\nposition=<-40122, -19983> velocity=< 4,  2>\nposition=< 40489,  10241> velocity=<-4, -1>\nposition=< -9889,  -9903> velocity=< 1,  1>\nposition=< 10282, -30061> velocity=<-1,  3>\nposition=< 20331,  -9907> velocity=<-2,  1>\nposition=<-19967, -50208> velocity=< 2,  5>\nposition=<-30046, -40131> velocity=< 3,  4>\nposition=<-50179, -40139> velocity=< 5,  4>\nposition=< 20301,  20322> velocity=<-2, -2>\nposition=<-50230,  -9910> velocity=< 5,  1>\nposition=<-40133,  40473> velocity=< 4, -4>\nposition=<-19979, -19985> velocity=< 2,  2>\nposition=< 40476, -19984> velocity=<-4,  2>\nposition=< 20341,  50544> velocity=<-2, -5>\nposition=< -9894,  40471> velocity=< 1, -4>\nposition=< 20329,  30398> velocity=<-2, -3>\nposition=<-30075,  50548> velocity=< 3, -5>\nposition=< 50550,  30392> velocity=<-5, -3>\nposition=<-50230, -30061> velocity=< 5,  3>\nposition=< 40498, -40140> velocity=<-4,  4>\nposition=<-19949,  50548> velocity=< 2, -5>\nposition=<-30042, -19988> velocity=< 3,  2>\nposition=<-40140,  20325> velocity=< 4, -2>\nposition=< 30401,  50553> velocity=<-3, -5>\nposition=<-30040,  -9903> velocity=< 3,  1>\nposition=< 30393, -19979> velocity=<-3,  2>\nposition=< 50546, -30063> velocity=<-5,  3>\nposition=< 20331, -50216> velocity=<-2,  5>\nposition=<-30081,  10244> velocity=< 3, -1>\nposition=<-40132,  -9908> velocity=< 4,  1>\nposition=< 10233, -40140> velocity=<-1,  4>\nposition=<-40127, -30061> velocity=< 4,  3>\nposition=< 30405,  50549> velocity=<-3, -5>\nposition=< 30389,  -9909> velocity=<-3,  1>\nposition=< -9882, -19984> velocity=< 1,  2>\nposition=<-20007,  10245> velocity=< 2, -1>\nposition=< 20305,  30401> velocity=<-2, -3>\nposition=< 50529, -19988> velocity=<-5,  2>\nposition=<-19951, -19985> velocity=< 2,  2>\nposition=< 40489,  20321> velocity=<-4, -2>\nposition=< 30415, -19984> velocity=<-3,  2>\nposition=<-50223,  50544> velocity=< 5, -5>\nposition=< 20326, -19988> velocity=<-2,  2>\nposition=< 30413,  20318> velocity=<-3, -2>\nposition=< 10246,  30398> velocity=<-1, -3>\nposition=< 40470,  20317> velocity=<-4, -2>\nposition=< 50526,  50548> velocity=<-5, -5>\nposition=< 50560,  30392> velocity=<-5, -3>\nposition=<-40102, -40140> velocity=< 4,  4>\nposition=<-19964,  50553> velocity=< 2, -5>\nposition=<-30042,  10240> velocity=< 3, -1>\nposition=<-40115,  30396> velocity=< 4, -3>\nposition=< -9920, -19988> velocity=< 1,  2>\nposition=< -9874,  10244> velocity=< 1, -1>\nposition=< 10247,  30397> velocity=<-1, -3>\nposition=<-30075,  -9909> velocity=< 3,  1>\nposition=<-19954,  -9910> velocity=< 2,  1>\nposition=< 50577,  30392> velocity=<-5, -3>\nposition=< 20347,  20316> velocity=<-2, -2>\nposition=< -9875, -40136> velocity=< 1,  4>\nposition=< 50573,  50547> velocity=<-5, -5>\nposition=<-30074, -19984> velocity=< 3,  2>\nposition=< -9902,  50553> velocity=< 1, -5>\nposition=<-40151,  40469> velocity=< 4, -4>\nposition=< 50581, -30064> velocity=<-5,  3>\nposition=< 30378, -50214> velocity=<-3,  5>\nposition=<-30083,  20318> velocity=< 3, -2>\nposition=<-30059,  20323> velocity=< 3, -2>\nposition=<-30072, -40136> velocity=< 3,  4>\nposition=< 20341,  -9908> velocity=<-2,  1>\nposition=<-30035, -30059> velocity=< 3,  3>\nposition=< -9889, -40140> velocity=< 1,  4>\nposition=< -9930,  20320> velocity=< 1, -2>\nposition=< 50557,  -9907> velocity=<-5,  1>\nposition=< 30373,  40469> velocity=<-3, -4>\nposition=< -9875, -50208> velocity=< 1,  5>\nposition=< -9923,  20320> velocity=< 1, -2>\nposition=<-30080,  30392> velocity=< 3, -3>\nposition=< 30414,  40477> velocity=<-3, -4>\nposition=<-40149, -50207> velocity=< 4,  5>\nposition=<-40118, -30055> velocity=< 4,  3>\nposition=< -9918,  40474> velocity=< 1, -4>\nposition=< 40454, -40131> velocity=<-4,  4>\nposition=<-20007,  50549> velocity=< 2, -5>\nposition=<-50179, -30059> velocity=< 5,  3>\nposition=<-19980,  20325> velocity=< 2, -2>\nposition=<-50227,  -9911> velocity=< 5,  1>\nposition=< 20297, -50216> velocity=<-2,  5>\nposition=<-30081,  -9908> velocity=< 3,  1>\nposition=< 40497, -30062> velocity=<-4,  3>\nposition=<-20007,  30393> velocity=< 2, -3>\nposition=< -9918,  10246> velocity=< 1, -1>\nposition=< 20305,  40468> velocity=<-2, -4>\nposition=<-30055,  40468> velocity=< 3, -4>\nposition=<-40130,  40468> velocity=< 4, -4>\nposition=< 30434,  -9909> velocity=<-3,  1>\nposition=<-30033, -40136> velocity=< 3,  4>\nposition=< 20353, -50216> velocity=<-2,  5>\nposition=< 20302, -30063> velocity=<-2,  3>\nposition=< 10238, -40131> velocity=<-1,  4>\nposition=< 50562, -30058> velocity=<-5,  3>\nposition=< 30400,  40468> velocity=<-3, -4>\nposition=<-40146,  20319> velocity=< 4, -2>\nposition=< 20332,  -9907> velocity=<-2,  1>\nposition=< 10280, -30060> velocity=<-1,  3>\nposition=< 10231,  -9912> velocity=<-1,  1>\nposition=< 50541, -50213> velocity=<-5,  5>\nposition=< 40470,  40476> velocity=<-4, -4>\nposition=<-50190, -40131> velocity=< 5,  4>\nposition=< 30413, -19986> velocity=<-3,  2>\nposition=< 30433, -19988> velocity=<-3,  2>\nposition=< 40452, -50212> velocity=<-4,  5>\nposition=< 50557, -30058> velocity=<-5,  3>\nposition=< 10269,  50550> velocity=<-1, -5>\nposition=< 40494,  -9903> velocity=<-4,  1>\nposition=< 50545,  20325> velocity=<-5, -2>\nposition=< 40502,  40469> velocity=<-4, -4>\nposition=< 30373,  10243> velocity=<-3, -1>\nposition=<-30043, -40134> velocity=< 3,  4>\nposition=<-40149, -30060> velocity=< 4,  3>\nposition=<-40103,  10246> velocity=< 4, -1>\nposition=<-40122,  20321> velocity=< 4, -2>\nposition=< 10223, -19988> velocity=<-1,  2>\nposition=< 10261,  10249> velocity=<-1, -1>\nposition=< 10242,  20317> velocity=<-1, -2>\nposition=<-30074,  50548> velocity=< 3, -5>\nposition=< 10253,  -9903> velocity=<-1,  1>\nposition=< 40462,  -9907> velocity=<-4,  1>\nposition=<-50210, -40134> velocity=< 5,  4>\nposition=< -9913,  10240> velocity=< 1, -1>\nposition=<-30048,  30397> velocity=< 3, -3>\nposition=< -9872,  10244> velocity=< 1, -1>\nposition=<-40142,  10249> velocity=< 4, -1>\nposition=< 50562, -50209> velocity=<-5,  5>\nposition=<-40140, -40131> velocity=< 4,  4>\nposition=< 40492,  30392> velocity=<-4, -3>\nposition=< 50581,  10247> velocity=<-5, -1>\nposition=<-19983,  40476> velocity=< 2, -4>\nposition=<-50235,  40477> velocity=< 5, -4>\nposition=< 20321, -30064> velocity=<-2,  3>\nposition=< 30415,  40468> velocity=<-3, -4>\nposition=<-50193, -19984> velocity=< 5,  2>\nposition=< 30389, -19987> velocity=<-3,  2>\nposition=<-50227,  30393> velocity=< 5, -3>\nposition=< 30389,  50551> velocity=<-3, -5>\nposition=< 40506, -40136> velocity=<-4,  4>\nposition=<-40143, -30056> velocity=< 4,  3>\nposition=<-19947, -30064> velocity=< 2,  3>\nposition=< 40489,  30397> velocity=<-4, -3>\nposition=< 50533, -30059> velocity=<-5,  3>\nposition=< 30426, -40137> velocity=<-3,  4>\nposition=< 50538,  40473> velocity=<-5, -4>\nposition=<-30058,  50544> velocity=< 3, -5>\nposition=< 50557, -30062> velocity=<-5,  3>\nposition=< 50577,  30396> velocity=<-5, -3>\nposition=<-19975,  10249> velocity=< 2, -1>\nposition=< 40473,  30399> velocity=<-4, -3>\nposition=< 30410, -19986> velocity=<-3,  2>\nposition=< 10255,  20321> velocity=<-1, -2>\nposition=< 10229,  20321> velocity=<-1, -2>\nposition=<-50235,  20323> velocity=< 5, -2>\nposition=<-40151,  10242> velocity=< 4, -1>\nposition=< 20317,  30392> velocity=<-2, -3>\nposition=<-19999, -50209> velocity=< 2,  5>\nposition=<-50195, -19985> velocity=< 5,  2>\nposition=< -9922,  10249> velocity=< 1, -1>\nposition=< 40467, -50207> velocity=<-4,  5>\nposition=< 30406, -50211> velocity=<-3,  5>\nposition=< 10238,  30392> velocity=<-1, -3>\nposition=< 50537, -30060> velocity=<-5,  3>\nposition=<-30055,  20319> velocity=< 3, -2>\nposition=< 20302,  40469> velocity=<-2, -4>\nposition=< 50565,  50546> velocity=<-5, -5>\nposition=< 40449, -19984> velocity=<-4,  2>\nposition=< -9875,  20318> velocity=< 1, -2>\nposition=< -9931,  10245> velocity=< 1, -1>\nposition=< 50573, -19982> velocity=<-5,  2>\nposition=<-50198, -19980> velocity=< 5,  2>\nposition=<-40119,  40472> velocity=< 4, -4>\nposition=< 20330,  -9911> velocity=<-2,  1>\nposition=< 30423, -30064> velocity=<-3,  3>\nposition=<-40151, -50208> velocity=< 4,  5>\nposition=< 40505,  30400> velocity=<-4, -3>\nposition=< 10266, -50216> velocity=<-1,  5>\nposition=<-40150, -30064> velocity=< 4,  3>\nposition=< -9915,  20322> velocity=< 1, -2>\nposition=< 50534,  10249> velocity=<-5, -1>\nposition=< -9923,  -9905> velocity=< 1,  1>\nposition=< 50581,  20323> velocity=<-5, -2>\nposition=<-40151,  30395> velocity=< 4, -3>\nposition=< -9906,  20322> velocity=< 1, -2>\nposition=<-40146,  50545> velocity=< 4, -5>\nposition=<-19974,  10245> velocity=< 2, -1>\nposition=<-30075, -40137> velocity=< 3,  4>\nposition=<-50185,  -9912> velocity=< 5,  1>\nposition=< -9899,  50552> velocity=< 1, -5>\nposition=< 30393, -19988> velocity=<-3,  2>\nposition=<-19970,  40472> velocity=< 2, -4>\nposition=< 50574,  -9908> velocity=<-5,  1>\nposition=<-20003,  40474> velocity=< 2, -4>\nposition=< 40492,  -9903> velocity=<-4,  1>\nposition=< -9891,  30392> velocity=< 1, -3>\nposition=< 20329,  -9905> velocity=<-2,  1>\nposition=< 30422, -30064> velocity=<-3,  3>\nposition=< 30402, -30063> velocity=<-3,  3>\nposition=< 50565,  20320> velocity=<-5, -2>\nposition=< 50551,  30397> velocity=<-5, -3>\nposition=< 50581,  30393> velocity=<-5, -3>\nposition=< -9883, -40137> velocity=< 1,  4>\nposition=<-20002, -19980> velocity=< 2,  2>\nposition=< 20316, -50216> velocity=<-2,  5>\nposition=< 10258, -40131> velocity=<-1,  4>\nposition=< 30429,  30397> velocity=<-3, -3>\nposition=< 30424, -30064> velocity=<-3,  3>\nposition=< 40505,  20325> velocity=<-4, -2>\nposition=< 40457, -40131> velocity=<-4,  4>\nposition=< 40497,  40472> velocity=<-4, -4>\nposition=< 20322,  40477> velocity=<-2, -4>\nposition=< -9929, -19988> velocity=< 1,  2>\nposition=< 20310, -30061> velocity=<-2,  3>\nposition=< -9871, -50216> velocity=< 1,  5>\nposition=<-30043,  10244> velocity=< 3, -1>\nposition=< 40505,  -9909> velocity=<-4,  1>\nposition=< 20345, -50209> velocity=<-2,  5>\nposition=< 10237,  30398> velocity=<-1, -3>\nposition=<-30058,  50553> velocity=< 3, -5>\nposition=<-40123, -50211> velocity=< 4,  5>\nposition=<-40150,  50553> velocity=< 4, -5>\nposition=< 10226,  20317> velocity=<-1, -2>\nposition=< 10269,  -9912> velocity=<-1,  1>\nposition=< 20340, -19988> velocity=<-2,  2>\nposition=<-50222,  40476> velocity=< 5, -4>\nposition=< -9883, -40140> velocity=< 1,  4>\nposition=< 50575, -40136> velocity=<-5,  4>\nposition=<-19972, -30064> velocity=< 2,  3>\nposition=<-40125, -30064> velocity=< 4,  3>\nposition=<-40151, -19982> velocity=< 4,  2>\nposition=< 30434, -30062> velocity=<-3,  3>\nposition=<-30042,  -9912> velocity=< 3,  1>\nposition=< 40465,  20324> velocity=<-4, -2>\nposition=< 30429,  30400> velocity=<-3, -3>\nposition=< 10229,  10245> velocity=<-1, -1>\nposition=< 20301, -19981> velocity=<-2,  2>\nposition=< 20331,  10240> velocity=<-2, -1>\nposition=<-30079,  30396> velocity=< 3, -3>\nposition=<-50191,  20325> velocity=< 5, -2>\nposition=<-50215,  40468> velocity=< 5, -4>\nposition=<-30046, -50208> velocity=< 3,  5>\nposition=< 30421,  40470> velocity=<-3, -4>\nposition=< -9931,  50550> velocity=< 1, -5>\nposition=<-19997,  20320> velocity=< 2, -2>\nposition=< 50573, -19983> velocity=<-5,  2>\nposition=<-50219, -40138> velocity=< 5,  4>\nposition=< 20358,  50545> velocity=<-2, -5>\nposition=< 50558,  -9911> velocity=<-5,  1>\nposition=< 40449, -50208> velocity=<-4,  5>\nposition=<-30082, -40140> velocity=< 3,  4>\nposition=<-40135, -30055> velocity=< 4,  3>\nposition=<-20007,  20323> velocity=< 2, -2>\nposition=<-19979,  -9903> velocity=< 2,  1>\nposition=< 50533, -50209> velocity=<-5,  5>\nposition=< -9915, -40139> velocity=< 1,  4>\nposition=< 10270, -19984> velocity=<-1,  2>\nposition=< 20353,  50546> velocity=<-2, -5>\nposition=<-19957,  -9908> velocity=< 2,  1>\nposition=< 30377, -30064> velocity=<-3,  3>\nposition=<-30075, -40140> velocity=< 3,  4>\nposition=< 40483,  40473> velocity=<-4, -4>\nposition=< 20300, -40135> velocity=<-2,  4>\nposition=< 40481,  30396> velocity=<-4, -3>\nposition=< 10234,  40470> velocity=<-1, -4>\nposition=< -9883, -50215> velocity=< 1,  5>\nposition=< 50568,  10244> velocity=<-5, -1>\nposition=< 40492,  20316> velocity=<-4, -2>\nposition=<-19994, -30062> velocity=< 2,  3>\nposition=<-50214,  10248> velocity=< 5, -1>\nposition=< -9923,  -9908> velocity=< 1,  1>\nposition=<-19951, -40134> velocity=< 2,  4>\nposition=< 10245,  20325> velocity=<-1, -2>\nposition=< 30415, -40131> velocity=<-3,  4>\nposition=< 20357,  10244> velocity=<-2, -1>\nposition=< 20337,  20323> velocity=<-2, -2>\nposition=< 10226, -40137> velocity=<-1,  4>\nposition=<-19990,  20325> velocity=< 2, -2>\nposition=<-40127, -50207> velocity=< 4,  5>\nposition=< 10221,  10240> velocity=<-1, -1>\nposition=< 40461,  -9908> velocity=<-4,  1>\nposition=< 30373, -30055> velocity=<-3,  3>\nposition=<-50219, -40135> velocity=< 5,  4>\nposition=< 10269,  20320> velocity=<-1, -2>\nposition=<-40159, -30057> velocity=< 4,  3>\nposition=<-40102,  30392> velocity=< 4, -3>\nposition=< 50525,  10241> velocity=<-5, -1>\nposition=<-50227, -30056> velocity=< 5,  3>\nposition=<-50191,  -9903> velocity=< 5,  1>\nposition=<-50194,  10244> velocity=< 5, -1>\nposition=< 40476,  50544> velocity=<-4, -5>\nposition=<-50187, -30056> velocity=< 5,  3>\nposition=< 30429, -40134> velocity=<-3,  4>\nposition=<-20002,  -9910> velocity=< 2,  1>\nposition=<-19994,  30395> velocity=< 2, -3>\nposition=<-40122,  -9908> velocity=< 4,  1>\nposition=<-30043,  50545> velocity=< 3, -5>\nposition=< 10221, -30062> velocity=<-1,  3>\nposition=< 30426,  40469> velocity=<-3, -4>\nposition=<-19999,  20325> velocity=< 2, -2>\nposition=< 30389,  40472> velocity=<-3, -4>\nposition=<-50187, -30055> velocity=< 5,  3>\nposition=<-30070,  50549> velocity=< 3, -5>\nposition=< 50537,  50553> velocity=<-5, -5>\nposition=<-30035,  20325> velocity=< 3, -2>\nposition=<-30056,  10249> velocity=< 3, -1>\nposition=< 30421,  -9912> velocity=<-3,  1>\nposition=<-19991, -50210> velocity=< 2,  5>\nposition=< 40507, -19988> velocity=<-4,  2>\nposition=< 50527,  30396> velocity=<-5, -3>\nposition=< -9928,  -9912> velocity=< 1,  1>\nposition=< -9883, -50211> velocity=< 1,  5>\nposition=< 40452, -40135> velocity=<-4,  4>\nposition=<-30035,  20325> velocity=< 3, -2>\nposition=< 30386,  -9906> velocity=<-3,  1>\nposition=<-40130,  40470> velocity=< 4, -4>\nposition=< 40449,  20325> velocity=<-4, -2>\nposition=< 20353,  40477> velocity=<-2, -4>\nposition=<-50179,  50544> velocity=< 5, -5>\nposition=< 50582,  10240> velocity=<-5, -1>\nposition=<-40106,  40469> velocity=< 4, -4>\nposition=<-30082,  40468> velocity=< 3, -4>\nposition=< 10237,  30395> velocity=<-1, -3>\nposition=< 30410,  50553> velocity=<-3, -5>"

def print_grid(stars: list[list[int]]) -> bool:
  ymin, ymax = min(s[1] for s in stars), max(s[1] for s in stars)
  if ymax-ymin > 15:
    return False
  xmin, xmax = min(s[0] for s in stars), max(s[0] for s in stars)
  for y in range(ymin,ymax+1):
    row = ""
    for x in range(xmin,xmax+1):
      if any(s[0]==x and s[1]==y for s in stars):
        row += '█'
      else:
        row += ' '
    print(row)
  return True

def solve() -> tuple[str,int]:
  stars = [[int(i) for i in re.findall("-?\d+", l)] for l in INPUT.split('\n')]
  for steps in range(1000000):
    for s in stars:
      s[0] += s[2]
      s[1] += s[3]
    steps += 1
    if print_grid(stars):
      return "RBCZAEPP", steps
  assert False

main(solve)
