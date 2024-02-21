import json

with open('C:\\Users\\adler\\Documents\\PP-2024\\Lab4\\json\\sample-data.json') as json_file:
    new_data = json.load(json_file)

print("Interface status")
print("================================================================================")
print("DN                                                 Description           Speed    MTU  ")
print("-------------------------------------------------- --------------------  ------  ------")

item1 = new_data["imdata"][0]
item2 = new_data["imdata"][1]
item3 = new_data["imdata"][2]

print(item1["l1PhysIf"]["attributes"]["dn"],"                            ",item1["l1PhysIf"]["attributes"]["speed"]," ",item1["l1PhysIf"]["attributes"]["mtu"])
print(item2["l1PhysIf"]["attributes"]["dn"],"                            ",item2["l1PhysIf"]["attributes"]["speed"]," ",item2["l1PhysIf"]["attributes"]["mtu"])
print(item3["l1PhysIf"]["attributes"]["dn"],"                            ",item3["l1PhysIf"]["attributes"]["speed"]," ",item3["l1PhysIf"]["attributes"]["mtu"])