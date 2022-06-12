def fun(starting_number,actual_step,steps,is_it_first_initation):
    if steps == 0:
        return 0
    else:
        result=[]
        temp=[]
        for i in starting_number:
            temp.append(i)
        temp.sort(reverse=True) # descending order
        if is_it_first_initation:
            print('step[',actual_step,']=: ', starting_number)
            is_it_first_initation = False
            actual_step+=1
        for i in temp:
                    if result: # list of results is not empty
                        if i < result[-1]:
                            num_of_appearance=temp.count(i)
                            result.append(str(num_of_appearance))
                            result.append(i)
                        else:
                            pass
                    else:
                        num_of_appearance = temp.count(i)
                        result.append(str(num_of_appearance))
                        result.append(i)
        next_step_str_result = ''
        for i in result:
            next_step_str_result+=str(i)
        print('step[', actual_step,']=: ', next_step_str_result)
        return fun(next_step_str_result,actual_step+1,steps-1,is_it_first_initation)


if __name__ == '__main__':

    try:
        number_to_make_fun=input("Enter an integer fun-number [1 - ]: ")
        number_to_make_fun=str(number_to_make_fun)
        num_of_steps=input("Enter number of steps [1 - ]: ")
        num_of_steps=int(num_of_steps)
        fun(number_to_make_fun,0,num_of_steps,True)
    except ValueError:
        print('Incorrect input data.')
