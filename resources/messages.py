import discord

help = discord.Embed(
    title = '__Sierokarte Bot Help__',
    color = discord.Color.blue(),
)
help.add_field(name='CALCARCARUM (will remove or edit)',
value='**!calcarcarum** or **!ca** \n Respond to the prompts given and it will'+
        ' generate a list of recources needed',
inline=False)
help.add_field(name='ETERNALS (will remove or edit)',
value='**!eternals** or **!e** \n Follow the initial prompt and click on the '+
        'reacts to change pages',
inline=False)
help.add_field(name='WIKI',
value='**!wiki** or **!w** \n Searches the item after the command and returns '+
'a link from the GBF wiki \n Syntax: !wiki <item>',
inline=False)
help.add_field(name='TIME',
value='**!time** or **!t** \n gives the time in JST',
inline=False)
help.add_field(name='ART',
value = '**!art** or **!a** \n Returns an embed with all the art associated ' +
'with the character \n Syntax: !art <character name>',
inline=False)
help.add_field(name='FIND',
value = '**!find** or **!f** \n Returns a list of characters that matches the' +
'trait(s) listed \n Syntax: !find <trait1> <trait2> ...',
inline=False)

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

eternals = discord.Embed(
    title = 'Eternals Help',
    description = '__Pick what you are looking for:__\n'
    '**0** : Unlock Eternals/Uncap Revenant Weapons\n'
    '**1** : Uncap Eternal to 5*\n',
    color = discord.Color.gold()
)
eternals.set_footer(text='Hit c to cancel')
eternals.set_image(url='https://gbf.wiki/images/6/6c/RevWep_banner.png')

eternals_1 = [
discord.Embed(
    title = 'Step 1: Obtain the Revenant Weapon',
    description = 'Get the **Revenant Weapon** from a Unite '
    'and Fight (Guild War) event.'
    'The Eternal that corresponds to each weapon is as follows:\n'
    'Anre - One-Rift Spear\nTweyen - Two-Crown Bow\n'
    'Threo - Three-Tiger Axe\nFeower - Four-Sky Blade\n'
    'Fif - Five-Soul Staff\nSeox - Six-Ruin Fist\n'
    'Seofon - Seven-Star Sword\nEahta - Eight-Life Katana\n'
    'Niyon - Nine-Realm Harp\nTien - Ten-Wolf Gun',
    color = discord.Color.gold()
),
discord.Embed(
    title = 'Step 2: Awaken the Revenant Weapon',
    description = 'After fully uncapping and leveling your Revenant Weapon to '
    'level 100, go to the **Weapon Series** tab at the **shop**, go to the '
    '**Revenant Weapon** section, and select your weapon. '
    'Awakening will require:\n'
    '-Shining Orb ×50 \n'
    '-Skylight Scroll ×50 \n'
    '-Radiant Whorl ×50 \n'
    '-White Dragon Scale ×50 \n'
    '-Champion Merit ×50 \n'
    '-Crystal ×100',
    color = discord.Color.gold()
),
discord.Embed(
    title = 'Step 3: Change the Revenant Weapon\'s Element',
    description = 'You will need to change the weapon\'s element this step. '
    '**Because you will eventually duel the Eternal with the Revenant Weapon as'
    ' your mainhand, it\'s recommended to change the element to the one that is'
    ' strong against the eternal**. You will need:\n-Weapon Relic ×1\n'
    '-True Animas ×3\n'
    'To get a Weapon Relic:\n'
    '**Go to Shop > Weapon Series > Ultima Weapons > Atma Recollection**\n'
    '-Low Orb ×250\n-Whorl ×250\n-Flawed Prism ×250\n'
    'Type of orb, whorl, ect. will be dependant on the weapon type you go for\n'
    'Weapon Skill Level needs to be 10 to proceed',
    color = discord.Color.gold()
),
discord.Embed(
    title = 'Upgrade The Shop',
    description = 'To upgrade further, you need to upgrade the shop. '
    '**Only need to do this once**. The following items are needed:\n'
    'Crimson Axe, Imperial Shotel, Crusher Glove, Main Gauche, Shining Knuckles, '
    'Shadow Spear, Rainbow Scale Pistol, Fire Nymph Staff, Water Nymph Staff, '
    'Earth Serpentine, Wind Talon Spear, Shining Barrel, Shadow Wand, '
    'Spiked Club : ×1\nMithra Anima ×5\nRupie ×200,000',
    color = discord.Color.gold()
),
discord.Embed(
    title = 'Step 4: Upgrade the Revenant Weapon',
    description = 'There are 6 separate upgrade to complete the weapon. '
    'Type of orb, whorl, ect. will be dependant on the weapon type you go for.\n',
    color = discord.Color.gold()
),
discord.Embed(
    title = 'Final Step',
    description = 'To unlock the Eternal, you must defeat character in a Fate'
    ' Episode in order to recruit them. Good luck!',
    color = discord.Color.gold()
)]
for e in eternals_1:
    e.set_footer(text='Times out after being left idle for 25 seconds')
