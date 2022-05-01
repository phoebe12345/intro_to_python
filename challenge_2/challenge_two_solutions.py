dictionary = {}
category_dictionary = {}
total_amount_spent = 0
place_holder_one = 0
counter = 0
days_dictionary = {}
with open("challengetwo.txt") as file:

    for line in file:
        
        items = line.split(",")
        amount = items[-1]
        amount = float(amount)
        total_amount_spent = total_amount_spent + amount
        amount = abs(amount)
       
        if amount < 50:
            counter = counter + 1

        place_spent = items[2]
        if place_spent not in dictionary:
            dictionary[place_spent] = 1
            
        elif place_spent in dictionary:
            dictionary[place_spent] = dictionary[place_spent] + 1
            
        maximum = 0
        max_key = None
        for place_spent in dictionary:
            if dictionary[place_spent] > maximum:
                maximum = dictionary[place_spent]
                max_key = place_spent

        category_spent = items[-3]
        if category_spent not in category_dictionary:
            category_dictionary[category_spent] = 1
        elif category_spent in category_dictionary:
            category_dictionary[category_spent] = category_dictionary[category_spent] + 1
        
        max = 0
        max_category_spent = None
        
        for category_spent in category_dictionary:
            if category_dictionary[category_spent] > max:
                max = category_dictionary[category_spent]
                max_category_spent = category_spent
        
        money_spent_days = items[0]
        money_spent_days = money_spent_days.split("/")
        money_spent_days = money_spent_days[1]
        money_spent_days = int(money_spent_days)
        
        if money_spent_days not in days_dictionary:
            days_dictionary[money_spent_days] = "true"
    
    print("total amount spent:", total_amount_spent)
    print("you did not spent money", 30 - len(days_dictionary), "days out of 30 days in April")
    print("this month,", counter, "transactions were under 50 dollars")
    print("you spent the most money on:", max_category_spent)
    print("you visited", max_key, maximum, "times this month")
    

           

        
        
        
        
