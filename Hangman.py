class Hangman:

    from words import words


    def valid_word(words):
        import random
        word = random.choice(words)
        while '-' in word or ' ' in word:
            word = random.choice(words)
        return word.upper()
    
    def play_hangman(word):
        import string
        from hangman_functions import find_index
        length = len(word)
        guess_word = "_"*length
        print(f"The word is {length} letters long")

        used_alphabets = set()
        unused_alphabets = set(string.ascii_uppercase)
        while guess_word != word:
            alphabet = input(f"\n You have used the following words: {used_alphabets} \n Enter an alphabet {guess_word}: ").upper()
            if alphabet in used_alphabets:
                print("Sorry you have already guessed that letter")
            elif alphabet in unused_alphabets:
                unused_alphabets.remove(alphabet)
                used_alphabets.add(alphabet)
                if alphabet in word:
                    indices = find_index(alphabet, word)
                    for ind in indices:
                        guess_word = guess_word[:ind] + alphabet + guess_word[ind+1:]
                else:
                    print("Sorry the letter is not in the word to be guessed.")
            else:
                print("This is not a letter! ")
        if guess_word == word:
            print(f"\n Congrats! You have guessed the word: {word}".upper())
        

    word_to_be_guessed = valid_word(words)
    play_hangman(word_to_be_guessed)