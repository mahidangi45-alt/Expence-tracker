# EXPENCE TRACKER PROJECT  => PERSONAL FINANCE APP 

expenseslist = []    # list of all expenses in form of dictionary


print("welcome to expence tracker 🙏  : kharcha tohda kam kiya karo :) ☺️")

while True:
    print("\n=========MENU=========")
    print("1. Add expences.")
    print("2. view all expences 👀 .")
    print("3. Total kharcha 🫴 .")
    print("4. Exit ")

    choise = input("please enter your choise  🤲 : ")

    # Add expence
    if (choise == "1"):  # input() string data hai, isliye "1" likha hai
        date = input("kis din kharcha kiya tha? : 🧐")
        category = input("kis type ka kharcha kiya tha ( food , makeup , dress, party etc ): 🤨 ")
        discription = input("details : 🤨 ")
        amount = float(input(" kitne ka kharcha kiya tha 🤨 "))

        expense = {
            "date" : date,
            "category" : category,
            "discription" : discription,
            "amount" : amount,
        }

        expenseslist.append(expense)
        print("\n expences are added 🤝 succesfully ✅ ")

    # view all expences 
    elif (choise == "2"):
        if (len(expenseslist) == 0):
            print("no expences added..😎...... jao ja ke kharcha karo 😜 ")
        else:
            print("================YE RAHA AAPKA SARA KHARCHA====🤖=========")
            count = 1
            for eachkharcha in expenseslist:
                # F-string ke andar single quotes (') use kiye hain taaki syntax error na aaye
                print(f"kharcha number {count} -> {eachkharcha['date']} , {eachkharcha['category']} , {eachkharcha['discription']} , {eachkharcha['amount']} ")
                count += 1

    # view total spending
    elif (choise == "3"):
        total = 0
        for eachkharcha in expenseslist:
            total = total + eachkharcha["amount"]
        
        print("\n TOTAL KHARCHA :", total)  # Yeh print ab 'elif' ke andar properly indented hai

    # EXIT
    elif (choise == "4"):
        print("DHANYABAD 🫶 AAPNE HAMARA SYSTEM USE KIYA 🥹")
        break
      
    else:
        print("INVALID CHOISE......❎.........👊🏼...TRY AGAIN ")