eternals_1[0].set_image(url='https://i.imgur.com/rzqklQ3.png')
eternals_1[1].set_thumbnail(url='https://gbf.wiki/images/f/fe/Stamp191.png')
eternals_1[2].set_thumbnail(url='https://gbf.wiki/images/f/fe/Stamp214.png')
eternals_1[3].set_image(url='https://i.imgur.com/39BUX5R.png')
eternals_1[4].set_thumbnail(url='https://gbf.wiki/images/f/f3/Stamp218.png')
eternals_1[4].add_field(name='First Upgrade', value='300× Satin Feather\n'
'100× Untamed Flame\n100× Rough Stone\n100× Low Orb\n100× Tome\n150× Scroll\n'
'100× Whorl\n10× Supreme Merit\n3× Blue Sky Crystal\n100× Crystal',inline=True)

eternals_1[4].add_field(name='Second Upgrade', value='100× Fresh Water Jug\n'
'100× Vermilion Stone\n100× Hollow Soul\n150× Low Orb\n150× Tome\n150× Whorl\n'
'30× Dragon Scale\n50× Rainbow Prism\n3× True Anima\n5× Blue Sky Crystal\n'
'200× Crystal',inline=True)

eternals_1[4].add_field(name='Third Upgrade', value='300× Zephyr Feather\n'
'100× Falcon Feather\n80× Foreboding Clover\n200× Low Orb\n100× High Orb\n'
'200× Whorl\n100× Anima\n10× Supreme Merit\n7× Blue Sky Crystal\n'
'300× Crystal',inline=True)

eternals_1[4].add_field(name='Fourth Upgrade', value='100× Swirling Amber\n'
'100× Lacrimosa\n80× Blood Amber\n250× Low Orb\n250× Whorl\n50× Dragon Scale\n'
'150× Rainbow Prism\n3× True Anima\n10× Blue Sky Crystal\n'
'400× Crystal',inline=True)

eternals_1[4].add_field(name='Fifth Upgrade', value='20× Green Dragon Eye\n'
'20× Resolute Reactor\n20× Fanned Fin\n20× Genesis Bud\n20× Primal Bit\n'
'20× Black Fog Sphere\n100× Antique Cloth\n10× Supreme Merit\n'
'15× Blue Sky Crystal\n500× Crystal\n60× Omega Unique Item',inline=True)

eternals_1[4].add_field(name='Sixth Upgrade', value='3× True Fire Anima\n'
'3× True Water Anima\n3× True Earth Anima\n3× True Wind Anima\n'
'3× True Light Anima\n3× True Dark Anima\n250× Rainbow Prism\n'
'30× Blue Sky Crystal\n1× Gold Brick\n500× Crystal',inline=True)
eternals_1[5].set_image(url='https://gbf.wiki/images/7/7c/Stamp10.png')

