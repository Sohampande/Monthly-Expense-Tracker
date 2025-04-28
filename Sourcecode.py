import random
import pymysql
import matplotlib.pyplot as plt
import statistics as stat
connection = pymysql.connect(host="localhost",database="mep",cursorclass=pymysql.cursors.DictCursor)
mycur=connection.cursor()



#Basic Info for the sql table, 
def user_basic_info():
    global name_user, Nas, DOB, Age
    name_useR = input("please enter your full Name:")
    DOB = input("please enter your date of birth: ")
    Age = input("please enter your age: ")
    name_user = name_useR.strip()

#primary key for user,
def primary_key_for_user():
       Nas = name_user.split(" ")
       nas2 = []
       special_characters = ["!","@","#","$","%","&","*","^","€","‡","°","±"]
       nas2.append(random.choice(Nas))
       nas2.append(random.choice(special_characters))
       nas2.append(Age)
       Userid = "".join(nas2)
       return Userid 
    
#function for making a new user's values. 
def user_basic(x):


    salary=float(input("Please enter your monthly salary :"))
    
    car_insure=float(input("Please enter your monthly car insurance :"))
    med_insure=float(input("Please enter your monthly medical insurance cost :"))
    life_insure=float(input("Please enter your montly life insurance cost : "))
    
    insurance= sum([car_insure,med_insure,life_insure])
    
    utility=float(input("Please enter your monthly utility cost :"))
    rent=float(input("Please enter your monthly rent :"))
    
    Personal_Upkeep=float(input("Enter your Personal Upkeep cost:"))
    Subscriptions=float(input("Enter your Subscriptions cost:"))
    Entertainment=float(input("Enter your Entertainment cost:"))
    Groceries=float(input("Enter your Groceries cost:"))
    basic=(x,name_user,DOB,Age,salary,insurance,utility,rent,Personal_Upkeep,Subscriptions,Entertainment,Groceries)
    basic_query="INSERT INTO central (userid,Name,Dob,Age,Salary,Insurances,Utility,Rent,Personal_Upkeep,Subscriptions,Entertainment,Groceries) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
    mycur.execute(basic_query,basic)
    connection.commit()

#function for menu
def menu():
    c = 1
    print('Welcome to the program',name_user)
    print('''What would you like to do today ? 
                          1. Changing older values 
                          2. Viewing older values
                          3. Quit ''')
    x = int(input("Please enter your choice :"))
    while c == 1:
        if x not in [1,2,3]:
             print("incorrect value")
             x = int(input("please enter the appropriate choice :"))
             if x not in [1,2,3]:
                 print("please enter the correct value ")
                 x = int(input("please enter the correct choice :"))
                 c = 1
        if x in [1,2,3]:
            c = 0
    return x 

#fuction for changing the values
def change_val(x):
    c = 1
    while c == 1:
        print('''The existing columns are : 
                          1. Dob
                          2. Age
                          3. Salary
                          4. Insurances
                          5. Utility
                          6. Rent
                          7. Personal Upkeep
                          8. Subscriptions
                          9. Entertainment
                          10.Groceries''')
        
        col = int(input("Please enter the number of the column you want to change : "))
        
        if col == 1:
            val = input("please enter the value of dob you need to change to(YYYY-MM-DD): ")
            insert_query = "update central set dob = %s where userid = %s;"
            basic = (val,userid)
            mycur.execute(insert_query, basic)
            connection.commit()
            print("DOB is changed to", val)
            print()
        elif col == 2:
            val = int(input("please enter the value of age you need to change to: "))
            insert_query = "update central set age = %s where userid = %s;"
            basic = (val,userid)
            mycur.execute(insert_query, basic)
            connection.commit()
            print("Age is changed to", val)
        elif col == 3:
            val = int(input("please enter the value of salary you need to change to: "))
            insert_query = "update central set salary = %s where userid = %s;"
            basic = (val,userid)
            mycur.execute(insert_query, basic)
            connection.commit()
            print("salary is changed to", val)
        elif col == 4:
            val = int(input("please enter the value of insurances you need to change to: "))
            insert_query = "update central set Insurances = %s where userid = %s;"
            basic = (val,userid)
            mycur.execute(insert_query, basic)
            connection.commit()
            print("insurances is changed to", val)
        elif col == 5:
            val = int(input("please enter the value of utility you need to change to: "))
            insert_query = "update central set Utility = %s where userid = %s;"
            basic = (val,userid)
            mycur.execute(insert_query, basic)
            connection.commit()
            print("utility is changed to", val)
        elif col == 6:
            val = int(input("please enter the value of rent you need to change to: "))
            insert_query = "update central set Rent = %s where userid = %s;"
            basic = (val,userid)
            mycur.execute(insert_query, basic)
            connection.commit()
            print("rent is changed to", val)
        elif col == 7:
            val = int(input("please enter the value of personal upkeep you need to change to: "))
            insert_query = "update central set Personal_Upkeep = %s where userid = %s;"
            basic = (val,userid)
            mycur.execute(insert_query, basic)
            connection.commit()
            print("personal upkeep is changed to", val)
        elif col == 8:
            val = int(input("please enter the value of subscriptions you need to change to: "))
            insert_query = "update central set subscriptions = %s where userid = %s;"
            basic = (val,userid)
            mycur.execute(insert_query, basic)
            connection.commit()
            print("subscriptions is changed to", val)
        elif col == 9:
            val = int(input("please enter the value of entertainment you need to change to: "))
            insert_query = "update central set Entertainment = %s where userid = %s;"
            basic = (val,userid)
            mycur.execute(insert_query, basic)
            connection.commit()
            print("entertainment is changed to", val)
        elif col == 10:
            val = int(input("please enter the value of Groceries you need to change to: "))
            insert_query = "update central set Groceries = %s where userid = %s;"
            basic = (val,userid)
            mycur.execute(insert_query, basic)
            connection.commit()
            print("groceries is changed to", val)
        cho = input("do you want to change another value (y/n): ")
        if cho == "y":
            c = 1
        elif cho == "n":
            c = 0
            
