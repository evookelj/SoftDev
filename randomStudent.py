#Emma Vukelj and Kenneth Li
#SoftDev period 6
#09-13-2016

from random import choice, randint

CLASSES =  {4: [ 'Ayman', 'Shaeq', 'Patrick', 'Yvonne', 'Wilson', 'Brian', 'Farhan', 'Janet', 'Harry', 'Kevin', 'Nicholas', 'Jason', 'Yikai', 'Emma', 'Kenneth', 'Nala', 'Karol', 'Elias', 'Ely', 'Reo', 'Dhiraj', 'Amy', 'Arvind', 'Nobel', 'Angela', 'Edward', 'Jonathan', 'Celine', 'Daniel', 'Lindsey', 'Ziyan', 'Elina'], 8: ['Julian', 'Sebastian', 'Jordan', 'Alan', 'Yuki', 'Chloe', 'Noah', 'Edvic', 'Jia Qi', 'Shan', 'Rodda', 'Anya', 'Edmond', 'Asher', 'Kathy', 'Sharon', 'Vncent', 'Lawrence', 'Sachal', 'Gabriel', 'Jason', 'Daniel', 'Felix', 'Jacob', 'Bayle', 'Fortune', 'Gio', 'Kelly', 'William', 'Jordan', 'Haley', 'Henry'],9: ['James', 'Vanna', 'Zicheng', 'Quinn', 'Anthony C', 'Joel', 'Steph', 'Xinhui', 'Richard', 'Misha', 'Maddie', 'Winston', 'Shariar', 'Nancy', 'Jerry', 'Michael', 'Stiven', 'Will',  'Olivia', 'Constantine', 'Jessica', 'Kate', 'Shamaul', 'Max', 'Sarah', 'Anthony L', 'Brandon', 'Nicole', 'Brian', 'Issac', 'Seiji', 'Lorenz']}

def randStudentOfPd(n):
    print choice(CLASSES[n])

def main():
    pd = randint(0,2)
    if pd==1: randStudentOfPd(4)
    elif pd==2: randStudentOfPd(8)
    else: randStudentOfPd(9)

main()
