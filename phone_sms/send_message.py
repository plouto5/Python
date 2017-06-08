from clockwork import clockwork

api = clockwork.API('e22468d6b972f1425f77827f6f279d11b4b2c183')

message = clockwork.SMS(from_name = "The Dark Master", to = "6129102910", message = "I am watching you.....")

response = api.send(message)
print(response)