def view_old_values(x):
    main_loop = 1
    query="select Insurances,Utility,Rent,Personal_Upkeep,Subscriptions,Entertainment,Groceries from central where userid=%s;"
    dict_1 = mycur.execute(query,(userid))
    [dict_1]=mycur.fetchall()
    connection.commit()
    while main_loop == 1:
        print('''What would like to see : 
                          1.Maximum expenditure of the month 
                          2.Minimum expenditure of the month
                          3.Total expenditure of the month
                          4.Mean expenditure of the month
                          5.Range expenditure of the month
                          6.Visualisations for the month 
                          7.Quit''')
        choice = eval(input("please enter your the number of your choice: "))
        dict_max = max(dict_1.values())
        for key in dict_1:
            if dict_1[key] == dict_max:
                max_val = dict_max
                max_val_key = key
                
        dict_min = min(dict_1.values())
        for key in dict_1:
            if dict_1[key] == dict_min:
                min_val = dict_min
                max_min_key = key
       
        if choice == 1:
            print("the maximum value spent was for", max_val_key ,"--->", max_val)
        elif choice == 2:
            print("the minimum value spent was for", max_min_key ,"--->", min_val)
        elif choice == 3:
            print("the total value spent was --->",sum(dict_1.values()))
        elif choice == 4:
            print("the mean value spent was --->",stat.mean(dict_1.values()))
        elif choice == 5:
            print("the range of the values spent was --->",max_val - min_val)
        elif choice == 6:
            s = 1
            while s == 1:
                print('''The available visualization are : 
                                  1. Pie charts representing the total spending
                                  2. Bar graph
                                  3. Quit''')
                choi = int(input("please enter your choice : "))
                if choi == 1:
                        values = dict_1.values()
                        keys = ('Insu', 'Utili', 'Rent', 'Per_Upk', 'Subs', 'Ent', 'Groc')
                        colors = [ "#fa4274","#fc9cb5","#d9ae94", "#f58b51", "#f3712b", "#ea6016"]
                        plt.pie(values, labels=keys, colors=colors, 
                                shadow= True,
                                autopct = "%1.1f%%",
                                wedgeprops={"edgecolor": "black", "linewidth":2}, startangle= 180)
                        plt.title("Pie charts representing the total spending")
                        plt.tight_layout()
                        choi_f_plt = input("do you want to save the pie chart(y/n) ?")
                        if choi_f_plt == 'y':
                            plt.savefig('piechart.jpg')
                            print("The pie chart is stored as piechart.jpg")
                        plt.show()
                        
                elif choi == 2:
                        colors = ["#fa4274","#fc9cb5","#d9ae94", "#f58b51", "#f3712b", "#ea6016"]
                        y_axis = list(dict_1.values())
                        x_axis = ('Insu', 'Utili', 'Rent', 'Per_Upk', 'Subs', 'Ent', 'Groc')
                        plt.bar(x_axis,y_axis, color = colors)
                        plt.legend()
                        plt.title("Bar graph of spending")
                        plt.xlabel('The category of spending')
                        choi_f_plt = input("do you want to save the plot(y/n) ?")
                        if choi_f_plt == 'y':
                            plt.savefig('barplot.jpg')
                            print("The bar plot is stored as barplot.jpg")
                        
                        plt.show()
                else:
                        print("Leaving the subsection")
                        s = 0
        elif choice == 7:
            print("Thank you!")
            main_loop = 0
            break
        else: 
            print("please enter the correct choice ! ")
        
        choi1 = input("do you want to enter another value(y/n): ")
        if choi1.lower() == "y":
            pass
        elif choi1.lower() == "n":
            print("Thank you!")
            main_loop = 0
            break
        else:
            print("Quiting the sub-part and returning to the main menu !")
            main_loop = 0
        
            
    
#_main_ 
print("                                  -------------X-------- MONTHLY EXPENSE TRACKER --------X-------------                            ")
print('''This Python and SQL-based monthly expense tracker is a versatile tool with practical real-world applications. It 
      empowers users to efficiently manage their finances and gain valuable insights into their spending patterns. This 
      expense tracker promotes financial responsibility, efficient resource allocation, and informed decision-making, 
                             making it a valuable asset for both individuals and organizations.''')

   
#These are the basic functioning to check if the user exits or no.
user_basic_info()
insert_query = "select Name from central where Name = %s;"
x = mycur.execute(insert_query, (name_user))
if x == 1:
    print("THE USER ALREADY EXISTS.")
    insert_query_main= "select userid from central where Name=%s and Dob=%s;"
    myuserid=mycur.execute(insert_query_main,(name_user,DOB))
    [myuserid]=mycur.fetchall()
    userid=myuserid["userid"]
    connection.commit()   
elif x == 0:
    print("THE USER DOES NOT EXIST ! ")
    userid = primary_key_for_user()
    user_basic(userid)

#Now we start with the actual functions of the project. 
# since it needs to be a menu driven format 
c = 1
while c == 1:
    choice = menu()
    if choice == 1:
        change_val(userid)
    #function for chenging the values
    elif choice == 2:
        view_old_values(userid)
    #function for viewing older values 
    elif choice == 3:
        print("THANK YOU :) ")
        c = 0
    
    
mycur.close()
connection.close()



