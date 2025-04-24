# Write your solution here
import random

class WordGame():
    def __init__(self, rounds: int):
        self.wins1 = 0
        self.wins2 = 0
        self.rounds = rounds

    def round_winner(self, player1_word: str, player2_word: str):
        # determine a random winner
        return random.randint(1, 2)

    def play(self):
        print("Word game:")
        for i in range(1, self.rounds+1):
            print(f"round {i}")
            answer1 = input("player1: ")
            answer2 = input("player2: ")

            if self.round_winner(answer1, answer2) == 1:
                self.wins1 += 1
                print("player 1 won")
            elif self.round_winner(answer1, answer2) == 2:
                self.wins2 += 1
                print("player 2 won")
            else:
                pass # it's a tie

        print("game over, wins:")
        print(f"player 1: {self.wins1}")
        print(f"player 2: {self.wins2}")

class LongestWord(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)

    def round_winner(self, word1, word2):
        if len(word1) != len(word2):
            return 1 if len(word1) > len(word2) else 2

class MostVowels(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)

    def round_winner(self, word1, word2):
        vowels = set("aeiouAEIOU")
        count1 = sum(1 for ch in word1 if ch in vowels)
        count2 = sum(1 for ch in word2 if ch in vowels)
        if count1 != count2:
            return 1 if count1 > count2 else 2

class RockPaperScissors(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)

    def round_winner(self, word1, word2):
        judge = {"rock": "scissors", "scissors": "paper", "paper": "rock"}
        res = {1, 2}
        
        if word1 not in judge or (word2 in judge and word2 != judge[word1]):
            res.remove(1)
        if word2 not in judge or (word1 in judge and word1 != judge[word2]):
            res.remove(2)
        if res:
            return res.pop()
