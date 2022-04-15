import os 
import sqlite3
import random

def prepDB():
    # delete the db to start over
    os.remove('notebook.db')
    # open db and obtain cursor 
    con = sqlite3.connect('notebook.db')
    cur = con.cursor()
    # create tables
    try: 
        cur.execute("""CREATE TABLE people (
        id INTEGER,
        first_name TEXT,
        last_name TEXT,
        age INTEGER
        )    
        """)
    except:
        print('table already made')
    try: 
        cur.execute("""CREATE TABLE hobby (
        name TEXT,
        kind TEXT,
        setting TEXT
        )    
        """)
    except:
        print('table already made')
    try: 
        cur.execute("""CREATE TABLE Institution (
        name TEXT,
        type TEXT
        )    
        """)
    except:
        print('table already made')
    try: 
        cur.execute("""CREATE TABLE profession (
        name TEXT,
        feild TEXT
        )    
        """)
    except:
        print('table already made')
    try: 
        cur.execute("""CREATE TABLE worksAs (
        pid INTEGER,
        professionName TEXT,
        comany TEXT,
        yearsExp INTEGER
        )    
        """)
    except:
        print('table already made')
    try: 
        cur.execute("""CREATE TABLE studdied (
        pid INTEGER,
        instName TEXT,
        major TEXT,
        degreeType TEXT
        )    
        """)
    except:
        print('table already made')
    try: 
        cur.execute("""CREATE TABLE hasHobby (
        pid INTEGER,
        hobbyName TEXT,
        yearsDone INTEGER
        )    
        """)
    except:
        print('table already made')
    #database complete 
    con.commit()
    con.close()
    print('tables ready!')

f_names = [
            'cade',
            'john',
            'mary',
            'patricia',
            'lisa',
            'charles',
            'jennifer',
            'thomas',
            'stephanie',
            'will',
            'joe',
            'betty',
            'grace',
            'matthew',
            'mark',
            'quin']
l_names = [
        'smith',
        'williams',
        'lopez',
        'lueker',
        'johnson',
        'oneal',
        'connors',
        'richardson',
        'robinson',
        'rogers',
        'michaels',
        'nelson',
        'edwards',
        'doe',
        'mitchel',
        'lafrance']

def randNames(f_names, l_names): 
    f_names = f_names.copy()
    l_names = l_names.copy()
    names = []
    id = 0
    while(len(f_names) > 0):
        f_index = random.randint(0, len(f_names) - 1)
        l_index = random.randint(0, len(l_names) - 1)
        f = f_names.pop(f_index)
        l = l_names.pop(l_index)
        age = random.randint(18,50)
        names.append((id,f,l,age))
        id = id + 1
    return names

# people ready 
people = randNames(f_names, l_names)

# hobby class 
class Hobby:
    def __init__(self, name, kind, setting):
        self.name = name
        self.kind = kind
        self.setting = setting

# hobbies 
biking = Hobby('biking', 'exercise', 'outdoor')
swimming = Hobby('swimming', 'exercise', 'indoor')
chess = Hobby('chess', 'intellectual', 'indoor')
soccer = Hobby('soccer','sport','outdoor')
hiking = Hobby('hiking','exercise','outdoor')
camping = Hobby('camping', 'recreation', 'outdoor')
cooking = Hobby('cooking','creative','indoor')
painting = Hobby('painting','creative','indoor')
fishing = Hobby('fishing','recreation','outdoor')
tennis = Hobby('tennis','sport','outdoor')
basketball = Hobby('basketball', 'sport','indoor')
running = Hobby('running','exercise','outdoor')
writing = Hobby('writing','intellectual','indoor')
photography = Hobby('photography','creative','outdoor')

hobbies = [biking, swimming,
        chess, soccer,
        hiking, camping,
        cooking, painting,
        fishing, tennis,
        basketball, running,
        writing, photography]

def hobbyTuple(hobbies):
    h_list = []
    for hobby in hobbies:
        h_list.append((hobby.name,
            hobby.kind,
            hobby.setting))
    return h_list

# list of hobbies
hobbies = hobbyTuple(hobbies)

# institutions 
institutions = [("CWRU","University"),
                   ("Cornell","University"),
                   ("OTIS","Art School"),
                   ("CSA", "Art School"),
                   ("CIM", "Music School"),
                   ("Ohio State", "University")]

# professions
professions = [('electrician','trade'),
                  ('programmer', 'tech'),
                  ('teacher', 'education'),
                  ('systems engineer', 'tech'),
                  ('chef','restaurant'),
                  ('waiter','restaurant'),
                  ('mechanic','trade')]

# companies 
companies = ['sony','google',
        'case western','amazon',
        'honda','pizza hut',
        'toyota', 'johnson and johnson',
        'facebook','cleveland clinic',
        'uber','apple',
        'irs','cia']

def populateDB(people, hobbies, institutions, professions, companies):
    # connect to db 
    con = sqlite3.connect('notebook.db')
    cur = con.cursor()
    # insert people
    cur.executemany("insert into people values (?, ?, ?, ?)", people)
    # insert hobbies
    cur.executemany("insert into hobby values (?, ?, ?)", hobbies)
    # insert institutions 
    cur.executemany("insert into institution values (?, ?)", institutions)
    # insert professions
    cur.executemany("insert into profession values (?, ?)", professions)
    # iterate through people and create relations 
    for person in people:
        # hobby 
        hobbyIndex = random.randint(0,len(hobbies)-1)
        hobby = hobbies[hobbyIndex] 
        h_years = random.randint(1,10)
        cur.execute("insert into hasHobby values (?,?,?)", (person[0], hobby[0], h_years ))
        # profession
        p_i = random.randint(0,len(professions)-1)
        p_years = random.randint(1,10)
        c_name = random.choice(companies)
        cur.execute("insert into worksAs values (?, ?, ?, ?)",
                (person[0], professions[p_i][0], c_name, p_years))
        # institution
        i_i = random.randint(0, len(institutions)-1)
        major = random.choice(['english','computer science',
            'math', 'painting',
            'singing', 'biology',
            'mech E', 'data science',
            'drama', 'creative writing',
            'chemistry', 'physics'])
        degree = random.choice(['bachelors','masters','associates','phd'])
        cur.execute("insert into studdied values (?, ?, ?, ?)",
                (person[0], institutions[i_i][0], major, degree))

    # commit changes
    con.commit()
    con.close()
    print('database populated')

if __name__ == "__main__":
    prepDB()
    populateDB(people,hobbies, institutions, professions, companies)
