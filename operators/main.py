# Do not modify these lines
__winc_id__ = 'd0d3cdcefbb54bc980f443c04ab3a9eb'
__human_name__ = 'operators'

# Add your code after this line

#The language spoken the most in Switzerland is the same as in Spain.
spain_dom_language = 'Castilian Spanish'
switzerland_dom_languague = 'German'
print (switzerland_dom_languague == spain_dom_language)

#The most prevalent religion in Switzerland is the same as in Spain.
spain_prev_religion = 'Roman Catholic'
switzerland_prev_religion = 'Roman Catholic'
print (switzerland_prev_religion ==wincpych spain_prev_religion)

#The name length of Spain's capital does not equal that of Switzerland.
spain_capital_namelenght = len ('Madrid)')
switzerland_capital_namelenght = len('Bern')
print(switzerland_capital_namelenght != spain_capital_namelenght)

#Switzerland's GDP is greater than Spain's GDP.
spain_GDP = 1778 * 1000
switzerland_GDP = 580
print (switzerland_GDP > spain_GDP)
#The population growth is less than 1% in Switzerland and Spain.
spain_pop_growth = 0.67
switzerland_pop_growth = 0.66
print(switzerland_pop_growth <1 and spain_pop_growth <1)

#At least one of the two countries has a population count of over 10 million.
spain_pop_count = 50
switzerland_pop_count = 8.4
print(switzerland_pop_count > 10 or spain_pop_count > 10 )

#Exactly one of the two countries has a population count of over 10 million.
print((switzerland_pop_count > 10 and spain_pop_count <= 10) or (switzerland_pop_count <= 10 and spain_pop_count > 10))