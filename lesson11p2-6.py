from collections import Counter

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
    else:
        # reset all the counts to zero
        for candidate in candidates.keys():
            candidates[candidate] = 0
    
    # Do the current round of votes
    for vote in votes:
        # make sure this voter has a next candidate
        while len(vote) > 0:
            # Check if this voters first choice has been eliminated
            if vote[0] in eliminated:
                # Remove and go to the next if so
                vote.pop(0)
                continue
            # Else we can count that vote and go to the next voter
            candidates[vote[0]] += 1
            break
    
    # See if there is a winner
    votes_to_win = len(votes) // 2 + 1
    for candidate in candidates.keys():
        if candidates[candidate] >= votes_to_win:
            return(True, candidate)
    
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
candidates = Counter()
eliminated = []
while not election_done:
    election_done, winner = rank_choice_round(votes, candidates, eliminated)
print("Winner:", winner)