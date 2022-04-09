# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# write your update damages function here:

def updated_damages(damage):
    new_damages = []
    for damage in damages:
        if damage == 'Damages not recorded':
            updated_damages.append(damage)
        elif damage[-1] == 'M':
            damage = (damage.replace('M', ''))
            updated_damages.append(float(damage) * 1000000)
        else:
            damage = (damage.replace('B', '')) 
            updated_damages.append(float(damage) * 1000000000)
    return new_damages


# write your construct hurricane dictionary function here:

new_list_damages = updated_damages()

def dic_hurricanes(names, months, years, max_sustained_winds, areas_affected, new_list_damages, deaths):
    hurricanes = {}
    counter = 0
    for name in names:
        hurricanes.update({name: {"Name": names[counter], "Month": months[counter], "Year": years[counter], "Max Sustained Wind": max_sustained_winds[counter], "Areas Affected": areas_affected[counter],"Damage": new_list_damages[counter], "Deaths": deaths[counter]}})
        counter +=1
    return hurricanes

# write your construct hurricane by year dictionary function here:

def dic_hurricanes_years(names, months, years, max_sustained_winds, areas_affected, updated_damagess, deaths):
    hurricanes_years = {}
    counter = 0
    for year in years:
        hurricanes_years.update({year: {"Name": names[counter], "Month": months[counter], "Year": years[counter], "Max Sustained Wind": max_sustained_winds[counter], "Areas Affected": areas_affected[counter],"Damage": updated_damagess[counter], "Deaths": deaths[counter]}})
        counter +=1
    return hurricanes_years





# write your count affected areas function here:


def count_affected(dictionary):
    count_dictionary = {}
    for list_a in dictionary:
        for area in list_a:
            if area not in count_dictionary:
                count_dictionary[area] = 1
            else:
                count_dictionary[area] += 1
    return count_dictionary




# write your find most affected area function here:


def most_damaged(dictionary):
    most_area = "Some Area"
    most_area_count = 0
    for key,value in dictionary.items():
            if value > most_area_count:
                most_area_count = value
                most_area = key
    return print(most_area + ": " + str(most_area_count))




# write your greatest number of deaths function here:

def most_lethal(hurricanes_dict):
    most_deaths = 0
    most_hurricane = "Some Hurricane"
    for hurricane in hurricanes_dict:
        if hurricanes_dict[hurricane]['Deaths'] > most_deaths:
            most_deaths = hurricanes_dict[hurricane]['Deaths']
            most_hurricane = hurricanes_dict[hurricane]['Deaths']
        return print("The most lethal hurricane was " + hurricane + " with " + str(most_deaths) + " deaths")





# write your catgeorize by mortality function here:


def mortality_scale(mortality):
    mortality_dict = {0 : [], 1 : [], 2: [], 3: [], 4: []}
    for hurricane in mortality:
        if mortality[hurricane]['Deaths'] == 0:
            mortality_dict[0].append(mortality[hurricane]['Name'])
        elif mortality[hurricane]['Deaths'] in range(1,100):
            mortality_dict[1].append(mortality[hurricane]['Name'])
        elif mortality[hurricane]['Deaths'] in range(101,500):
            mortality_dict[2].append(mortality[hurricane]['Name'])
        elif mortality[hurricane]['Deaths'] in range(501,1000):
            mortality_dict[3].append(mortality[hurricane]['Name'])
        elif mortality[hurricane]['Deaths'] > 1001:
            mortality_dict[4].append(mortality[hurricane]['Name'])
            
    return print(mortality_dict)




# write your greatest damage function here:

def most_damage(dictionary):
    most_dam_name = ""
    most_dam_value = 0
    for hurricane in dictionary:
        if dictionary[hurricane]['Damage'] == 'Damages not recorded':
            continue
        if dictionary[hurricane]['Damage'] > most_dam_value:
            most_dam_value = dictionary[hurricane]['Damage']
            most_dam_name = dictionary[hurricane]['Name']
    return print("The most destroying hurricane ever was " + most_dam_name + " with " + str(most_dam_value) + " deaths.")




# write your catgeorize by damage function here:

def damage_scale(dictionary):
    damage_dict = {0 : [], 1 : [], 2: [], 3: [], 4: []}
    for hurricane in dictionary:
        if dictionary[hurricane]['Damage'] == 0:
            damage_dict[0].append(dictionary[hurricane]['Name'])
        elif dictionary[hurricane]['Damage'] in range(1, 100000000):
            damage_dict[1].append(dictionary[hurricane]['Name'])
        elif dictionary[hurricane]['Damage'] in range(1, 1000000000):
            damage_dict[2].append(dictionary[hurricane]['Name'])
        elif dictionary[hurricane]['Damage'] in range(1, 10000000000):
            damage_dict[3].append(dictionary[hurricane]['Name'])
        elif dictionary[hurricane]['Damage'] > 10000000000:
            damage_dict[4].append(dictionary[hurricane]['Name'])
            
    return print(damage_dict)
