#generate list of valid words
def GenList(inString):
  wordDict = open("words_alpha.txt", "r") #read dictionary
  outList = []
  for word in wordDict:
    word = word.strip() #pull off newline
    if ContainsOnlyValidLetters(word, inString):
      outList += [word]
  return outList

#checks if string 'word' only contains characters in string 'inString'
def ContainsOnlyValidLetters(word, inString):
  for c in word:
    if c not in inString:
      return False
  return True

def CullList(possibleWords, inStringSplit):
  outList = []
  for word in possibleWords:
    if (CullListHelper(word, inStringSplit)):
      outList += [word]
  return outList

def CullListHelper(word, inStringSplit):
  i = 0
  j = 1
  while j < len(word):
    if (word[i] == word[j]): #if duplicate character, remove
      return False
    for edge in inStringSplit: #for each edge,
      if word[i] in edge and word[j] in edge: #if both i and j on same edge, remove
        return False
    i += 1
    j += 1
  return True

def IsPangram(word, alphabet):
    for char in alphabet:
        if char not in word:
            return False
    return True

def DetermineSolution(words, alphabet, maxvalue = 5):
  i = 1
  outList = []
  while i <= maxvalue: #while we haven't hit the max,
    print("Checking combinations of length", i , '...')
    possibleCombinations = GenerateCombinations(words, i) #get combos
    for combo in possibleCombinations: #for all combos,
      comboAsString = ''.join(combo)
      if IsPangram(comboAsString, alphabet): #check if pangram
        outList += [combo]
    if(outList): #if we've found a solution,
      return outList
    i+=1 
  return ['OH NO!']

#generate all length i sets of words
def GenerateCombinations(array, tuple_length, prev_array=[]):
    if len(prev_array) == tuple_length:
        return [prev_array]
    combs = []
    for i, val in enumerate(array):
        if (val == 'downright' and prev_array and prev_array[-1] == 'undaunted'):
          print('hey')
        if((prev_array and val[0] == prev_array[-1][-1]) or (not prev_array)):
          prev_array_extended = prev_array.copy()
          prev_array_extended.append(val)
          combs += GenerateCombinations(array[i+1:], tuple_length, prev_array_extended)
    return combs

def main(inString, maxValue):
  inString = inString.lower() #set to lowercase

  inStringNoComma = inString.replace(',','') #cut out commas
  possibleWords = GenList(inStringNoComma) #generate list of words with valid characters
  #print(possibleWords)

  inStringSplit = inString.split(',') #split the input into edges
  possibleWords = CullList(possibleWords, inStringSplit)
  #print(possibleWords)

  solutions = DetermineSolution(possibleWords, inStringNoComma, maxValue)
  for solves in solutions:
    print(solves)
  return solutions

main('DWG,UOT,ENI,HAR', 5)

# 1: receive input
# 2: generate list of words containing these letters
# 3: split input
# 4: cull list by rules (no repeat letter, no adjacent letters)
# 5: select minimum sets that contain all letters
# 6: identify which sets, if any, can be traversed
# 7: either return or return to 5, depending on success in 6