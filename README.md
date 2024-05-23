Sure, here's a `README.md` for your GitHub repository to guide people on how to start and use the bot:

```markdown
# Voice State Update Bot

This Discord bot sends a message to a specific channel whenever a user from a monitored list joins a voice channel. Special messages can be customized for specific users.

## Features

- Tracks voice state updates of specified users
- Sends a custom message to a designated text channel when a monitored user joins a voice channel

## Getting Started

### Prerequisites

- Python 3.8 or higher
- `discord.py` library

### Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/yourusername/voice-state-update-bot.git
   cd voice-state-update-bot
   ```

2. **Create and activate a virtual environment (optional but recommended)**

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required packages**

   ```bash
   pip install discord.py
   ```

### Configuration

1. **Edit the bot script**

   Open the `bot.py` script and replace `"YOUR_DISCORD_BOT_TOKEN"` with your actual Discord bot token. You can obtain a bot token by creating a new application in the [Discord Developer Portal](https://discord.com/developers/applications).

   ```python
   client.run("YOUR_DISCORD_BOT_TOKEN")
   ```

2. **Update monitored users and channel name (if needed)**

   The bot monitors the users listed in the `paneleiros` list. If you want to add or remove users, modify this list. Also, ensure the channel name `"os-maiores"` matches the channel in your Discord server.

### Running the Bot

1. **Run the bot**

   ```bash
   python bot.py
   ```

   The bot should now be running and monitoring the specified users.

### Customization

To add more custom messages or change the behavior for other users, edit the `on_voice_state_update` function in the `bot.py` script.

```python
@client.event
async def on_voice_state_update(member, before, after):
    if member.name.lower() in paneleiros and not before.channel and after.channel:
        channel = discord.utils.get(member.guild.channels, name="os-maiores")
        if channel:
            if member.name.lower() == "sudeenly":
                await channel.send(f"One kebab please, {member.mention}")
            else:
                await channel.send(f"Boa, o paneleiro do {member.mention} entrou na call. Foda-se")
```

## Contributing

Feel free to fork this repository and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

## License

All rights reserved. Ah, nevermind, just copy it.
```

Save this content to a file named `README.md` in the root of your repository. This guide provides clear instructions on how to set up, configure, and run your bot, as well as how to customize it further if needed.
