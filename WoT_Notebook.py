print("WoT Notebook 1.0")

nations = ('U.S.S.R.', 'Germany', 'U.S.A.', 'U.K.', 'France', 'Czehoslovkia', 'China', 'Japan') #Creating corteges
types = ('Light_Tanks', 'Medium_Tanks', 'Heavy_Tanks', 'Tank_Destroyers', 'SPGs')
USSR_L = ('MS-1','BT-2')
USSR_M = ('A-32','T-28')
USSR_H = ('KV-1S','IS')
USSR_D = ('AT-1','SU-76M')
USSR_S = ('SU-18','SU-26')
USSR = { 'Light_Tanks' : USSR_L, 'Medium_Tanks' : USSR_M, 'Heavy_Tanks' : USSR_H, 'Tank_Destroyers' : USSR_D,'SPGs' : USSR_S}
USSR_list = USSR.keys()
USSR_list = list(USSR_list)
USSR_list.sort()
USSR_list[0], USSR_list[1] = USSR_list[1], USSR_list[0]
USSR_list[1], USSR_list[2] = USSR_list[2], USSR_list[1]
USSR_list[3], USSR_list[4] = USSR_list[4], USSR_list[3]
MS1 = ('Cost - 0', 'Hit Points - 100', 'Hull armor - 16/16/16', 'Turret armor - 16/16/16', 'Damage - 30/30/36', 'Penetration - 34/44/19')


def input_num():	#Parsing input
	while True:
		result = input()
		try:
			num = int(result)
			break
		except ValueError:
			print("Incorrect number")
	return num
	
	
def show_USSR_tank():
    while True:
        print('Tank:',end=' ')
        res = input()
        if res == "MS-1":
            for item in MS1:
                print(item)
        elif res == "exit":
            break

def choose_nat():
    print("\nEnter:")
    while True:
        res = input()
        if res == "U.S.S.R.":
            for type in USSR_list:
                print(type,'-',USSR[type])
            show_USSR_tank()
            break
		#elif res == "Germany"
		#elif res == "U.S.A."
		#elif res == "U.K."
		#elif res == "France"
		#elif res == "Czehoslovkia"
		#elif res == "China"
		#elif res == "Japan"
        elif res == "exit":
            break
        else:
            print("Incorrect input") 
			
			
def show_nat():
    for nat in nations:
        print(nat, end=' ')
    while True:
        print("\n1)Choose nation\n2)Return")
        choose = input_num()
        if choose == 1:
            choose_nat()
            #break
        elif choose == 2:
            break
			
		
def show_types():
	for type in types:
		print(type, end='   ')
	
	
while True:   #Main
	print("\n1)Show all nations\n2)Show all types\n3)Searching tank\n4)Exit")
	choose = input_num()
	if choose == 1:
		show_nat()
	elif choose == 2:
		show_types()
	#if choose == 3:
			
	elif choose == 4:
	    exit()
	else:
		print("Incorrect input")