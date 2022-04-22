print("Bienvenido a la calculadora preventiva de gorreros.")
cuenta = input("¿De cuanto es la cuenta que le tienen que pagar al cachon del estanco? $")
propina = input("¿Cuanto vas a tirarle de propina al vale por buena gente? ¿7,10,15 porciento? ")
gorreros = input("¿Entre cuantos gorreros vas a dividir la cuenta? ")

valor_propina = int(propina) / 100
valor_propina *= float(cuenta)
final_cuenta = float(valor_propina) + float(cuenta)
total_diferido = float(final_cuenta) / float(gorreros)

round_total = round(total_diferido,2)
print(f"Todos los gorreros deben pagar ${round_total}")