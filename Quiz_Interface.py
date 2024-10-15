print("Welcome to KBC\nPress enter to start")
input()
def KBC():
    ques= [
        ["What is the capital of India ?", 'Bhubaneswar','Kolkata','Delhi','Chennai',3],
        ["Who's the first president of India ?", 'Rajendra Prasad','J. Nehru','MG','Jethalal',1],
        ["Who's the CEO of Google ?", 'Sundar Pichai','Ambani','Bill Gates','Tim Cook',1],
        ["In which lang. was Facebook created ?", 'Python','JavaScript','C#','php',4],
        ["Who let the ____ out ?", 'Cats','Dogs','Turtle','Capybara',2],
        ["Who let the ____ out ?", 'Cats','Dogs','Turtle','Capybara',2],
    ]


    levels= [1000,2000,4000,8000,16000,32000]
    money= 0
    
    for i in range(0,len(ques)):
        question= ques[i]
        print('----------------')
        print(f'{(i+1)}. Question for Rs. {levels[i]} is: {question[0]}')
        print(f'a.{question[1]}        b.{question[2]}')
        print(f'c.{question[3]}        d.{question[4]}\n')

        ans= int(input("Type your answer (1-4) >> "))
        if ans==question[-1]:
            print(f'\nCongratulations! You won Rs.{levels[i]}\n')
            if i == 1:
                money = 2000
            elif i == 3:
                money = 8000
            elif i == 5:
                money = 32000
        else:
            print("\nWrong Answer!")
            break

    print(f"Congratulations! You're taking Rs.{money} with you home.")

KBC()
