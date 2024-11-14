# relink foreground database to new background database

old_db_name = "carbon fiber"

# current background database
old_dependency_name = "ecoinvent-3.10-cutoff"

# new background database to link to
new_dependency_name = "ecoinvent-3.10-cutoff"

# new foreground database name
new_db_name = f"{old_db_name} {new_dependency_name}"

# load database object
db = bw2data.Database(old_db_name)

# turn it into a dictionary
data = db.load()

for i, ds in data.items():

    ds["database"] = new_db_name
    for e in ds["exchanges"]:
        #print(e)
        if e.get("input")[0] == old_dependency_name:
            e["input"] = (new_dependency_name, e["input"][1])
        
        e["output"] = (new_db_name, e["output"][1])

        if e["type"] == "production":
            e["output"] = e["input"]
data = {(new_db_name, k[1]): v for k, v in data.items()}

# write it back to project
bw2data.Database(new_db_name).write(data)