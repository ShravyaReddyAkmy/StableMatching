# Gale Shapley Algorithm implementation on stable matching marriage propblem
# Written by: Shravya Reddy AKmy
# Date: 09/29/2021

import random
import time
men_list=[] # Creating list to add all men
women_list=[] # Creating list to add all women
men_pref_list={} # Creating dictionary to add prefernce list of each man
women_pref_list={} # Creating dictionary to add prefernce list of each woman
match_formed=[] # Creating list to add pairs formed

# Function to create preference lists of men and women for given "n" 
def create_prefernce_list():
    n=int(input("\nEnter a value for number of men/women:"))
    for n in range (0,n):
        men_list.append('m'+str(n))
        women_list.append('w'+str(n))    
    for m in men_list:
        pref_list_m=[]
        pref_list_m=random.sample(women_list,len(women_list))
        men_pref_list[m]=pref_list_m
    for w in women_list:
        pref_list_w=[]
        pref_list_w=random.sample(men_list,len(men_list))
        women_pref_list[w]=pref_list_w
    return [men_list,women_list,men_pref_list,women_pref_list,n]

# Function to create stable matching using Gale-Shapley algorithm approach
def generate_stable_matching():
    men_waiting_list=men_list # Initializing List of men who are yet to propose
    print (men_waiting_list)
    while(len(men_waiting_list)>0):
        for man in men_waiting_list:
            for woman in men_pref_list[man]:
                match_taken = [pair for pair in match_formed if woman in pair]
                if (len(match_taken))==0:
                     match_formed.append([man,woman])
                     men_waiting_list.remove(man)
                     break
                elif (len(match_taken)>0):
                     current_partner = women_pref_list[woman].index(match_taken[0][0])
                     man_proposed = women_pref_list[woman].index(man)
                     if (man_proposed<current_partner):
                         men_waiting_list.remove(man)
                         men_waiting_list.append(match_taken[0][0])
                         match_taken[0][0]=man
                         break

# Funtion to check if there are any unstable pairs formed
def verify_stable_matching():
    for pair in match_formed:
        current_man=pair[0]
        current_woman=pair[1]
        current_man_rank=women_pref_list[current_woman].index(current_man)
        current_woman_pref_list=women_pref_list[current_woman]
        if current_man_rank>0:
                for man in current_woman_pref_list:
                    if (women_pref_list[current_woman].index(man)<current_man_rank):
                        man_preferences=men_pref_list[man]
                        man_pair=[pair for pair in match_formed if man in pair][0][1]
                        man_pair_rank=man_preferences.index(man_pair)
                        current_woman_rank=man_preferences.index(current_woman)
                        if man_pair_rank>current_woman_rank:
                            print ("Unstable pair:",man,current_woman)
                            return False   
                        else:
                            current_woman_pref_list.remove(man)
                            continue                            
        else:
                continue

# Main Funtion 
def main():
    random.seed(10)
    f=open("results-1b.txt","a")
    preference_list=create_prefernce_list()
    print("\nNumber of men/women:",preference_list[4],file=f)
    print("MEN=",preference_list[0])
    print("WOMEN=",preference_list[1])
    print("\nPreference lists of men:\n",preference_list[2],file=f)
    print("\nPreference lists of women:\n",preference_list[3],file=f)
    print("\nRunning Gale Shapley Algorithm for Men optimality")
    start=time.time()
    generate_stable_matching()
    end=time.time()
    total_time=(end-start)*1000
    print("\nFinal Stable Matching:",match_formed,file=f)
    print("Time taken to run Gale-shapley Algorithm in ms:",total_time,file=f)
    value=verify_stable_matching()
    if value==False:
        print("Unstable pairs found",file=f)
    else :
        print("Final matching is a Stable matching",file=f)
    print("***************************************************************",file=f)
    f.close()
main()
            










