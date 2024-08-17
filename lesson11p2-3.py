from collections import Count

def rank_choice_round(votes, candidates, eliminated):
    '''Given a set of rank ordered votes, a list of candidates and a list of
    eliminated candidates, do one round of instant run off voting. Return
    True and the candidate if there is a winner this round and False and
    "no winner" if not'''
    # Handle first round case
    if len(candidates) == 0:
        # read all votes for all rounds and set candidate counts to zero
        for vote in votes:
            for vround in vote:
                if vround not in candidates:
                    candidates[vround] = 0
    
    # TODO see if current round votes produce a winner
    
    # TODO if no winner, eliminate a candidate and return no winner
    
    return(False, "no winner")


# Example
votes = [
    ["A", "B", "C"],
    ["B", "A", "C"],
    ["C", "B", "A"],
    ["C", "A", "B"],
]

election_done = False
candidates = Count()
eliminated = []
while not election_done:
    election_done, winner = rank_choice_round(votes, candidates, eliminated)
print("Winner:", winner)
