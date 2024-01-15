def dodawanie(a,b):
	return a + b

def odejmowanie(a,b):
	return a - b

def mnozenie(a,b):
	return a * b

def dzielenie(a,b):
	if b != 0:
		return a / b
	else:
		return "Nie mozna dzielic przez zero"

liczba1 = float(input("Podaj pierwsza liczbe: "))
liczba2 = float(input("Podaj druga liczbe: "))

print("Dodawanie: ", dodawanie(liczba1, liczba2))
print("Odejmowanie: ", odejmowanie(liczba1, liczba2))
print("Mnozenie: ", mnozenie(liczba1, liczba2))
print("Dzielenie: ", dzielenie(liczba1, liczba2))
