emp={
    "id":101,
    "name":"Riya Patel",
    "designation":"Manager",
    "salary":20000
}
print("Original Dictionary:")
print(emp)
del emp["designation"]
print("\nDictionary after deleting 'designation' key:")
print(emp)
emp["name"]="Ekta Patel"
print("\nDictionary after updating 'name' value:")
print(emp)