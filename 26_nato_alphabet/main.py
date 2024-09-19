import pandas


# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

result = False

while not result:
    word = input("Enter a word: ").upper()
    df = pandas.read_csv("nato_phonetic_alphabet.csv")
    nato_dict = {row.letter:row.code for (index, row) in df.iterrows()}
    try:
        result = [nato_dict[letter] for letter in word]
    except KeyError:
        print("Sorry only alphabet words, try again.")
    else:
        print(result)
