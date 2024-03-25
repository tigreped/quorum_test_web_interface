import pandas as pd

legislator_processed = False
bill_processed = False

# Files to read under ./data directory
bills = pd.read_csv('../data/bills.csv')
legislators = pd.read_csv('../data/legislators.csv')
votes = pd.read_csv('../data/votes.csv')
vote_results = pd.read_csv('../data/vote_results.csv')

# Data structures to persist accounts in memory
legislator_vote_count = {}
bill_vote_count = {}

# Simple method to account for the legislator votes
def count_legislator_votes():
    for index, row in vote_results.iterrows():
        legislator_id = row['legislator_id']
        vote_type = row['vote_type']
        if legislator_id not in legislator_vote_count:
            legislator_vote_count[legislator_id] = {'id': legislator_id, 'pros': 0, 'cons': 0}
        if vote_type == 1:  # votos a favor
            legislator_vote_count[legislator_id]['pros'] += 1
        elif vote_type == 2:  # votos contra
            legislator_vote_count[legislator_id]['cons'] += 1
        legislator_processed = True

# Simple method to account for the bills' votes
def count_bill_votes():
    for index, row in bills.iterrows():
        bill_id = row['id']
        primary_sponsor_id = row['sponsor_id']
        verify = legislators.loc[legislators['id'] == primary_sponsor_id, 'name']
        if verify is not None and verify.values.size >= 1:
            primary_sponsor_name = verify.values[0]
        if bill_id not in bill_vote_count:
            bill_vote_count[bill_id] = {'id': bill_id, 'pros': 0, 'cons': 0, 'primary_sponsor': primary_sponsor_name}
        vote_ids = votes.loc[votes['bill_id'] == bill_id, 'id'].values
        for vote_id in vote_ids:
            vote_results_for_this_vote = vote_results.loc[vote_results['vote_id'] == vote_id]
            bill_vote_count[bill_id]['pros'] += len(vote_results_for_this_vote.loc[vote_results_for_this_vote['vote_type'] == 1])
            bill_vote_count[bill_id]['cons'] += len(vote_results_for_this_vote.loc[vote_results_for_this_vote['vote_type'] == 2])
        bill_processed = True

# Main method triggers simple tests
def simple_test():
    print(f'Legislators: \n{legislator_vote_count} *BEFORE')
    count_legislator_votes()
    print(f'Legislators: \n{legislator_vote_count} *AFTER')
    print(f'Bills: \n{bill_vote_count} *BEFORE')
    count_bill_votes()
    print(f'Bills: \n{bill_vote_count} *AFTER')
