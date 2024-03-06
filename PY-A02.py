def main():
    # Solicita ao usuário que digite 10 valores para preencher a lista
    numbers = []
    for i in range(10):
        value = int(input(f"Digite o {i + 1}º valor: "))
        numbers.append(value)

    # Separa os números pares e ímpares em listas diferentes
    even_numbers = [num for num in numbers if num % 2 == 0]
    odd_numbers = [num for num in numbers if num % 2 != 0]

    # Exibe os números pares
    print("Números pares:", even_numbers)

    # Exibe os números ímpares em uma tupla
    print("Números ímpares:", tuple(odd_numbers))

    # Exibe a quantidade de números pares e ímpares
    print("Quantidade de números pares:", len(even_numbers))
    print("Quantidade de números ímpares:", len(odd_numbers))

    # Calcula e exibe a soma de todos os números pares e ímpares
    sum_even = sum(even_numbers)
    sum_odd = sum(odd_numbers)
    print("Soma dos números pares:", sum_even)
    print("Soma dos números ímpares:", sum_odd)


if __name__ == "__main__":
    main()
