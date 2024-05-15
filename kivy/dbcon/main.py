from db import Connection
from db import Students

conn = Connection()

def start():
    conn.clear()

    names = ["Антон Антонович", 'Никита Никитич', 'Федор Федорович', 'Александр Александрович', 'Павел Павлович']

    temp = []
    for item in names:
        temp.append(
            Students(name = item)
        )
        
    conn.add(temp)
    

def add(name):
    student = Students(name = name)
    conn.add(student)

def edit_last(name):
    item = conn.get_last()
    item.name = name
    conn.add(item)
    
    
if __name__ == '__main__':
    start()