def check_anagram(text_a, text_b):
    if sorted(text_a) == sorted(text_b):
        print(f"{text_a} and {text_b} are Anagram of Each other")
