words = {
    1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten',
    11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen',
    16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen', 20: 'twenty',
    30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety'
}


def to_words(n, omit_the_word_zero=False, needs_and_prefix_before_tens_or_units=False):
    if n > 999999:
        raise Exception("Can't convert something this big")
    if n == 0:
        if omit_the_word_zero:
            return ""
        return "zero"
    if n >= 1000:
        return to_words(n // 1000) + " thousand " + to_words(n - (n // 1000) * 1000, True, True)
    if n >= 100:
        return to_words(n // 100, True) + " hundred " + to_words(n - (n // 100) * 100, True, True)
    and_prefix = "and " if needs_and_prefix_before_tens_or_units else ""
    if n >= 20:
        if n - (n // 10) * 10 == 0:
            return and_prefix + words[(n // 10) * 10]
        else:
            return and_prefix + words[(n // 10) * 10] + "-" + to_words(n - (n // 10) * 10, True)
    return and_prefix + words[n]


def without_spaces_or_hyphens(string):
    return string.replace(" ", "").replace("-", "")


accumulator = 0
for x in range(1, 1001):
    accumulator += len(without_spaces_or_hyphens(to_words(x)))

print(accumulator)

# print(to_words(0))
# print(to_words(5))
# print(to_words(11))
# print(to_words(19))
# print(to_words(20))
# print(to_words(29))
# print(to_words(30))
# print(to_words(31))
# print(to_words(99))
# print(to_words(100))
# print(to_words(101))
# print(to_words(110))
# print(to_words(119))
# print(to_words(120))
# print(to_words(121))
# print(to_words(190))
# print(to_words(199))
# print(to_words(200))
# print(to_words(499))
# print(to_words(999))
# print(to_words(1000))
# print(to_words(1001))
# print(to_words(1011))
# print(to_words(1021))
# print(to_words(1120))
# print(to_words(1123))
# print(to_words(2000))
# print(to_words(10123))
# print(to_words(15123))
# print(to_words(20123))
# print(to_words(21123))
# print(to_words(159123))
