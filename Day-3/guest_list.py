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

