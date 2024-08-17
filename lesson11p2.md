# Python Lesson 11 Part 2
More debugging and practice. This has a lot of code sections, they are each in a different file in the repo to make it easy to start a section in the IDE and debug just that part.

Writing code accounts for 90 percent of programming and debugging is the other 90 percent. The Spider IDE includes great debugging tools for us as does Python itself. In a view of the future, let’s ask ChatGPT to provide us with a rank-choice voting program. Then let’s debug it (because, of course, it will not work).
```
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
```
Let’s not be too hard on the chat bot. You will see tons of stuff that does not work from colleagues, internet examples, old code from who knows when, our own code and chat bots. The error we see when we try to run this is TypeError: unhashable type: 'list' from this line of code
```
first_choices[votes[0]] += 1
```
In the file window, if you click between the line number and the program text, you can set (or clear) a 'breakpoint'. If you click on the line number given in the Console just above the error, Spyder will put you on the corresponding line in the file pane. Put a break point on that line. If we run the program with \<Ctrl\>+\<F5\>, it will run in debug mode and stop when the program gets to the breakpoint. When it stops, we can see the values for things using the Variable Explorer tab. It looks like votes is a list of lists with only one list in it. The intention was probably a list of candidates so that votes[0] would produce ‘A’, which is hashable, but instead there is an extra set of [ ]. If we keep following back where the data originates, we see it comes from the candidate_votes variable, which also looks to have an extra set of [ ]s in its values, then to the dictionary comprehension in rank_choice_voting function and filled via the line with "append". Let's put a break point on that line so we can see what happens there and then reset with \<Shift\>+\<Ctrl\>+\<F12\> to stop the debug run and then \<Ctrl\>+\<F5\> to debug again. It seems to append a list slice, which will be a new list. Maybe it meant to just append the candidate? Let’s change from .append(vote[i:]) to .append(candidate) and see what happens. We will need to stop debugging again and then run the program with F5.

This is bad enough to defy an easy fix, but it did give us an example to use the debugger. Let’s move to doing this ourselves in a few steps. First we just make a shell of what we think we will have to do.
```
from collections import Count

def rank_choice_round(votes, candidates, eliminated):
    '''Given a set of rank ordered votes, a list of candidates and a list of
    eliminated candidates, do one round of instant run off voting. Return
    True and the candidate if there is a winner this round and False and
    "no winner" if not'''
    # TODO handle first round case
    
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
candidates = []
eliminated = []
while not election_done:
    election_done, winner = rank_choice_round(votes, candidates, eliminated)
print("Winner:", winner)
```
In Spider, we will already see two things. We get a warning for the first line that we import something we don’t use. We also get check marks on lines where we have put “TODO”. Let’s go one more step and take care of the first TODO and change our candidates variable from a list to a Counter.
```
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
```
We know this will not work since we only took care of one part, but let's put a break point on the second to last line and see if this will just load the candidates. We find that it does not even start and gives
ImportError: cannot import name 'Count' from 'collections'
We need to change Count to Counter in both places we use it. After that we can do a debug run (\<Ctrl\>+\<F5\>) and then run the rank_choice_round() once with \<Ctrl\>+\<F10\>. After that, in the Variable Explorer tab, we can see that candidates is now size 3 and if we double click that variable in the Variable Explorer view we see that each candidate has had their count set to 0. Good. Let’s stop our debug run with \<Ctrl\>+\<Shift\>+\<F12\> and fill in the next TODO.
```
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
    
    # Do the current round of votes
    for vote in votes:
        # make sure this voter has a next candidate
        while len(vote) > 0:
            # Get that next candidate and remove from the list
            candidate = vote.pop(0)
            # See if the candidate has already been eliminated
            if candidate in eliminated:
                # Go to the next if so
                continue
            # Else we can count that vote and go to the next voter
            candidates[candidate] += 1
            break
    
    # TODO see if there is a winner
    
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
```
We filled in the code to count a round of votes and added a TODO to see if there is a winner. Let's clear the previous break point and put one at the start of the for loop we just added. We can start a debug run, step through and see that this seems to be working.
As we head to the next TODO, we have a problem or maybe just a choice to make. Do you win if you get exactly 50% or do you need >50%? For social harmony, let’s say you need >50%, but I could see many cases where you just need an OK answer and if we wanted to make this into a module, it should probably be an option that you could set. For now >50%.
```
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
    
    # Do the current round of votes
    for vote in votes:
        # make sure this voter has a next candidate
        while len(vote) > 0:
            # Get that next candidate and remove from the list
            candidate = vote.pop(0)
            # See if the candidate has already been eliminated
            if candidate in eliminated:
                # Go to the next if so
                continue
            # Else we can count that vote and go to the next voter
            candidates[candidate] += 1
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
```
To see how this works, we again: quit our last debug section and clear the old breakpoint, set a new breakpoint at the start of our new section and then start a new debug session. If we want to jump to the next time the program sees a breakpoint, we can press \<Ctrl\>+\<F12\> (no shift). The part we added seems to be working, so we can stop our debug session.
As we head to the next TODO, there is another choice to make. If there is a tie for last, what should we do? In this fake election, this choice either results in a win for C or a two way tie in the election in round two. Wait, a two way win should not happen, so there is a logic error in our program. We seem to have two issues. First, we should not just count all the votes, we should change who each voter voted for at each step, so we would need to check for votes of eliminated candidates and move those votes to the next preferred candidate for that particular voter. To actually get a winner in this election, this also forces us to drop all tied for last candidates in each round. Let’s see if we can fix the first issue first and redo the voting section.
```
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
```
Using a breakpoint and debug run to look at the added reset and changed voting round, things are looking OK. Let’s add the elimination of all last place candidates.
```
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
    
    # If no winner, eliminate a candidate and return no winner
    results = sorted(candidates.items(), key=lambda x: x[1])
    # Get the lowest number of votes after converting to a list and sorting
    low_vote = results[0][1]
    while results[0][1] == low_vote:
        candidate, votes = results.pop(0)
        # Add to list of those eliminated
        eliminated.append(candidate)
        # Remove from the list of viable candidates
        del candidates[candidate]
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
```
Again, we can set a breakpoint on the part we added step though in a debug session and it again looks good. Not as many errors as there could be, but still pretty good practice with the debugger.

Question: Should we have abandoned our start from the chat-bot so quickly or should we have tried harder to debug that code?

[Python Lesson 12](lesson12.md) - CSV and JSON