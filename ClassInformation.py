
'''
#Create a dictionary with every student's First Name , Last Name , Age, Status, Address
#create a variable named studentName and ask input from the user

'''

#Creating the dictionary

from tkinter.font import names


classInformation = {
    "aryan" : {
        "firstName" : "Aryan",
        "lastName" : "Tamang",
        "age" : 18,
        "status" : "CEO",
        "address" : "Goldhunga, Balaju"
    },
    "prabin" :  {
        "firstName" : "Prabin",
        "lastName" : "Tamang",
        "age" : 19,
        "status" : "Chupa Rustom",
        "address" : "Lolang, Balaju"
    } ,
    "neeraj" :  {
        "firstName" : "Neeraj",
        "lastName" : "Paudel",
        "age" : 20,
        "status" : "Pawan's Besty",
        "address" : "Hetauda"
    },
    "pritam" : {
        "firstName" : "Pritam",
        "lastName" : "Shrestha",
        "age" : 19,
        "status" : "Anjana's Boy Friend",
        "address" : "Sukedhara, Ring Road"
    } ,
    "kshitish" : {
        "firstName" : "Kshitish",
        "lastName" : "Bhurtel",
        "age" : 21,
        "status" : "Chinese",
        "address" : "Mandikhatar, Dhumbarai"
    } ,
    "nitesh" : {
        "firstName" : "Nitesh",
        "lastName" : "Panta",
        "age" : 19,
        "status" : "Sticker man",
        "address" : "Bhaktapur"
    } ,
    "dibash" :  {
        "firstName" : "Dibash",
        "lastName" : "Thapa",
        "age" : 19,
        "status" : "Genius",
        "address" : "Puyatar, Balaju"
    },
    "prashant" :  {
        "firstName" : "Prashant",
        "lastName" : "Shrestha",
        "age" : 19,
        "status" : "Gamer",
        "address" : "New baneshwor"
    },
    "pawan" :  {
        "firstName" : "Pawan",
        "lastName" : "Khanal",
        "age" : 22,
        "status" : "Guffadi + Neeraj's Besty",
        "address" : "Goldhunga, Balaju"
    },
    "pukar" :  {
        "firstName" : "Pukar",
        "lastName" : "Khadka",
        "age" : 19,
        "status" : "Romeo",
        "address" : "Goldhunga, Balaju"
    },
    "sanjina" :  {
        "firstName" : "sanjina",
        "lastName" : "kim",
        "age" : 19,
        "status" : "Dhokebaj",
        "address" : "Baluwatar"
    },
    "sanjana" :  {
        "firstName" : "Sanjana",
        "lastName" : "Prajapati",
        "age" : 19,
        "status" : "Nice Person",
        "address" : "Dhumbarai"
    },
    "sakshi" :  {
        "firstName" : "Sakshi",
        "lastName" : "Thapa",
        "age" : 19,
        "status" : "Don",
        "address" : "Mandikhatar, Dhumbarai"
    },
    "srijana" :  {
        "firstName" : "Srijana",
        "lastName" : "Dahal",
        "age" : 19,
        "status" : "Veggy",
        "address" : "Dhumbarai"
    },
}


if __name__ == "__main__" :

    #creating studentName variable and asking fot the input from the user

    studentName = input("Enter the name of the student that you want to know about : ")

    #printing the details of Student
    print("\n First Name : ", classInformation[studentName]['firstName'])
    print("\n Last Name : ", classInformation[studentName]['lastName'])
    print("\n Age : ", classInformation[studentName]['age'])
    print("\n Status : ", classInformation[studentName]['status'])
    print("\n Address : ", classInformation[studentName]['address'])