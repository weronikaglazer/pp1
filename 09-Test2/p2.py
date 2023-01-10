def f(human_age):
    dog_years = 0
    
    for i in range(1,human_age+1):
        if (i==1 or i==2):
            dog_years += 10
        else:
            dog_years += 4
    return dog_years


