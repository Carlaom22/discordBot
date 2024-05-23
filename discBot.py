import discord
from discord.ext import commands

# Intents declaration
intents = discord.Intents.default()
intents.voice_states = True

# Initialize bot with intents
client = commands.Bot(command_prefix=".|. ", intents=intents)

# List of users to monitor
people = ["teixasg", "pr80", "nuno7774", "shin39252", "csm.exe", "kimmich", "dr4g6422", "brunoribeiro.7", "sudeenly"]

# Event listener for member voice state update
@client.event
async def on_voice_state_update(member, before, after):
    print(f"Voice state update: {member.name} before={before.channel} after={after.channel}")

    # Check if the member is in the monitored list and joined a voice channel
    if member.name.lower() in people and not before.channel and after.channel:
        print(f"{member.name} is in the monitored list and joined a channel")

        # Get the channel named "os-maiores" from the guild
        channel = discord.utils.get(member.guild.channels, name="os-maiores")
        if channel:
            print(f"Found channel: {channel.name}")
            # Send a special message if the member is "sudeenly" - We need to be careful with the girl
            if member.name.lower() == "sudeenly":
                await channel.send(f"One kebab please, {member.mention}")
            else:
                await channel.send(f"Boa, o paneleiro do {member.mention} entrou na call. Foda-se")
        else:
            print("Channel 'os-maiores' not found")
    else:
        print(f"{member.name} is not in the monitored list or did not join a new channel")

# Run the bot with your token
client.run("YOUR_DISCORD_BOT_TOKEN")
