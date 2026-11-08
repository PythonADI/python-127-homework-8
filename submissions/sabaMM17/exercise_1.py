phones = {"Nina": "555-1234", "Luka": "555-9876"}
print(f"Luka: {phones['Luka']}")

print(f"Ana: {phones.get('Ana','unknown')}")

phones["Ana"] = "555-0000"

phones["Nina"] = "555-1111"

print(f"Has Luka: {'Luka' in phones}")

removed = phones.pop("Luka")
print(f"Removed: {removed}")

print(phones)
print(f"{len(phones)} contacts")