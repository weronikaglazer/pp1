import random

class Arrays():    
    @staticmethod    
    def print_in_col(array):        
        for c in array:            
            print(c) 

    @staticmethod 
    def print_in_row(array):
        new_array = [str(x) for x in array]
        print(",".join(new_array))

    @staticmethod
    def create_array(number,value):
        new_list = []
        for i in range(number):
            new_list.append(value)
        print(new_list)

    @staticmethod
    def create_array_random(number,min_value,max_value):
        new_list = []
        for i in range(number):
            new_list.append(random.randint(min_value,max_value))
        print(new_list)

    @staticmethod
    def count_elements(array,min_value,max_value):
        counter = 0
        for number in array:
            if (min_value <= number <= max_value):
                counter += 1

        print(counter)
            

Arrays.create_array(10,4)
test_array = Arrays.create_array_random(20,-7,8)
Arrays.count_elements(test_array,-1,1)


