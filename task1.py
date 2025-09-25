import timeit
from boyer_moore import boyer_moore_search
from kmp_search import kmp_search
from rabin_karp import rabin_karp_search



with open('стаття_1.txt', 'r', encoding='utf-8') as f:
    text1 = f.read()
with open('стаття_2.txt', 'r', encoding='utf-8') as f:
    text2 = f.read()

existing_pattern = "алгоритм"
fake_pattern = "qwe123asd"

print("\nстаття 1:")
print(f"Існуючий '{existing_pattern}':")
print(f"Боєра-Мура: {timeit.timeit(lambda: boyer_moore_search(text1, existing_pattern), number=100):.6f} сек")
print(f"Кнута-Морріса-Пратта: {timeit.timeit(lambda: kmp_search(text1, existing_pattern), number=100):.6f} сек")
print(f"Рабіна-Карпа: {timeit.timeit(lambda: rabin_karp_search(text1, existing_pattern), number=100):.6f} сек")

print(f"Вигаданий '{fake_pattern}':")
print(f"Боєра-Мура: {timeit.timeit(lambda: boyer_moore_search(text1, fake_pattern), number=100):.6f} сек")
print(f"Кнута-Морріса-Пратта: {timeit.timeit(lambda: kmp_search(text1, fake_pattern), number=100):.6f} сек")
print(f"Рабіна-Карпа: {timeit.timeit(lambda: rabin_karp_search(text1, fake_pattern), number=100):.6f} сек")

print("\nстаття 2:")
print(f"Існуючий '{existing_pattern}':")
print(f"Боєра-Мура: {timeit.timeit(lambda: boyer_moore_search(text2, existing_pattern), number=100):.6f} сек")
print(f"Кнута-Морріса-Пратта: {timeit.timeit(lambda: kmp_search(text2, existing_pattern), number=100):.6f} сек")
print(f"Рабіна-Карпа: {timeit.timeit(lambda: rabin_karp_search(text2, existing_pattern), number=100):.6f} сек")

print(f"Вигаданий '{fake_pattern}':")
print(f"Боєра-Мура: {timeit.timeit(lambda: boyer_moore_search(text2, fake_pattern), number=100):.6f} сек")
print(f"Кнута-Морріса-Пратта: {timeit.timeit(lambda: kmp_search(text2, fake_pattern), number=100):.6f} сек")
print(f"Рабіна-Карпа: {timeit.timeit(lambda: rabin_karp_search(text2, fake_pattern), number=100):.6f} сек")