# Complete this
eternals_2 = [
discord.Embed(
    title = 'Step 1: Fight the Eternal',
    description = 'Once you get an Eternal to level 80, you will be able to '
    'fight them in a Fate Episode. This will be a one-on-one between your '
    'main character and the eternal, where your mainhand weapon will be set '
    'to the Revenant Weapon.\n**Weapon skills and summon auras have no effect '
    'in this battle, so a good approach is to bring a grid of weapons with '
    'high raw stats, regardless of element, and summons with good call  '
    'effects and raw stats**.\nAfter defeating them, a follow-up Fate Episode'
    ' will appear, requiring a "Weapon Soul" to start. This will be acquired '
    'in the subsiquent steps.',
    color = discord.Color.gold()
),
discord.Embed(
    title = 'Step 2: Acquire 4 Silver Relics',
    description = 'Silver Relics and Shards drop when you have an Eternal on '
    'your team from **Angel Halo (Nightmare)**, which may appear after '
    'completing Angel Halo(Very Hard). A few things to keep in mind:\n'
    '-Eternal can be in front or backline\n-Will always drop at least 1 shard\n'
    '-Drop will always coorespond with the Eternal on the team\n'
    '-If multiple Eternals are on the team, then the drop will coorespond with '
    'any of them\n-Drop rate buffs **do** effect the Relic drop rate\n'
    'Random Shards also drop form Akasha (Raid)\n'
    'Relics can be bought for 10 Shards at the shop',
    color = discord.Color.gold()
),
discord.Embed(
    title = 'Step 3: Uncap Silver Relic to 4*',
    description = 'Once you get your Silver Relic to 3\*, you can uncap it to '
    '4* with these resources:\n-300× of the corresponding weapon stone\n'
    '-300× of **each** Elemental Quartz',
    color = discord.Color.gold()
),
discord.Embed(
    title = 'Step 4: Craft Gold Relic',
    description = 'The 4* Level 150 Silver Weapon is then crafted into a Gold '
    'Relic using:\n-1× Gold Brick\n-10× Silver Centrum\n-10× Damascus Crystal\n'
    '-5× Legendary Merit\n-30× Class Distinction\n-1× of **each** Element for '
    'the coorespond Relic Weapon\n-100× Revenant Weapon Fragment\n\n'
    'Eternals and thier corresponding distinction are as follows:\nAnre-Guardian\n'
	'Tweyen-Sharpshooter\nThreo-Gladiator\nFeower-Fencer\nFif-Pilgrim\nSeox-Combatant\n'
	'Seofon-Sword Master\nEahta-Samurai\nNiyon-Troubadour\nTien-Bandit\n',
    color = discord.Color.gold()
),
discord.Embed(
    title = 'Step 4 (continue): Craft Gold Relic',
    description = 'The last items, Revenant Weapon Fragments, are acquired by '
    'reducing the corresponding Revenant Weapons. You already have 50 from the '
    'fully uncapped weapon you made to unlock the Eternal. From here there are '
    '2 options:\n1. Create and reduce another fully uncapped Revenant Weapon\n'
    '2. Create and reduce 10 element-changed Revenant Weapons\n'
    'Option 1 will cost another **gold brick** while option 2 will not '
    'require a gold brick but it can be more time consuming\n\n'
    '**__WARNING__**\nIn-between stages of the Revenant Weapon awakening **DO NOT**'
    ' increase fragment yield until after the very last step (using the gold brick).'
    'Furthermore, reducing a fully uncapped Silver Weapon WILL NOT give you '
    'Revenant Weapon Fragments.',
    color = discord.Color.gold()
),
discord.Embed(
    title = 'Step 5: Obtain the Weapon Soul',
    description = 'After crafting, ~~admire all the hard work, time, resources,'
    ' and effort you put into creating this weapon, and throw those feelings '
    'out the window as you~~ reduce the Gold Weapon to aquire the weapon soul.',
    color = discord.Color.gold()
),
discord.Embed(
    title = 'Step 6: Fight the Weapon',
    description = 'You can now start the Fate Episode, which is a one-on-one '
    'fight between the Eternal and their corresponding weapon. If you are'
    ' having trouble, follow the guide below.\n\n'
    '**__One-Rift Spear__**: Use Fleeting Spark whenever it\'s off cooldown, only use Spiral Spear when the boss is in Overdrive, use Arm the Bastion for the 50% trigger.\n'
    '**__Two-Crown Bow__**: Its Charge Attack inflicts paralysis and is triggered at 50% and 10%. Try to save Merculight for charge attacks. Also, be careful to not lower it below 25% with 3 charge diamonds, as the charge attack will probably kill Tweyen. It is best to save The Clincher for when Two-Crown Bow is in overdrive to get it to break quickly.\n'
    '**__Three-Tiger Axe__**: Hold Threo\'s Charge Attack until you can get off a second Vorpal Rage + Ground Zero combo.\n'
    '**__Four-Sky Blade__**: Use skills and attack into its 50% trigger then wait out its multi-attack buff. Proceed as normal afterwards. Fairly easy if Feower triggers skill reset.\n'
    '**__Five-Soul Staff__**: Since Fif lacks damage skills, you\'re reliant on her being able to multi-attack to win the fight. It can apply a def-down debuff, so make sure to clear it. Time her heal so you can get maximum effectiveness out of it and don\'t forget to use her auto-revive.\n'
    '**__Six-Ruin Fist__**: Fairly straightforward fight, don\'t triple attack into counters or Charge Attacks and you should be good.\n'
    '**__Seven-Star Sword__**: Press Emblema every turn in order to raise Seofon\'s DA rate. Save Infinito Creare for when the boss is in overdrive.\n'
    '**__Eight-Life Katana__**: Save your charge attack until you have 200%, then use it to break the opponents overdrive. Use Open Spirit the turn before your charge attack and Dance of the Gods when appropriate and you\'ll be fine.\n'
    '**__Nine-Realm Harp__**: Use all her skills turn 1. If both Comatose and Tuning land, you\'re home free.\n'
    '**__Ten-Wolf Gun__**: The majority of Tien\'s damage comes from her skills. When it goes in Break mode, use Final Order + Stardust. Don\'t use her Charge Attack until the end.',
    color = discord.Color.gold()
),
discord.Embed(
    title = 'Step 7: Uncap Eternal to 5*',
    description = 'You can now uncap your Eternal to 5*. The resources needed '
    'are dependant on **Element**.\n'
    '**Fire** - Rubeus Centrum ×30, Fire Urn ×10, Bright Spirits ×2, Fire Grimoire ×30\n'
    '**Water** - Indicus Centrum ×30, Water Urn ×10, Murky Spirits ×2, Water Grimoire ×30\n'
    '**Earth** - Luteus Centrum ×30, Earth Urn ×10, Murky Spirits ×2, Earth Grimoire ×30\n'
    '**Wind** - Galbinus Centrum ×30, Wind Urn ×10, Bright Spirits ×2, Wind Grimoire ×30\n'
    '**Light** - Niveus Centrum ×30, Light Urn ×10, Bright Spirits ×2, Fire Grimoire ×15, Wind Grimoire ×15\n'
    '**Dark** - Ater Centrum ×30, Dark Urn ×10, Murky Spirits ×2, Water Grimoire ×15, Earth Grimoire ×15\n'
    '__**All Eternals Will also need**__: Rainbow Prism ×100, Rupie ×100,000',
    color = discord.Color.gold()
),
discord.Embed(
    title = 'Step 8: Unlock 4th Skill',
    description = 'You have now unlocked the Fate Episode where you can unlock '
    'your Eternal\'s 4th skill. You will have to fight as your chosen Eternal '
    'character in against all the other Eternals. \nA final fate episode will '
    'appear when it is cleared, forcing **you** to fight them again '
    'one-on-one to unlock their new skill. Weapon skills and summon auras '
    'don\'t take effect just like in **Step 1** so plan accordingly\n\nWith '
    'that done, **congratulations** you have fully unlocked '
    'the full potential of a very powerful unit.',
    color = discord.Color.gold()
)]
for e in eternals_2:
    e.set_footer(text='Times out after being left idle for 25 seconds')
eternals_2[0].set_thumbnail(url='https://gbf.wiki/images/2/2f/Stamp12.png')
eternals_2[1].set_image(url='https://i.imgur.com/b2JAUoz.png')
eternals_2[2].set_thumbnail(url='https://gbf.wiki/images/b/bf/Stamp78.png')
eternals_2[3].set_thumbnail(url='https://gbf.wiki/images/7/76/Stamp155.png')
eternals_2[4].set_thumbnail(url='https://gbf.wiki/images/7/76/Stamp155.png')
eternals_2[5].set_thumbnail(url='https://gbf.wiki/images/f/ff/Stamp28.png')
eternals_2[6].set_thumbnail(url='https://gbf.wiki/images/2/26/Stamp13.png')
eternals_2[7].set_thumbnail(url='https://gbf.wiki/images/5/52/Stamp39.png')
eternals_2[8].set_thumbnail(url='https://gbf.wiki/images/9/94/Stamp42.png')

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

remove_2 = discord.Embed(
    title = 'How many are you removing?',
    description = 'Type a number from 1 through 10',
    color = discord.Color.blue(),
)
remove_2.set_footer(text='Hit c to cancel')
