def acronym_creator(str):
    index = 0
    new  = ""
    while index+1 < len(str):
        if str[index] == " " and str[index+1]!=" ":
            new += str[index+1]
        index+=1
    return(str[0].upper()+new.upper())
