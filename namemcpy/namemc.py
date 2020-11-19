import time
import requests
import json
from bs4 import BeautifulSoup
ts = time.time()

class namepy():

    def __init__(self):
        self.url = 'https://namemc.com'
        self.api_url = 'https://api.mojang.com/users/profiles/minecraft/'
        self.friend_url = 'https://api.namemc.com/profile/'
        self.like_list = 'https://api.namemc.com/server/' # + /likes
        self.uuid_api_url = 'https://sessionserver.mojang.com/session/minecraft/profile/'
        self.skin_url = 'https://namemc.com/skin/'

    def __version__(self):
        return "0.0.1" # returns namepy version

    def printFriendListUsernameOutputUuid(self, player): #add a function to find a users friend my username (player) is the player you want to search the friends of

        friend_list = []

        r = requests.get(self.api_url + player + '?at=' + str(ts)).json() #uses mojangs api scrapes website (there uuid is the "id" part) (ts is the timestamp in unix)

        uuid = (r['id']) # gets uuid

        url = self.friend_url + uuid + '/friends' # creating full namemc url
        friend_scrape = requests.get(url).json() # scrapes the url we just made # ^\

        for players in friend_scrape: #makes loop to print usernames
            friend_list.append(players['uuid'])
            #returns output of the friends usernames:
        print(friend_list)

    def printFriendListUuidOutputUsername(self, uuid):

        friend_list = []

        #namemc
        friend_scrape = requests.get(self.friend_url + uuid + '/friends').json() # scrapes the url we just made # ^\
        #namemc

        for players in friend_scrape: #prints the usernames inside statment
            friend_list.append(players['name'])
            #returns output of the friends usernames:
        return  friend_list

    def printFriendListUuidOutputUuid(self, uuid):
        friend_list = []
        #namemc
        friend_scrape = requests.get(self.friend_url + uuid + '/friends').json() # scrapes the url we just made # ^\
        #namemc

        for players in friend_scrape: #prints the usernames inside statment
            friend_list.append(players['uuid'])
            #returns output of the friends uuids:
        return  friend_list

    def printFriendListUsernameOutputUsername(self, player): #add a function to find a users friend my username (player) is the player you want to search the friends of

        friend_list = []

        r = requests.get(self.api_url + player + '?at=' + str(ts)).json() #uses mojangs api scrapes website (there uuid is the "id" part) (ts is the timestamp in unix)

        uuid = (r['id']) # gets uuid

        friend_scrape = requests.get(self.friend_url + str(uuid) + '/friends').json() # scrapes the url we just made # ^\

        for players in friend_scrape: #makes loop to print usernames
            friend_list.append(players['name'])
            #returns output of the friends usernames:
        return  friend_list

    def areFriendsUsername(self, player1, player2): # player1 is the user you will be searching the friends list and player 2 is the player you will look in player1's friend list
        friend_list = []
        #-------getting player 1 uuid-------
        player_1_link = requests.get(self.api_url + player1 + "?at=" + str(ts)).json() #look at printfriendlist for what this means
        player_1_uuid = (player_1_link['id']) # gets player 1 uuid value and stores it into the var
        #-------------------

        response_namemc = requests.get(self.friend_url + player_1_uuid + '/friends').json()

        for friends in response_namemc:
            friend_list.append(friends['name'])

        if player2 in friend_list:#if player2 is in friends list
            return True
        if player2 not in friend_list:#if player2 is not in friends list
            return False

    def areFriendsUuid(self, uuid1, uuid2): #uuid1 is the user you will be searching the friends list and uuid2 is the player you will look in player1's friend list
        friend_list = []

        response_namemc = requests.get(self.friend_url + uuid1 + '/friends').json()

        for friends in response_namemc:
            friend_list.append(friends['uuid']) # adds all uuids to the list friend_list

        if uuid2 in friend_list:
            return True
        if uuid2 not in friend_list:
            return False


    def serverLikeNumber(self, server): #server list being the servers ip INCLUDE THE DOMAIN TLD
        likes = [] # creates a list so we can append all the likes to this list later
        server_api_url = self.like_list + server + '/likes'
        server_url_request = requests.get(server_api_url).json() #requests get the url from above ^ then jsons it


        for players in server_url_request:
            likes.append(players)
            #prints output of uuids

        len_likes = int(len(likes)) # len likes the list to make it a number then int it so it can be a interger
        return len_likes

    def verifyLikeUsername(self, server, username):

        # -------getting username to uuid-------
        username_2_uuid_url = self.api_url + username + '?at=' + str(ts)
        username_2_uuid_request = requests.get(username_2_uuid_url).json()
        # -------------------

        #namemc api
        namemc_verify_like_url = self.like_list + server + '/likes?profile=' + str(username_2_uuid_request)
        namemc_verify_like_url_request = requests.get(namemc_verify_like_url).json() # will give a output of true or false true being is liking the server and false being the player is not liking the server
        #namemc api

        #if namemc_verify)_like_url output is false or true give response ect
        if namemc_verify_like_url_request==False:
            print('The player ' + username + ' is not liking the server ' + server)
            return True
        if namemc_verify_like_url_request==True:
            print('The player ' + username + ' is liking the server ' + server)
            return False

    def verifyLikeUuid(self, server, uuid): # same thing as username put you can search with a uuid instead of username

        #namemc api
        namemc_server_like_url_request = requests.get(self.like_list +  server + '/likes?profile=' + str(uuid)).json() # gets api
        #namemc api

        # if namemc_verify)_like_url output is false or true give response ect
        if namemc_server_like_url_request==False:
            return False
        if namemc_server_like_url_request==True:
            return True

    def usernameToUuid(self, username):
        # -------getting username to uuid-------
        username_2_uuid_url = requests.get(self.api_url + username + '?at=' + str(ts)).json()
        username_2_uuid = (username_2_uuid_url['id'])
        # -------------------
        return username_2_uuid

    def uuidToUsername(self, uuid):

        # -------getting uuid to username-------
        username_2_uuid_url = requests.get(self.uuid_api_url + uuid).json()
        username_2_uuid = (username_2_uuid_url['name'])
        # -------------------
        return username_2_uuid

    def skinUsers(self, skinid): # some test package not using namemcs api we have to scrape
        """Find all users with the skinid you entered."""

        skin_users_list = []

        skin_link = requests.get(self.skin_url + skinid)# scrapes link then requests get it

        soup = BeautifulSoup(skin_link.content, 'html.parser') #beatuiful soups the request var we made then html parse it (var holds are the data from the website)

        """"extracing info (via class)"""
        username_box_result = soup.find_all('div', class_='card-body player-list py-2') # find everything under div and the class for the usernames are stored

        for results in username_box_result: # for things in usernameboxreslt
            for usernames in results.find_all('a', href=True): # this just sorts everything to href libary which we need to search the naems in
                skin_users_list.append(usernames.text) # adds all names to list

        if ValueError: # if no one using skin returns false
            return False # false meaning no one is using the skin

        else: #if no error do this

            skin_users_list.remove('…') # removes something that is not a name

            return skin_users_list # returns

    def getSkinTags(self, skinid):
        """gets skin tags on namemc"""
        empty_tags = [] # for refrence at end
        tags = [] # list we will be storing the tags in

        skin_link = requests.get(self.skin_url + skinid) # get link
        soup = BeautifulSoup(skin_link.content, 'html.parser') #parses html

        tag_box_result = soup.find_all('div', class_='card-body text-center py-1') # stripen down list

        for tag in tag_box_result:
            for each_tag in tag.find_all(href=True): #stripen down list to just tags
                tags.append(each_tag.text)

            return tags

        if tags == empty_tags:
            return False #returns false if there are no tags

    def getSkinNumber(self, skinid):
        """ gets how many users are wearing a certain skin """

        user_list = []

        skin_link = requests.get(self.skin_url + skinid)
        soup = BeautifulSoup(skin_link.content, 'html.parser')

        username_box_result = soup.find_all('div', class_='card-body player-list py-2') # find everything under div and the class for the usernames are stored\
        for results in username_box_result:  # for things in usernameboxreslt
            for usernames in results.find_all('a', href=True):  # this just sorts everything to href libary which we need to search the naems in
                user_list.append(usernames.text)  # adds all names to list
                number = len(user_list) # lens the list for all users


        return number #returns the number value
