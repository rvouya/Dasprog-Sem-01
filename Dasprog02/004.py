initial_color = input("Enter the first letter of the cylinder's color : ").strip().lower()

if initial_color == 'o':
    contents = "ammonia"
elif initial_color == 'b':
    contents = "carbon monoxide"
elif initial_color == 'y':
    contents = "hydrogen"
elif initial_color == 'g':
    contents = "oxygen"
else:
    contents = "Unknown"

print(f"Contents : {contents}")