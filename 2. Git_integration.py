# Program to demostrate integration with GitHUb to fetch the 
# details fo users who created Pull requests (Active) on Kubernetes Github Repo.

import requests

# url to fetch the pull requests from the GitHub API
url = f'https://api.github.com/repos/kubernetes/kubernetes/pulls'

# Make a GET request to fetch pull requests data from the GitHub API
response = requests.get(url) 

# Only if the response is successfull 
if response.status_code == 200:
    # Convert the JSON response to a dictionary
    pull_requests = response.json()

    # create an empty dictionary to store PR creators and their counts
    pr_creator = {}

    # Iterate through each pull request and extract the creator's name
    for pull in pull_requests:
        creator = pull['user']['login']
        if creator in pr_creator:
            pr_creator[creator] += 1
        else:
            pr_creator[creator] = 1

    # Display the dictionary of PR creators and their counts
    print("PR Creators and Counts:")
    for creator, count in pr_creator.items():
        print(f"{creator}: {count} PR(s)")
else:
    print(f"Failed to detch data. Status code: {response.status_code}")