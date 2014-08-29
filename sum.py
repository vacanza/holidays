import holidays

ca = holidays.CA(years=[2013])
us = holidays.US(years=[2014])

t = ca + us

'2014-01-01' in t
