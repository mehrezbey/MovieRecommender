import pandas as pd

def processFacts(facts:list):
    facts_pd = {}
    # 1- Budget
    if "high-budget" in  facts[0]: #<
        facts_pd["budget_inf"]  = 15000000
        facts_pd["budget_sup"]  = 500000000
    elif "independent" in  facts[0]:
        facts_pd["budget_inf"]  = 0
        facts_pd["budget_sup"]  = 15000000
    else:
        facts_pd["budget_inf"]  = 0
        facts_pd["budget_sup"]  = 500000000
    
    # 2- genre
    facts_pd["genres"] = facts[1]
    
    # 3- superhero
    facts_pd["superheros"]  = "Yes" in  facts[2]

    # 4- Language
    if facts[3] == "English" :
        facts_pd["original_language"]  = "en"
    else:
        facts_pd["original_language"]  = ""
        
    # 5- Release Date
    if "Gen Z" in facts[4] :
        facts_pd["release_date"] = "2010-01-01"
        
    elif "Millennial" in facts[4]:
        facts_pd["release_date"] = "1990-01-01"
        
    elif "Gen X" in facts[4]:
        facts_pd["release_date"] = "1970-01-01"
        
    elif "Boomer" in facts[4]:
        facts_pd["release_date"] = "1950-01-01"
    else:
        facts_pd["release_date"] = "1900-01-01"
        
        
    # 6- Box Office
    if "Blockbuster" in  facts[5]:#
        facts_pd["revenue_inf"] = 500000000
        facts_pd["revenue_sup"] = 5000000000

        
    elif "Hit" in  facts[5]:#<
        facts_pd["revenue_inf"] = 100000000
        facts_pd["revenue_sup"] = 5000000000
        
    elif "Low" in  facts[5] :#<
        facts_pd["revenue_inf"] = 0
        facts_pd["revenue_sup"] = 100000000
    else:
        facts_pd["revenue_inf"] = 0
        facts_pd["revenue_sup"] = 5000000000
    
    
    # 7- Runtime
    if "Short" in facts[6] :
        facts_pd["runtime_inf"] = 0
        facts_pd["runtime_sup"] = 60

        
    elif "Medium" in facts[6] :
        facts_pd["runtime_inf"] = 60
        facts_pd["runtime_sup"] = 90
        
    elif "Standard" in facts[6]  :
        facts_pd["runtime_inf"] = 90
        facts_pd["runtime_sup"] = 120
        
    elif "Long" in facts[6] :
        facts_pd["runtime_inf"] = 120
        facts_pd["runtime_sup"] = 1000
    else:
        facts_pd["runtime_inf"] = 0
        facts_pd["runtime_sup"] = 1000

    return facts_pd
            
def selectMovies(facts:list):
    df = pd.read_csv("data/movies.csv")
    facts_pd = processFacts(facts)

    res = df[
        
                ((df['budget']>facts_pd["budget_inf"])&(df['budget']<facts_pd["budget_sup"]))&
                (df['genres'].str.contains(facts_pd["genres"], case=False, na=False))&
                (df['original_language'].str.contains(facts_pd["original_language"], case=False, na=False))&
                (df['release_date']>facts_pd["release_date"])&
                ((df['revenue']>facts_pd["revenue_inf"])&(df['revenue']<facts_pd["revenue_sup"]))&
                ((df['runtime']>facts_pd["runtime_inf"])&(df['runtime']<facts_pd["runtime_sup"]))
            ]
    # exclude superheros movies if user said no
    if (facts_pd["superheros"]==False):
        res = res[~res['keywords'].str.contains("marvel", case=False, na=False)]
        res = res[~res['keywords'].str.contains("dc", case=False, na=False)]
        res = res[~res['keywords'].str.contains("comic", case=False, na=False)]
    res.to_csv('data/output.csv', index=False)  # index=False to avoid writing row numbers
    return res

