from GithubApi import GithubApi

githubapi = GithubApi("jankowalski", "jankowalski@gmail.com", "password123")

'''Creating a repository'''
githubapi.add_repo("Hello-World")

'''Push commits'''
githubapi.commit("new commit message", "827efc6d56897b048c772e7f854f42", "7d1b31e74e15cbdbc88a537ed063a0", "Hello-World")

'''Creating Pull Request'''
githubapi.pull_request("Hello-World", "user:master", "master")

'''Accepting Pull Request'''
githubapi.accept_pull_request("title", "some commit message", "73474653676", "Hello-World", "2")

'''Deleting a repository'''
githubapi.delete_repository("Hello-World")