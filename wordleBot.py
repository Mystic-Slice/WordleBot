with open('allWords.txt', 'r') as f:
    POSSIBLE_ANSWERS = [line.strip() for line in f]

wordScore = {}
charFreq = {}

def filterWords(wordList, matches):
    rejectedLetters = []
    acceptedLetters = []
    for index, match in enumerate(matches):
        letter = match[0]
        type = match[1]
        if type == 0:
            rejectedLetters.append(letter)
            
        if type == 1:
            wordList = [x for x in wordList if letter in x]
            wordList = [x for x in wordList if x[index] != letter]
            acceptedLetters.append(letter)

        if type == 2:
            wordList = [x for x in wordList if x[index] == letter]
            acceptedLetters.append(letter)

    for letter in rejectedLetters:
        if letter in acceptedLetters:
            wordList = [x for x in wordList if x.count(letter) == acceptedLetters.count(letter)]
            continue
        wordList = [x for x in wordList if letter not in x]
    return wordList


def calcCharFreq():
    charFreq.clear()
    for i in range(ord('a'), ord('z')+1):
        charFreq[chr(i)] = 0

    for word in POSSIBLE_ANSWERS:
        for char in word:
            charFreq[char] += 1

def calcWordScore():
    wordScore.clear()
    for word in POSSIBLE_ANSWERS:
        wordUnique = ''.join(set(word))
        wordScore[word] = sum([charFreq[x] for x in wordUnique])

def sortPossibleAnswers():
    POSSIBLE_ANSWERS.sort(key=lambda word: -wordScore[word])

for turn in range(6):
    calcCharFreq()
    calcWordScore()
    sortPossibleAnswers()
    print("Search Space:", len(POSSIBLE_ANSWERS))
    optimalGuess = POSSIBLE_ANSWERS[0]
    print(f'Optimal Guess: {optimalGuess}')

    otherGuesses = []
    for x in POSSIBLE_ANSWERS:
        if wordScore[x] == wordScore[optimalGuess]:
            otherGuesses.append(x)

    if len(otherGuesses) > 0:
        print('Other Recommended Guesses: ')
        print(otherGuesses)

    optimalGuess = input("Enter your guess: ")
    if optimalGuess in POSSIBLE_ANSWERS: POSSIBLE_ANSWERS.remove(optimalGuess)
    matches = input("Enter the result: ")

    if matches == '22222':
        print("Congratulations!")
        quit()

    matches = [list([optimalGuess[index], int(matches[index])]) for index in range(5)]
    POSSIBLE_ANSWERS = filterWords(POSSIBLE_ANSWERS, matches)