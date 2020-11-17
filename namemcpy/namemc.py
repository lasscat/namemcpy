import time
import requests
import json
ts = time.time()
class namepy():

    def __init__(self):
        self.url = 'https://namemc.com'
        self.api_url = 'https://api.mojang.com/users/profiles/minecraft/'
        self.friend_url = 'https://api.namemc.com/profile/'
        self.like_list = 'https://api.namemc.com/server/' # + /likes

    def __version__(self):
        return "0.0.1" # returns namepy version

    def printFriendListUsername(self, player): #add a function to find a users friend my username (player) is the player you want to search the friends of
        r = requests.get(self.api_url + player + '?at=' + str(ts)) #uses mojangs api scrapes website (there uuid is the "id" part) (ts is the timestamp in unix)

        uuid_get = r.json() #creates variable then json it.

        uuid = (uuid_get['id']) # gets uuid

        url = self.friend_url + uuid + '/friends' # creating full namemc url
        friend_scrape = requests.get(url).json() # scrapes the url we just made # ^\

        for players in friend_scrape: #makes loop to print usernames
            print(players['name'])
            #returns output of the friends usernames:

    def printFriendListUuid(self, uuid):
        #namemc
        url = self.friend_url + uuid + '/friends' # creating full namemc url
        friend_scrape = requests.get(url).json() # scrapes the url we just made # ^\
        #namemc

        for players in friend_scrape: #prints the usernames inside statment
            print(players['name'])
            #returns output of the friends usernames:

    def printFriendListUuidOutputUuid(self, uuid):
        #namemc
        url = self.friend_url + uuid + '/friends' # creating full namemc url
        friend_scrape = requests.get(url).json() # scrapes the url we just made # ^\
        #namemc

        for players in friend_scrape: #prints the usernames inside statment
            print(players['uuid'])
            #returns output of the friends uuids:

    def printFriendListUsernameOutputUuid(self, player): #add a function to find a users friend my username (player) is the player you want to search the friends of
        r = requests.get(self.api_url + player + '?at=' + str(ts)) #uses mojangs api scrapes website (there uuid is the "id" part) (ts is the timestamp in unix)

        uuid_get = r.json() #creates variable then json it.

        uuid = (uuid_get['id']) # gets uuid

        url = self.friend_url + uuid + '/friends' # creating full namemc url
        friend_scrape = requests.get(url).json() # scrapes the url we just made # ^\

        for players in friend_scrape: #makes loop to print usernames
            print(players['uuid'])
            #returns output of the friends usernames:

    def areFriendsUsername(self, player1, player2): # player1 is the user you will be searching the friends list and player 2 is the player you will look in player1's friend list
        friend_list = []
        #-------getting player 1 uuid-------
        player_1_link = requests.get(self.api_url + player1 + "?at=" + str(ts)) #look at printfriendlist for what this means
        player_1_uuid_get  = player_1_link.json()
        player_1_uuid = (player_1_uuid_get['id']) # gets player 1 uuid value and stores it into the var
        #-------------------

        namemc_api_url = self.friend_url + player_1_uuid + '/friends' # gets namemc api url for player1
        response_namemc = requests.get(namemc_api_url).json()

        for friends in response_namemc:
            friend_list.append(friends['name'])

        if player2 in friend_list:#if player2 is in friends list
            print("True")
        if player2 not in friend_list:#if player2 is not in friends list
            print("false")

    def areFriendsUuid(self, uuid1, uuid2): #uuid1 is the user you will be searching the friends list and uuid2 is the player you will look in player1's friend list
        friend_list = []

        namemc_api_url = self.friend_url + uuid1 + '/friends'  # gets namemc api url for player1
        response_namemc = requests.get(namemc_api_url).json()

        for friends in response_namemc:
            friend_list.append(friends['uuid']) # adds all uuids to the list friend_list

        if uuid2 in friend_list:
            print("True")
        if uuid2 not in friend_list:
            print("false")


    def serverLikeNumber(self, server): #server list being the servers ip INCLUDE THE DOMAIN TLD
        likes = [] # creates a list so we can append all the likes to this list later
        server_api_url = self.like_list + server + '/likes'
        server_url_request = requests.get(server_api_url).json() #requests get the url from above ^ then jsons it


        for players in server_url_request:
            likes.append(players)
            #prints output of uuids

        len_likes = int(len(likes)) # len likes the list to make it a number then int it so it can be a interger
        print('The server' + server + ' Has ' + str(len_likes) + ' Likes')

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
            return False
        if namemc_verify_like_url_request==True:
            print('The player ' + username + ' is liking the server ' + server)
            return True

    def verifyLikeUuid(self, server, uuid): # same thing as username put you can search with a uuid instead of username

        #namemc api
        namemc_server_like_url = self.like_list +  server + '/likes?profile=' + str(uuid) #creates the url we will use for the api
        namemc_server_like_url_request = requests.get(namemc_server_like_url).json() # gets api
        #namemc api

        # if namemc_verify)_like_url output is false or true give response ect
        if namemc_server_like_url_request==False:
            print('The uuid ' + uuid + ' is not liking the server ' + server)
            return False
        if namemc_server_like_url_request==True:
            print('The uuid ' + uuid + ' is liking the server ' + server)
            return True
