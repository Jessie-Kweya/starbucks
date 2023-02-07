person={"name":"John Doe","Age":30,"location":"Nairobi","email":"johndoe@gmail.com"}
print(person["name"])
dict1={"first_name":"John","sur_name":"Doe","Age":30,"location":"Nairobi","email":"johndoe@gmail.com"}
print(dict1["first_name"])

ls1=["John",60,[50,60,40],{"location":"Mombasa"}]
print(ls1[2][2])
print(ls1[3]["location"])

#connect to a database and access a voters table
voters={
"30367812" : {"fname" : "John Maina", "dob" : "1997-12-12", "cons" : "Embakasi East", "cou" :"Nairobi",  "ward" :"Fedha"},
"29873526" : {"fname" : "Mohamed Adan", "dob" :  "1994-10-09", "cons" : "Kitale North", "cou" : "Kitale",  "ward" :"Central"},
"32895634" : {"fname" : "MaryAnne", "dob" :  "2001-11-04", "cons" : "Langata","cou" :"Nairobi", "ward" :"NWest"}
}
data=input("Enter National ID No.")
print(type(data))
data=data.strip()
print(voters[data]["fname"])

mykeys = voters.keys()
mykeys = list(mykeys)
print(type(mykeys))
print(mykeys)
checker = (data in mykeys)
print(checker)
#use if statement to display error if ID doesn't exist