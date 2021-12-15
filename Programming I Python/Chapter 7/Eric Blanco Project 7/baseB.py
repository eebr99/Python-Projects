#this is the module that holds functions necessary to analyze baseball data
#inside the functions, convert the data to ints

def bat_avg(List, index):
   return format(int(List[index][3]) / int(List[index][1]), '.3f')

def onBase(List, index):
   hit = int(List[index][3])
   BB = int(List[index][8])
   HBP = int(List[index][10])
   AB = int(List[index][1])
   SF = int(List[index][11])
   return format((hit + BB + HBP) / (AB + BB + HBP + SF), '.3f')
   
def slug(List, index):
   double = int(List[index][4])
   triple = int(List[index][5])
   HR = int(List[index][6])
   single = int(List[index][3]) - (double + triple + HR)
   AB = int(List[index][1])
   return format((single + 2*double + 3*triple + 4*HR) / AB, '.3f')

def OPS(on_base, slugging):
   return format((float(on_base) + float(slugging)), '.3f')

def runs_prod(List, index):
   RBI = int(List[index][7])
   runs = int(List[index][2])
   HR = int(List[index][6])
   return str((RBI + runs) - HR)

def runs_per_plate(List, index):
   RBI = int(List[index][7])
   runs = int(List[index][2])
   HR = int(List[index][6])
   BB = int(List[index][8])
   HBP = int(List[index][10])
   AB = int(List[index][1])
   SF = int(List[index][11])
   return format(((RBI + runs) - HR) / (AB + BB + HBP + SF), '.3f')

