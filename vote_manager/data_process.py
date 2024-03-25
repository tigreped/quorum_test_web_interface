import pandas as pd

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
    legislator_info = {}
    # Load legislator names information
    for index, row in legislators.iterrows():
        leg_id = row['id']
        leg_name = row['name']
        legislator_info[leg_id] = leg_name

    for index, row in vote_results.iterrows():
        legislator_id = row['legislator_id']
        vote_type = row['vote_type']
        if legislator_id not in legislator_vote_count:
            legislator_vote_count[legislator_id] = {'id': legislator_id, 'name': legislator_info[legislator_id], 'pros': 0, 'cons': 0}
        if vote_type == 1:  # votos a favor
            legislator_vote_count[legislator_id]['pros'] += 1
        elif vote_type == 2:  # votos contra
            legislator_vote_count[legislator_id]['cons'] += 1

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
