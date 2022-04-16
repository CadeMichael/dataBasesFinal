import sqlite3

# hobby 
def hobbyQuery(h_name, h_kind, h_setting):
    query = """
    select first_name, last_name, age 
    from people, hasHobby, hobby
    Where id = pid AND hobbyName = name
    """
    if h_name == "":
        pass
    else:
        query += "AND name = '{}'".format(h_name)
    if h_kind == "":
        pass
    else:
        query += "AND kind = '{}'".format(h_kind)
    if h_setting == "":
        pass
    else:
        query += "AND setting = '{}'".format(h_setting)
    return query

# profession
def jobQuery(p_name, p_company, p_field):
    query = """
    select first_name, last_name, age 
    from people, worksAs, profession
    Where id = pid AND professionName = name
    """
    if p_name == "":
        pass
    else:
        query += "AND name = '{}'".format(p_name)
    if p_company == "":
        pass
    else:
        query += "AND company = '{}'".format(p_company)
    if p_field == "":
        pass
    else:
        query += "AND field = '{}'".format(p_field)
    return query

# studdied as 
def educationQuery(i_name, i_type, i_major, i_degree):
    query = """
    select first_name, last_name, age 
    from people, studdied, institution
    Where id = pid AND instName = name
    """
    if i_name == "":
        pass
    else:
        query += "AND name = '{}'".format(i_name)
    if i_type == "":
        pass
    else:
        query += "AND type = '{}'".format(i_type)
    if i_major == "":
        pass
    else:
        query += "AND major = '{}'".format(i_major)
    if i_degree == "":
        pass
    else:
        query += "AND degreeType = '{}'".format(i_degree)
    return query

# age 
def ageQuery(min, max):
    query = "select first_name, last_name, age from people where"
    if min > 0 and max < 0:
        query += " age >= {} ".format(min)
    elif max > 0 and min < 0:
        query += " age <= {} ".format(max)
    else:
        query += " age >= {} AND ".format(min)
        query += " age <= {} ".format(max)
    return query

# all queries 
def queryPrefs(minAge,
        maxAge,
        pName,
        pCompany,
        pField,
        hName,
        hKind,
        hSetting,
        eName,
        eType,
        eMajor,
        eDegree):
    # establish connection with database
    con = sqlite3.connect('notebook.db')
    cur = con.cursor()
    # handle empty int form values 
    if minAge == '':
        minAge = -1
    else: 
        minAge = int(minAge)
    if maxAge == '':
        maxAge = -1
    else: 
        maxAge = int(maxAge)
    # set matches to impossible value
    matches = [-1]
    # check if age was queried 
    if minAge > 0 or maxAge > 0:
        # get query
        age_q = ageQuery(minAge, maxAge)
        # get people
        age_approved = cur.execute(age_q).fetchall()
        # intersection with other query was null, break
        if matches == []:
            return []
        # first query triggered
        elif matches == [-1]:
            matches = age_approved
        else:
            # intersection of matches 
            matches = set.intersection(set(matches), set(age_approved))
    # check for profession queries
    if pName != "" or pCompany != "" or pField != "":
        job_q = jobQuery(pName, pCompany, pField)
        job_approved = cur.execute(job_q).fetchall()
        if matches == []:
            return []
        elif matches == [-1]:
            matches = job_approved
        else:
            matches = set.intersection(set(matches), set(job_approved))
    # check for hobby queries 
    if hName != "" or hKind != "" or hSetting != "":
        hobby_q = hobbyQuery(hName, hKind, hSetting)
        hobby_approved = cur.execute(hobby_q).fetchall()
        if matches == []:
            return []
        elif matches == [-1]:
            matches = hobby_approved
        else:
            matches = set.intersection(set(matches), set(hobby_approved))
    # check for education queries 
    if eName != "" or eType != "" or eMajor != "" or eDegree != "":
        prof_q = educationQuery(eName, eType, eMajor, eDegree)
        prof_approved = cur.execute(prof_q).fetchall()
        if matches == []:
            return []
        elif matches == [-1]:
            matches = prof_approved
        else:
            matches = set.intersection(set(matches), set(prof_approved))
    # check if there was no user input query
    if matches == [-1]:
        matches = cur.execute("select first_name, last_name, age from people").fetchall()
    con.commit()
    con.close()
    return matches
