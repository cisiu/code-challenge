import requests
import json

class GithubApi(object):
    URL = 'https://api.github.com'

    create_repo_payload = {
        "name": "repo_name",
        "description": "This is your test repository"
    }

    pull_request_payload = {
        "title": "Amazing new feature",
        "body": "Please pull this in!",
        "head": "user:master",
        "base": "master"
    }
    commit_payload = {
        "message": "my commit message",
        "author": {
            "name": "Scott Chacon",
            "email": "ssss@gmail.com",
            "date": "2008-07-09T16:13:30+12:00"
        },
        "parents": [
            "7d1b31e74ee336d15cbd21741bc88a537ed063a0"
        ],
        "tree": "827efc6d56897b048c772eb4087f854f46256132",
        "signature": "-----BEGIN PGP SIGNATURE-----"
    }

    merge_pull_request_payload = {
        "commit_title": "title",
        "commit_message": "meassage",
        "sha": "12345"
    }

    def __init__(self, git_user, login, passwd):
        self.session = requests.Session()
        self.session.headers.update({'User-Agent': 'Custom user agent'})

        self.user = git_user
        self.login = login
        self.passwd = passwd

    '''POST / user / repos'''
    def add_repo(self, new_repo_name):
        self.create_repo_payload["name"]=new_repo_name
        self.payld = self.create_repo_payload
        self.payld = json.dumps(self.payld)
        self.new_repo = self.session.post(url=self.URL+'/{}/repos'.format(self.user),
                                            data=self.payld, auth=(self.login, self.passwd))
        if self.new_repo!=201:
            print "FAIL, repo not created!!!"

    '''POST / repos /:owner /:repo / pulls'''
    def pull_request(self, repo_name, head, base):
        self.create_repo_payload["name"] = repo_name
        self.create_repo_payload["head"] = head
        self.create_repo_payload["base"] = base
        self.payld = self.create_repo_payload
        self.payld = json.dumps(self.payld)
        self.new_request = self.session.post(url = self.URL+'/repos/{}/{}/pulls'.format(self.user,repo_name),
                                             data=self.payld, auth=(self.login, self.passwd))
        if self.new_request.status_code != 201:
            print "FAIL, pull request not raised!!!"

    '''DELETE / repos /:owner /:repo'''
    def delete_repository(self, repo_name):
        self.deleted_repo = self.session.delete(self.URL+'/repos/{}/{}'.format(self.user, repo_name))
        if self.deleted_repo.status_code!=204:
            print "FAIL, repo not deleted!!!"

    '''PUT / repos /:owner /:repo / pulls /:number / merge'''
    def accept_pull_request(self, commmit_title, commit_message, sha, repo_name, pull_nr):
        self.merge_pull_request_payload["commit_title"] = commmit_title
        self.merge_pull_request_payload["commit_message"] = commit_message
        self.merge_pull_request_payload["sha"] = sha
        self.payld = json.dumps(self.merge_pull_request_payload)
        self.accept_pull_req = self.session.post(url=self.URL + '/repos/{}/{}/pulls/{}/merge'.format(self.user,
                                                repo_name, pull_nr), data=self.payld, auth=(self.login, self.passwd))
        if self.accept_pull_req.status_code!=204:
            print "FAIL, repo not deleted!!!"

    ''' POST / repos /:owner /:repo / git / commits'''
    def commit(self, message, tree, parents, repo_name):
        self.commit_payload["message"] = message
        self.commit_payload["tree"] = tree
        self.commit_payload["parents"] = parents
        self.payld = json.dumps(self.commit_payload)
        self.commit_request = self.session.post(url = self.URL+'/repos/{}/{}/git/commits'.format(self.user,repo_name),
                                                data=self.payld, auth=(self.login, self.passwd))
        if self.commit_request.status_code!=201:
            print "FAIL, commit not succesfull!!!"



