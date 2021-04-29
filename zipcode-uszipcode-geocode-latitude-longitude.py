# library for zipcodes
# for extensive list of zipcodes, set simple_zipcode =False
from uszipcode import SearchEngine

# instantiate search object using uszipcode.SearchEngine()
search = SearchEngine(simple_zipcode=True)



# create dict to store geocode by zipcode
di_zip_geo = {}

# create list to store zipcodes with no geocode
ls_zip_none = []

# =================================================================================
# this assumes unique list of zip codes, in this case stored as a set() object
# ... st_all_zipcode
# =================================================================================

print('Number of zip codes: ', len(st_all_zipcode))

for each_zipcode in st_all_zipcode:
    
    # use `search` object from uszipcode library
    zip_search = search.by_zipcode(each_zipcode)
    geocode = (zip_search.lat, zip_search.lng)
    
    # sometimes no geocode found for that zipcode
    if geocode == (None, None):
        # store zipcode w/o geocode in list
        ls_zip_none.append(each_zipcode)
    
    else: 
        # store geocode by zipcode in dictionary
        di_zip_geo[each_zipcode] = geocode
    
print('Number of zip codes with geocodes: ', len(di_zip_geo.keys()))
print('Number of zip codes without geocodes: ', len(ls_zip_none))
