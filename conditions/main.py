# Do not modify these lines
__winc_id__ = '25596924dffe436da9034d43d0af6791'
__human_name__ = 'conditions'

# Add your code after this line
def farm_action(weather, time, milking_status, location_cows, season, slurry_tank, grass_status):
        if time == ('night' or weather == 'rainy') and location_cows == 'pasture':
            return 'take cows to cowshed'
        elif milking_status is True:
            if location_cows == 'pasture':
                return 'take cows to cowshed\nmilk cows\ntake cows back to pasture'
            elif location_cows == 'cowshed':
                 return 'milk cows'
        elif slurry_tank is True and (weather == 'rainy' or weather == 'neutral'):
            if location_cows == 'pasture':
                return 'take cows to cowshed\nfertilize\ntake cows back to pasture'
            elif location_cows == 'cowshed':
                return 'fertilize pasture'
        elif grass_status == True and season == 'spring' and weather == 'sunny':  
            if location_cows == 'pasture':  
                return 'take cows to cowshed\nmow grass\ntake cows back to pasture'
            elif location_cows == 'cowshed':
                return 'fertilize pasture'
        else:
            return 'wait'


print(farm_action('rainy', 'night', False, 'cowshed', 'winter', False, True))
