sentance = input("Enter youre text: ")
#sentance is a list becouse it storing more than one character
#creating dictionary to count each vowel
vowel = {
    "a":0,
    "e":0,
    "o":0,
    "i":0,
    "u":0
}
for character in sentance:
   print(character)
   #in is a keyword that checks if a key exists in a viarable
   if character in vowel :
      vowel[character] += 1 

print(vowel)