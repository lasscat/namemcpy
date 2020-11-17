from namemcpy import namepy
example = namepy()
test = example.verifyLikeUuid(server='example.com', uuid='uuid')
print(test)

# OUTPUT
#if uuid is not liking the server then
#print(the uuid (uuid) is not liking the server (server))
return False
#if uuid is liking the server then
#print(the uuid (uuid) is liking the server (server))
return True
