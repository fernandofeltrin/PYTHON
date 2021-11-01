from collections import Counter

texto = 'A Radiologia é a ciência que estuda a anatomia por meio de radiações'

a1, a2, a3, a4, a5, a6 = Counter(texto).most_common(6)

print(f'O elemento mais comum é: "{a2[0]}", repetido {a2[1]} vezes')
print(f'O elemento mais comum é: "{a3[0]}", repetido {a3[1]} vezes')
print(f'O elemento mais comum é: "{a4[0]}", repetido {a4[1]} vezes')
print(f'O elemento mais comum é: "{a5[0]}", repetido {a5[1]} vezes')
print(f'O elemento mais comum é: "{a6[0]}", repetido {a6[1]} vezes')
