""" Using randomly selected words from nouns, verbs, adjectives, prepositions and adverbs, 
generate and display a poem with structure inspired by Cliﬀord Pickover """


import random

nouns_list = ["fossil", "horse", "aardvark", "judge", "chef", "mango", "extrovert", "gorilla"]
verbs_list = ["kicks", "jingles", "bounces", "slurps", "meows", "explodes", "curdles"]
adjectives_list = ["furry", "balding", "incredulous", "fragrant", "exuberant", "glistening"]
prepositions_list = ["against", "after", "into", "beneath", "upon", "for", "in", "like", "over", "within"]
adverbs_list = ["curiously", "extravagantly", "tantalizingly", "furiously", "sensuously"]


nouns = random.choices(nouns_list, k=3)
verbs = random.choices(verbs_list, k=3)
adjectives = random.choices(adjectives_list, k=3)
prepositions = random.choices(prepositions_list, k=3)
adverb = random.choice(adverbs_list)
vowels = ["a", "e", "i", "o", "u"]

def article(word):
    if word[0] in vowels:
        return "An"
    return "A"

print(f"{article(adjectives[0])} {adjectives[0]} {nouns[0]}")

print("\n")

print(f"{article(adjectives[0])} {adjectives[0]} {nouns[0]} {verbs[0]} {prepositions[0]} the {adjectives[1]} {nouns[1]}")
print(f"{adverb}, the {nouns[0]} {verbs[1]}")
print(f"the {nouns[1]} {verbs[2]} {prepositions[1]} {article(adjectives[2]).lower()} {adjectives[2]} {nouns[2]}")