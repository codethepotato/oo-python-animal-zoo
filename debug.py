from lib.animal import *
from lib.zoo import *

# code here

# e.g.  
#   z1 = Zoo( 'Micke Grove Zoo', 'Lodi, CA' )
#   a1 = Animal( 'Lion', 75, 'Luke', z1 )

z1 = Zoo('Roosevelt Zoo', 'Minot, ND')
z2 = Zoo('Red River Zoo', 'Fargo, ND')

a1 = Animal('Lion', 88, 'Pepper', z1)
a2 = Animal('Cougar', 65, 'Zuko', z2)
a3 = Animal('Gorilla', 76, 'Gibby', z2)


# do not remove 
import ipdb; ipdb.set_trace()
