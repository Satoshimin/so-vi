#!/user/bin/python3

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

print("Dodawanie: ", dodawanie(2, 2))
print("Odejmowanie: ", odejmowanie(2, 2))
print("Mnozenie: ", mnozenie(2, 2))
print("Dzielenie: ", dzielenie(2, 2))
