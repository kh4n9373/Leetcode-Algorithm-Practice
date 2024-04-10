class Solution:
    def deckRevealedIncreasing(deck):
        deck.sort()
        res = [0]*len(deck)
        simulation = [i for i in range(len(deck))]
        for n in deck:
            i = simulation.pop(0)
            res[i] = n
            if simulation:
                simulation.append(simulation.pop(0))
        return res