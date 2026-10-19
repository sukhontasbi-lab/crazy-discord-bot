import os
from pathlib import Path

import discord
from discord.ext import commands
from dotenv import load_dotenv


def create_bot() -> commands.Bot:
    intents = discord.Intents.default()
    intents.message_content = True

    bot = commands.Bot(command_prefix="!", intents=intents)

    @bot.event
    async def on_ready() -> None:
        print(f"Connected as {bot.user}.")
        print("Try !hello or !ping in a server channel.")

    @bot.command(name="hello")
    async def hello(ctx: commands.Context) -> None:
        await ctx.reply(
            f"Hello, {ctx.author.display_name}!",
            mention_author=False,
        )

    @bot.command(name="ping")
    async def ping(ctx: commands.Context) -> None:
        latency_ms = round(bot.latency * 1000)
        await ctx.reply(f"Pong! {latency_ms} ms.", mention_author=False)

    return bot


def main() -> None:
    # Replit Secrets or other environment variables take precedence over .env.
    load_dotenv(Path(__file__).with_name(".env"))
    token = os.getenv("DISCORD_BOT_TOKEN")

    if not token:
        raise SystemExit(
            "DISCORD_BOT_TOKEN is not set. Add it to Replit Secrets or a local .env file."
        )

    create_bot().run(token)


if __name__ == "__main__":
    main()
