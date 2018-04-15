capitals_dict = {
'Alabama' : 'Montgomery',
'Alaska' : 'Juneau',
'Arizona' : 'Phoenix',
'Arkansas' : 'Little Rock',
'California' : 'Sacramento',
'Colorado' : 'Denver',
'Connecticut' : 'Hartford',
'Delaware' : 'Dover',
'Florida' : 'Tallahassee',
'Georgia' : 'Atlanta',
'Hawaii' : 'Honolulu',
'Idaho' : 'Boise',
'Illinois' : 'Springfield',
'Indiana' : 'Indianapolis',
'Iowa' : 'Des',
'Kansas' : 'Topeka',
'Kentucky' : 'Frankfort',
'Louisiana' : 'Baton',
'Maine' : 'Augusta',
'Maryland' : 'Annapolis',
'Massachusetts' : 'Boston',
'Michigan' : 'Lansing',
'Minnesota' : 'Saint',
'Mississippi' : 'Jackson',
'Missouri' : 'Jefferson',
'Montana' : 'Helena',
'Nebraska' : 'Lincoln',
'Nevada' : 'Carson',
}

import random

for i in [1, 2, 3, 4, 5]:
    state = random.choice(capitals_dict.keys())
    capital = capitals_dict[capitals_dict.keys()]
    capital_guess = input("what is the capital of " + state + "? ")

    if capital_guess == capital:
        print("That\'s correct! Good Job!")
    else:
        print("Capital of " + state + " is: " + capital + ".")

print("All done.")
