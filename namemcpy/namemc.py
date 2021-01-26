"""
MIT License

Copyright (c) 2020 Luke Lass

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import time
import requests
import json
from bs4 import BeautifulSoup
ts = time.time() # module so I can get unix time for the mojang api

class namepy():

    def __init__(self):
        """pretty much every variable for links for api ect"""
        self.url = 'https://namemc.com'
        self.api_url = 'https://api.mojang.com/users/profiles/minecraft/'
        self.friend_url = 'https://api.namemc.com/profile/'
        self.like_list = 'https://api.namemc.com/server/' # + /likes
        self.uuid_api_url = 'https://sessionserver.mojang.com/session/minecraft/profile/'
        self.skin_url = 'https://namemc.com/skin/'
        self.cape_url = 'https://namemc.com/cape/'
        self.user_profile_url = 'https://namemc.com/profile/'

    def __version__(self):
        """returns version number"""
        return "1.4.0" # returns namepy version

    def printFriendList(self, playerInput=False, uuidInput=False, output=False):  # add a function to find a users friend my username (player) is the player you want to search the friends of
        "print friends list search by username and the ouput being username"
        if isinstance(playerInput, str):  # if playerinput is a bool or a string then
            if output == 'username' or output == 'player' or output == 'uuid':  # just to make sure that the player entered or spelled the output thing right
                friend_list = []

                r = requests.get(self.api_url + playerInput + '?at=' + str(ts)).json()  # uses mojangs api scrapes website (there uuid is the "id" part) (ts is the timestamp in unix)

                uuid = (r['id'])  # gets uuid

                friend_scrape = requests.get(self.friend_url + str(uuid) + '/friends').json()  # scrapes the url we just made # ^\

                for players in friend_scrape:
                    if output == 'uuid':
                        friend_list.append(players['uuid'])  # if output or player said uuid just prints all uuids and appends to list
                    if output == 'username' or output == 'player':
                        friend_list.append(players['name'])  # if player said output username appends list
                return friend_list

        if isinstance(uuidInput, str):
            if output == 'username' or output == 'player' or output == 'uuid':
                friend_scrape = requests.get(self.friend_url + str(uuidInput) + '/friends').json()  # scrapes the url we just made # ^\

                for players in friend_scrape:
                    if output == 'uuid':
                        friend_list.append(players['uuid'])  # if output or player said uuid just prints all uuids and appends to list
                    if output == 'username' or output == 'player':
                        friend_list.append(players['name'])  # if player said output username appends list
                    return friend_list

    def areFriends(self, uuid1=False, uuid2=False, username1=False, username2=False):  # player1 is the user you will be searching the friends list and player 2 is the player you will look in player1's friend list
        """find if a user is friends by username"""

        friend_list = []

        if isinstance(username1, str) and isinstance(username2, str):
            # -------getting player 1 uuid-------
            player_1_link = requests.get(self.api_url + username1 + "?at=" + str(ts)).json()  # look at printfriendlist for what this means
            player_1_uuid = (player_1_link['id'])  # gets player 1 uuid value and stores it into the var
            # -------------------
            response_namemc = requests.get(self.friend_url + player_1_uuid + '/friends').json()

        if isinstance(uuid1, str) and isinstance(uuid2, str):
            response_namemc = requests.get(self.friend_url + uuid1 + '/friends').json()

        for friends in response_namemc:

            if isinstance(uuid1, str) and isinstance(uuid2, str):
                friend_list.append(friends['uuid'])

            if isinstance(username1, str) and isinstance(username2, str):
                friend_list.append(friends['name'])

        if isinstance(uuid1, str) and (uuid2, str):
            print(friend_list)
            if uuid2 in friend_list:  # if player2 is in friends list
                return True

            if uuid2 not in friend_list:  # if player2 is not in friends list
                return False

        if isinstance(username1, str) and isinstance(username2, str):

            if username2 in friend_list:  # if player2 is in friends list
                return True

            if username2 not in friend_list:  # if player2 is not in friends list
                return False


    def serverLikeNumber(self, server): #server list being the servers ip INCLUDE THE DOMAIN TLD
        """get the server like number"""

        likes = [] # creates a list so we can append all the likes to this list later
        server_url_request = requests.get(self.like_list + server + '/likes').json() #requests get the url from above ^ then jsons it


        for players in server_url_request:
            likes.append(players)
            #prints output of uuids

        len_likes = int(len(likes)) # len likes the list to make it a number then int it so it can be a interger
        return len_likes

    def verifyLike(self, server, uuid=False, username=False):
        """verify like by username"""

        if isinstance(username, str):
            # -------getting username to uuid-------
            username_2_uuid_request = requests.get(self.api_url + username + '?at=' + str(ts)).json()
            player2uuid = (username_2_uuid_request['id'])

            namemc_verify_like_url = self.like_list + server + '/likes?profile=' + str(player2uuid)
            namemc_verify_like_url_request = requests.get(namemc_verify_like_url).json()  # will give a output of true or false true being is liking the server and false being the player is not liking the server

        if isinstance(uuid, str):
            namemc_verify_like_url = self.like_list + server + '/likes?profile=' + str(input)

            namemc_verify_like_url_request = requests.get(namemc_verify_like_url).json()  # will give a output of true or false true being is liking the server and false being the player is not liking the server
            # namemc api
        if namemc_verify_like_url_request == False:
            return False
        if namemc_verify_like_url_request == True:
            return True
            # if namemc_verify)_like_url output is false or true give response ect

    def usernameToUuid(self, username):
        """username to uuid"""

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

        if tags == empty_tags: # maybe if tags == [] NOT SURE THOUGH
            return False #returns false if there are no tags

    def getSkinNumber(self, skinid):
        """ gets how many users are wearing a certain skin """

        user_list = []

        skin_link = requests.get(self.skin_url + skinid)
        soup = BeautifulSoup(skin_link.content, 'html.parser')

        username_box_result = soup.find_all('div', class_='card-body player-list py-2') # find everything under div and the class for the usernames are stored
        for results in username_box_result:  # for things in usernameboxreslt
            for usernames in results.find_all('a', href=True):  # this just sorts everything to href libary which we need to search the naems in
                user_list.append(usernames.text)  # adds all names to list
                
        return len(user_list) #returns the number value

    def getCapeUsers(self, capeid):

        cape_user_list = []

        cape_request = requests.get(self.cape_url + capeid)

        soup = BeautifulSoup(cape_request.text, 'html.parser')
        cape_scrape = soup.find_all('div', class_='card-body player-list py-2')

        for capeusers in cape_scrape:
            for get_cape in capeusers.find_all('a', href=True):
                cape_user_list.append(get_cape.text)

        return cape_user_list

    def capeUserNumber(self, capeid):

        cape_list_for_number = []

        cape_request = requests.get(self.cape_url + capeid)

        soup = BeautifulSoup(cape_request.text, 'html.parser')
        cape_scrape = soup.find_all('div', class_='card-body player-list py-2')

        for cape_user in cape_scrape:
            for capeNumber in cape_user.find_all('a', href=True):
                cape_list_for_number.append(capeNumber.text)
                
        return len(cape_list_for_number) 

    def playerSkins(self, current=False, username=False, uuid=False): #username or uuid is 'false' because its not mandatory to enter them11

        skin_hash_list = [] #makes list to store all skin hashes that namemc is using
        final_list = []

        if isinstance(username, str):
            profile_request = requests.get('https://namemc.com/profile/' + username) #gets websites code or scrapes it

        if isinstance(uuid, str):
            profile_request = requests.get('https://namemc.com/profile/' + str(uuid)) #gets websites code or scrapes it

        soup = BeautifulSoup(profile_request.text, 'html.parser')
        skin_scrape = soup.find_all('div', class_='card-body text-center') # searches for div in the specified class

        for usedskins in skin_scrape:
            for skin_hashes in usedskins.find_all('a', href=True):
                    skin_hash_list.append(skin_hashes['href'])

        if current == False: # if player wants to see the first skin or current skin then it will NOT git rid of javascript thing because it will not view it
            skin_hash_list.remove('javascript:void(0)') # weird thing that actually gets in the list so I have to do this

        for s in skin_hash_list: # strips /skin/ from the lis
            final = s.lstrip('/skin/')
            final_list.append(final) # cant seem to clear the final list so I just made another list

        if current == False: # if current false just print the full list
            return final_list
        if current == True: # if current true give it the first value if your wondering the reason why its 0 is because in programming numbers start at 0
            return final_list[0]
        
    def renderSkin(self, skinhash, model, x=False, y=False, directon=False, time=False):

        if directon=='front' and model=='slim' and time==False:
            url = 'https://render.namemc.com/skin/3d/body.png?skin=' + skinhash + '&model=slim&theta=0&phi=0&time=0&width=600&height=800'
            
        if directon=='front' and model=='slim' and isinstance(time, str):
            url = 'https://render.namemc.com/skin/3d/body.png?skin=' + skinhash + '&model=slim&theta=0&phi=0&time=' + time + '&width=600&height=800'

        if directon=='front' and model=='big' and time==False:
            url = 'https://render.namemc.com/skin/3d/body.png?skin=' + skinhash + '&model=big&theta=0&phi=0&time=0&width=600&height=800'
            
        if directon=='front' and model=='big' and isinstance(time, str):
            url = 'https://render.namemc.com/skin/3d/body.png?skin=' + skinhash + '&model=big&theta=0&phi=0&time=' + time + '&width=600&height=800'
        
        if isinstance(x, str) and isinstance(y, str) and directon==False and isinstance(time, str):
            url = 'https://render.namemc.com/skin/3d/body.png?skin=' + skinhash + '&model='+ model + '&theta='+ x + '&phi='+ y + '&time=' + time + '&width=600&height=800'

        return url
