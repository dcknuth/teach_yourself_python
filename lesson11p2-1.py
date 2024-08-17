# Attempt from chat-bot
def get_winner(candidate_votes):
    while True:
        # Count the first preferences
        first_choices = {candidate: 0 for candidate in candidate_votes.keys()}
        for votes in candidate_votes.values():
            if len(votes) > 0:
                first_choices[votes[0]] += 1
        
        # Check if any candidate has a majority
        for candidate, votes in first_choices.items():
            if votes > len(candidate_votes) / 2:
                return candidate
        
        # Find the candidate with the fewest votes
        min_votes = min(first_choices.values())
        candidates_with_min_votes = [candidate for candidate, votes in first_choices.items() if votes == min_votes]
        
        # Eliminate the candidate with the fewest votes
        for candidate in candidates_with_min_votes:
            del candidate_votes[candidate]
        
        # Redistribute votes of the eliminated candidate
        for votes in candidate_votes.values():
            for candidate in candidates_with_min_votes:
                if candidate in votes:
                    votes.remove(candidate)
    
    return None


def rank_choice_voting(candidates, votes):
    candidate_votes = {candidate: [] for candidate in candidates}
    for vote in votes:
        for i, candidate in enumerate(vote):
            if candidate in candidates:
                candidate_votes[candidate].append(vote[i:])
                break
    
    winner = get_winner(candidate_votes)
    return winner


# Example usage
candidates = ["A", "B", "C"]
votes = [
    ["A", "B", "C"],
    ["B", "A", "C"],
    ["C", "B", "A"],
    ["C", "A", "B"],
]

winner = rank_choice_voting(candidates, votes)
print("Winner:", winner)
