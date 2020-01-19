import discord

wiki = 'https://gbf.wiki/Main_Page'

arc_thumbnails = {
    'Justice':'https://gbf.wiki/images/8/8a/Justice_%28SSR%29.png',
    'The Hanged Man':'https://gbf.wiki/images/d/d4/The_Hanged_Man_%28SSR%29.png',
    'Death':'https://gbf.wiki/images/f/fd/Death_%28SSR%29.png',
    'Temperance':'https://gbf.wiki/images/2/23/Temperance_%28SSR%29.png',
    'The Devil':'https://gbf.wiki/images/9/91/The_Devil_%28SSR%29.png',
    'The Tower':'https://gbf.wiki/images/0/04/The_Tower_%28SSR%29.png',
    'The Star':'https://gbf.wiki/images/e/e8/The_Star_%28SSR%29.png',
    'The Moon':'https://gbf.wiki/images/e/e5/The_Moon_%28SSR%29.png',
    'The Sun':'https://gbf.wiki/images/1/12/The_Sun_%28SSR%29.png',
    'Judgement':'https://gbf.wiki/images/7/71/Judgement_%28SSR%29.png'
}

arc_calc_1 = discord.Embed(
    title = 'Pick a summon/evoker below to calculate',
    description = '**0** : Justice - Maria Theresa\n'
    '**1** : The Hanged Man - Caim\n'
    '**2** : Death - Nier\n'
    '**3** : Temperance - Estarriola\n'
    '**4** : The Devil - Fraux\n'
    '**5** : The Tower - Lobelia\n'
    '**6** : The Star - Geisenborger\n'
    '**7** : The Moon - Haaselia\n'
    '**8** : The Sun - Alanaan\n'
    '**9** : Judgement - Katzelia',
    color = discord.Color.orange(),
)
arc_calc_1.set_footer(text='Hit c to cancel')
arc_calc_1.set_thumbnail(url='https://media.giphy.com/media/llaRufU4fSE9LEtwrB/giphy.gif')

arc_calc_2 = discord.Embed(
    title = 'Pick the start step',
    description = '**0** : No Summon\n'
    '**1** : Summon 0*\n'
    '**2** : Summon 1*\n'
    '**3** : Summon 2*\n'
    '**4** : Summon 3*\n'
    '**5** : Upgrade Summon to SSR\n'
    '**6** : Summon 4*\n'
    '**7** : Summon 5*\n'
    '**8** : Recruit Evoker\n'
    '**9** : Evoker 1*\n'
    '**10** : Evoker 2*\n'
    '**11** : Evoker 3*',
    color = discord.Color.orange(),
)
arc_calc_2.set_footer(text='Hit c to cancel')

arc_calc_3 = discord.Embed(
    title = 'Pick the end step',
    description = '**0** : Summon 0*\n'
    '**1** : Summon 1*\n'
    '**2** : Summon 2*\n'
    '**3** : Summon 3*\n'
    '**4** : Upgrade Summon to SSR\n'
    '**5** : Summon 4*\n'
    '**6** : Summon 5*\n'
    '**7** : Recruit Evoker\n'
    '**8** : Evoker 1*\n'
    '**9** : Evoker 2*\n'
    '**10** : Evoker 3*\n'
    '**11** : Evoker 4*',
    color = discord.Color.orange(),
)
arc_calc_3.set_footer(text='Hit c to cancel')

arc_calc_4 = discord.Embed(
    title = 'Do you want to see the individual steps?',
    description = '**0** : Yes\n'
    '**1** : No',
    color = discord.Color.orange()
)
arc_calc_4.set_footer(text='Hit c to cancel')

eternals_1 = discord.Embed(
    title = 'Eternal Help',
    description = '__Pick what you are looking for:__\n'
    '**0** : Unlock Eternals/Uncap Revenant Weapons\n'
    '**1** : Uncap Eternal to 5*\n',
    color = discord.Color.gold(),
)
eternals_1.set_footer(text='Hit c to cancel')
eternals_1.set_image(url='https://gbf.wiki/images/6/6c/RevWep_banner.png')

add_1 = discord.Embed(
    title = 'What are you adding?',
    description = '0 : Character\n'
    '1 : Weapon \n'
    '2 : Summon',
    color = discord.Color.blue(),
)
add_1.set_footer(text='Hit c to cancel')

add_2 = discord.Embed(
    title = 'What are you adding?',
    description = 'Type the name of what you are adding',
    color = discord.Color.blue(),
)
add_2.set_footer(text='Hit c to cancel')

add_3 = discord.Embed(
    title = 'Too many characters!',
    description = 'Remove some characters before you add more',
    color = discord.Color.red(),
)

add_3 = discord.Embed(
    title = 'Too many weapons!',
    description = 'Remove some weapons before you add more',
    color = discord.Color.red(),
)

add_3 = discord.Embed(
    title = 'Too many summons!',
    description = 'Remove some summons before you add more',
    color = discord.Color.red(),
)

add_4 = discord.Embed(
    title = 'Successfully added',
    description = '',
    color = discord.Color.blue(),
)

remove_1 = discord.Embed(
    title = 'What are you removing?',
    description = 'Type the name of what you are removing',
    color = discord.Color.blue(),
)
remove_1.set_footer(text='Hit c to cancel')
