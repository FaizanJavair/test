import noapi
import random
# Getting Started Tutorial


async def main():
   

    start = noapi.datastore("test-school")
   
    school = start.schools.first()
    students = school.students


    for i in students:
        print(i._oid + " - " +i.name)




    noapi.disconnect()


if __name__ == "__main__":
    noapi.run(main())