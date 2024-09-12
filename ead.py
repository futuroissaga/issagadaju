
altura_chico = 1.50
altura_juca = 1.10

crescimento_chico = 0.02  
crescimento_juca = 0.03   


anos = 0


while altura_juca <= altura_chico:
    altura_chico += crescimento_chico  
    altura_juca += crescimento_juca    
    anos += 1                          


print(f"Serão necessários {anos} anos para que Juca seja maior que Chico.")
