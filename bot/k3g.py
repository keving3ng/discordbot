import random
import requests

from discord.ext.commands import Bot
from discord import Game

BOT_PREFIX = ("!") # prefixes recognized by bot to use message

client = Bot(command_prefix=BOT_PREFIX) # initializes bot using Bot() and prefixes above

@client.command(name='8ball', # primary call keyword
                description="Answers a yes/no question.", # description for specific !help
                brief="Magic answers.", # description for the general !help
                aliases=['eight_ball', 'eightball', '8-ball'], # aliases to be displayed in specific !help
                pass_context=True) # passes information about the sender and message
async def eight_ball(context):
    possible_responses = [
        'That\'s a resounding no',
        'Absolutely not'
        'I hope you\'re not serious',
        'Absolutely definitely',
        'Honestly? Probably',
        'It shall occur',
    ]
    await client.say(random.choice(possible_responses) + ", " + context.message.author.mention)


@client.command(name='github',
                description="Displays information on a github user given a username.", # desc for specific !help
                brief="Github user lookup.",
                category="Commands")# description for the general !help
async def githubLookup(username):
    github_url = 'https://api.github.com/users/' + username # creates the github api link to specific user
    data = requests.get(github_url).json() # uses requests lib to pull json file from api

    if 'login' in data:
        await client.say("Username: "+ str(data['login']) +"\nLocation: "+ str(data['location']) +"\nNo. of Public Repos: "+ str(data['public_repos']) +"\nFollowers: "+ str(data['followers']) +"\nFollowing:  "+ str(data['following']))
    else:
        await client.say("Error: User not found")

@client.command(name='crypto',
                description="Displays current price for a cryptocurrency in USD.", # desc for specific !help
                brief="Cryptocurrency price check.") # description for the general !help
async def cryptoprice(symbol):
    coin_url = "https://min-api.cryptocompare.com/data/price?tsyms=USD&fsym=" + symbol
    data = requests.get(coin_url).json()

    if 'USD' in data:
        await client.say("Price of "+ str(symbol) +" is $" + str(data['USD']) + " USD.")
    else:
        await client.say("Error: Invalid symbol")


@client.command(name='flip',
                description="Flips a coin",
                brief="Coin flip",
                pass_context=True)
async def flipacoin(context):
    coin_values = ['Heads', 'Tails']
    await client.say(random.choice(coin_values) + ", " + context.message.author.mention)


@client.command(description="Link to the source code on Github",
                brief="Source code link")
async def source():
    await client.say("https://github.com/keving3ng/discordbot")


@client.event
async def on_ready():
    await client.change_presence(game=Game(name="memes"))
    print('Logged in as') # Displays bot login information in console
    print(client.user.name)
    print(client.user.id)
    print('------')

token_file = open("token.txt", "r") # bot token is stored in this text file
client.run(token_file.read()) # initializes the bot
