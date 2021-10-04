from helpers import get_countries

__winc_id__ = '25a8041d2d5e4e3ab61ab1be43bfb863'
__human_name__ = 'dictionaries'


countries = get_countries()

def create_pasport(name,date_of_birth,place_of_birth,height,nationality):
	pasport ={
		'name':name,
		'date_of_birth':date_of_birth,
		'place_of_birth':place_of_birth,
		'height':height,
		'nationality':nationality
	}
	return pasport

"""def add_stamp(pasport,countries):
	if('stamps' in pasport):
		#merge countries list
	else:
"""


print(create_pasport('Arif Nasrullah','09-09-1988','Suriname',1.76,'Dutch'))
