

def dict_comp(stop,step):
    if stop > step:
        number_times_of_step_in_stop = stop//step
        length_of_element_in_stop_without_reminder = number_times_of_step_in_stop * step
        temp_list_of_item = [f'item-{i}' for i in range(1,(number_times_of_step_in_stop + 1))]
        
        

        value_list = list(range(1, (length_of_element_in_stop_without_reminder + 1)))
        
        list6 = [value_list[i:i+step] for i in range(0,len(value_list),step)]
        

        dict_comp1 = {key:value for (key,value) in zip(temp_list_of_item, list6)}
        print(dict_comp1)





dict_comp(10,2)



