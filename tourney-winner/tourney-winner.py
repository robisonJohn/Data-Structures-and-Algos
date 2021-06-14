# Solution runs in O(n) time | O(k) space - where
# n is the number of competitions and k is the 
# number of teams

'''
Initialize the current best team as an empty string
Create a scores matrix that assigns the curent best team to a value of zero
The enumerate argument unpacks a list object such that idx is the index of iteration and competition is the value at index idx
We can then let result equal the value of the results list at index idx
Similarly, we can let homeTeam, awayTeam equal the value of the tuple value returned by competition at that given index
If result is 1, set winning team equal to home team; else, set winning team to away team
We can then call the updateScores function using winningTeam (the result), 3 (the total amount of points), and scores (the scores matrix)
The update scores will then add the winningTeam to the dictionary, if it is not already there, and then update the score by 3 points
Then, if the scores of winning team is greater than the scores of the current best team, let current best team equal to winning team
We repeat this process until we have iterated through both objects
We may then return the value of the current best team upon exiting the for loop
'''

HOME_TEAM_WON = 1

def tournamentWinner(competitions, results):
    currentBestTeam = ""
    scores = {currentBestTeam: 0}

    for idx, competition in enumerate(competitions):
        result = results[idx]
        homeTeam, awayTeam = competition

        winningTeam = homeTeam if result == HOME_TEAM_WON else awayTeam

        updateScores(winningTeam, 3, scores)

        if scores[winningTeam] > scores[currentBestTeam]:
            currentBestTeam = winningTeam
    
    return currentBestTeam

def updateScores(team, points, scores):
    if team not in scores:
        scores[team] = 0

    scores[team] += points