import discord
import requests

client = discord.Client()

@client.event
async def on_message(message):
    if message.author == client.user: # Prevents bot from replying to itself
        return

    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
    elif message.content.startswith('!bot'):
        await client.send_message(message.channel, "You rang?")
    elif message.content.startswith('!github'):
        await client.send_message(message.channel, "Enter a Github username: ")

        githubUser = await client.wait_for_message(timeout=5.0, author=message.author)

        github_url = 'https://api.github.com/users/' + githubUser.content.strip()
        data = requests.get(github_url).json()

        await client.send_message(message.channel, "Username = "+data['login']+"\nLocation = "+data['location']+
                                  "\nNo. of Public Repos ="+str(data['public_repos'])+"\nFollowers = "
                                  +str(data['followers'])+"\nFollowing = "+str(data['following']))

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

token_file = open("token.txt", "r")
client.run(token_file.read())
