# zipcode-uszipcode-geocode-latitude-longitude
Playbook to lookup geocode (latitude, longitude) by zipcode using uszipcode library

Install uszipcode library:
```
pip install uszipcode
```

Python code:
```python
# library for zipcodes
# for extensive list of zipcodes, set simple_zipcode =False
from uszipcode import SearchEngine

search = SearchEngine(simple_zipcode=True)

# use `search` object from uszipcode library
zip_search = search.by_zipcode('87144')
geocode = (zip_search.lat, zip_search.lng)
print(geocode)
```

### References: 
* Stackoverflow calculate distance, see uszipcode library. https://stackoverflow.com/questions/52292765/how-to-calculate-distance-between-two-zips
* Python uszipcode library. https://pypi.org/project/uszipcode/
