from colorama import Fore, Style, init
init(autoreset=True)

print(Fore.CYAN + "--------------------------------------------")
print(Fore.CYAN + " 🌤️  WELCOME TO YOUR SMART WEATHER ADVISOR ")
print(Fore.CYAN + "--------------------------------------------")


temperature = int(input(Fore.YELLOW + "\nEnter today's temperature (°C): "))

print(Fore.WHITE + "\n🌡️  Weather Report:")

if temperature >= 40:
    print(Fore.RED + "🔥 It's extremely hot! Avoid going outside and drink plenty of water.")
    print(Fore.LIGHTRED_EX + "💧 Suggestion: Stay under shade or use an umbrella.")
elif temperature >= 30:
    print(Fore.YELLOW + "☀️ It's quite hot today. Good day for cold drinks or ice cream 🍦")
    print(Fore.LIGHTYELLOW_EX + "🧢 Suggestion: Wear sunglasses and light clothes.")
elif temperature >= 20:
    print(Fore.GREEN + "🌤️ The weather is perfect! Great time for a walk or a short trip 🚶‍♂️")
    print(Fore.LIGHTGREEN_EX + "🌳 Suggestion: Enjoy nature!")
elif temperature >= 10:
    print(Fore.BLUE + "🧥 It's getting cold. You should wear a light jacket.")
    print(Fore.LIGHTBLUE_EX + "☕ Suggestion: A warm cup of coffee will be great!")
else:
    print(Fore.CYAN + "❄️ It's freezing cold! Stay indoors and keep yourself warm.")
    print(Fore.LIGHTCYAN_EX + "🔥 Suggestion: Use a blanket and enjoy some hot soup 🍜")

print(Fore.MAGENTA + "\n✅ Have a wonderful day ahead!\n")
print(Fore.CYAN + "--------------------------------------------")
