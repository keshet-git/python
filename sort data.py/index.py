#students = ('Squidwerd','Arick','popy','goorg','Sandy','Patrick','Mr.Krabs')

#students.sort()
#sorted_students = sorted(students, reverse=True)
#for i in sorted_students:
#    print(i)

#students = [('Squidwerd', 'F', 60),
 #           ('goorg','B',45),
  #          ('Sandy','A',33),
   #         ('Patrick','D', 20),
    #        ('Mr.Krabs', 'C',78)]
#grade = lambda grade:grade[1]
#age = lambda age:age[2]
#students.sort(key=age,reverse=True)

#for i in students:
 #   print(i)

students = (('Squidwerd', 'F', 60),
            ('goorg','B',45),
            ('Sandy','A',33),
            ('Patrick','D', 20),
            ('Mr.Krabs', 'C',78))
#grade = lambda grade:grade[1]
age = lambda age:age[2]
sorted_students = sorted(students,key=age)

for i in sorted_students:
    print(i)