def read_votes():
    votes = {}
    while True:
        print('Vote (or done):')
        vote = input()
        if vote == 'done':
            break
        if vote in votes:
            votes[vote] += 1
        else:
            votes[vote] = 1
    return votes

def report(votes):
    if not votes:
        print('No votes')
        return
    for name, count in votes.items():
        print(f'{name}: {count}')
    winner = max(votes, key = votes.get)
    print(f'winner: {winner}')

votes = read_votes()
report(votes)