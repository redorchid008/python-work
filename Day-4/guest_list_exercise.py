guest_list = ['baba', 'maa', 'tista', 'ahaan']
print(f"Hi {guest_list[0].title()}, you're invited to the dinner.")
print(f"Hi {guest_list[1].title()}, you're invited to the dinner.")
print(f"Hi {guest_list[2].title()}, you're invited to the dinner.")
print(f"Hi {guest_list[3].title()}, you're invited to the dinner.")

absent_from_guest_list = guest_list.pop(0)
print(absent_from_guest_list.title())

guest_list.insert(0, 'tini')
#print(guest_list)
print(f"Hi {guest_list[0].title()}, you're invited to the dinner.")
print(f"Hi {guest_list[1].title()}, you're invited to the dinner.")
print(f"Hi {guest_list[2].title()}, you're invited to the dinner.")
print(f"Hi {guest_list[3].title()}, you're invited to the dinner.")

print(f"{guest_list[0].title()}, {guest_list[1].title()}, {guest_list[2].title()}, {guest_list[3].title()} - we've found a bigger table.")

guest_list.insert(0, 'baba')
guest_list.insert(3, 'kaku')
guest_list.append('kakima')

print(guest_list)
print(len(guest_list))
print(f"{guest_list[0].title()}, {guest_list[1].title()}, {guest_list[2].title()}, {guest_list[3].title()}, {guest_list[4].title()}, {guest_list[5].title()}, {guest_list[6].title()} - we have space for only two guests.")

print(f"{guest_list.pop(0)}, I'm sorry. I can't invite you to dinner.")
print(f"{guest_list.pop(0)}, I'm sorry. I can't invite you to dinner.")
print(f"{guest_list.pop(0)}, I'm sorry. I can't invite you to dinner.")
print(f"{guest_list.pop(0)}, I'm sorry. I can't invite you to dinner.")
print(f"{guest_list.pop(2)}, I'm sorry. I can't invite you to dinner.")

print(f"{guest_list[0].title()} and {guest_list[1].title()}, you're still invited.")

print(guest_list)

del guest_list[0]
del guest_list[0]
print(guest_list)