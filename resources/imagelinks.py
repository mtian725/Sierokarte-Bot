import discord

wind = discord.Color.from_rgb(141, 229, 95)
fire = discord.Color.from_rgb(195, 59, 35)
water = discord.Color.from_rgb(76, 157, 225)
earth = discord.Color.from_rgb(180, 119, 63)
light = discord.Color.from_rgb(254, 236, 109)
dark = discord.Color.from_rgb(139, 82, 212)
grey = discord.Color.from_rgb(169, 167, 165)

images = {
  'abby' : [
  (fire,'https://gbf.wiki/images/5/50/Npc_zoom_3030011000_01.png'),
  (fire,'https://gbf.wiki/images/7/79/Npc_zoom_3030011000_02.png')
  ],
  'agielba' : [
  (fire,'https://gbf.wiki/images/6/68/Npc_zoom_3040017000_01.png'),
  (fire,'https://gbf.wiki/images/3/3a/Npc_zoom_3040017000_02.png'),
  ],
  'aglovale' : [
  (water,'https://gbf.wiki/images/c/c2/Npc_zoom_3040192000_01.png'),
  (water,'https://gbf.wiki/images/9/98/Npc_zoom_3040192000_02.png'),
  (water,'https://gbf.wiki/images/f/f1/Aglovale%2C_Lord_of_Frost_NPC.png'),
  (grey,'https://gbf.wiki/images/d/d4/House_of_Wales_Dress_Uniform_%28Aglovale%29.png'),
  ],
  'airitotoki' : [
  (earth, 'https://gbf.wiki/images/c/cf/AiriTotoki_A.png'),
  (earth, 'https://gbf.wiki/images/b/b5/AiriTotoki_B.png')
  ],
  'alanaan' : [
  (fire,'https://gbf.wiki/images/f/f9/Npc_zoom_3040167000_01.png'),
  (fire,'https://gbf.wiki/images/5/5a/Npc_zoom_3040167000_02.png')
  ],
  'albert' : [
  (light,'https://gbf.wiki/images/2/22/Npc_zoom_3040045000_01.png'),
  (light,'https://gbf.wiki/images/2/20/Npc_zoom_3040045000_02.png'),
  (light,'https://gbf.wiki/images/4/4e/Npc_zoom_3040045000_03.png'),
  (light,'https://gbf.wiki/images/2/23/Npc_zoom_3030177000_01.png'),
  (light,'https://gbf.wiki/images/e/e4/Npc_zoom_3030177000_02.png')
  ],
  'alec' : [
  (fire,'https://gbf.wiki/images/4/4a/Npc_zoom_3030003000_01.png'),
  (fire,'https://gbf.wiki/images/5/52/Npc_zoom_3030003000_02.png'),
  (fire,'https://gbf.wiki/images/9/97/Npc_zoom_3030003000_03.png')
  ],
  'aletheia' :[
  (earth,'https://gbf.wiki/images/d/d1/Npc_zoom_3040002000_01.png'),
  (earth,'https://gbf.wiki/images/a/a0/Npc_zoom_3040002000_02.png')
  ],
  'alexiel' :[
  (earth,'https://gbf.wiki/images/9/92/Npc_zoom_3040158000_01.png'),
  (earth,'https://gbf.wiki/images/1/11/Npc_zoom_3040158000_02.png'),
  (earth,'https://gbf.wiki/images/6/6a/Npc_zoom_3040158000_81.png'),
  (earth,'https://gbf.wiki/images/9/9f/Npc_zoom_3040232000_01.png'),
  (earth,'https://gbf.wiki/images/4/40/Npc_zoom_3040232000_02.png'),
  (earth,'https://gbf.wiki/images/e/e8/Npc_zoom_3040232000_81.png')
  ],
  'alistair' : [
  (water, 'https://gbf.wiki/images/f/fc/Npc_zoom_3020053000_01.png'),
  (water, 'https://gbf.wiki/images/4/43/Npc_zoom_3020053000_02.png')
  ],
  'aliza' : [
  (fire, 'https://gbf.wiki/images/b/b3/Npc_zoom_3040083000_01.png'),
  (fire, 'https://gbf.wiki/images/e/ee/Npc_zoom_3040083000_02.png'),
  (fire, 'https://gbf.wiki/images/1/1b/Npc_zoom_3030015000_01.png'),
  (fire, 'https://gbf.wiki/images/9/90/Npc_zoom_3030015000_02.png'),
  (water, 'https://gbf.wiki/images/0/06/Npc_zoom_3030242000_01.png'),
  (water, 'https://gbf.wiki/images/8/8a/Npc_zoom_3030242000_02.png'),
  (wind, 'https://gbf.wiki/images/5/5c/Npc_zoom_3040233000_01.png'),
  (wind, 'https://gbf.wiki/images/c/ca/Npc_zoom_3040233000_02.png'),
  (grey, 'https://gbf.wiki/images/7/7d/Sahara_Musafir_%28Aliza%29.png'),
  (grey, 'https://gbf.wiki/images/e/ea/AlizaIdol.png')
  ],
  'almeida' : [
  (earth, 'https://gbf.wiki/images/8/86/Npc_zoom_3030139000_01.png'),
  (earth, 'https://gbf.wiki/images/a/a5/Npc_zoom_3030139000_02.png'),
  (earth, 'https://gbf.wiki/images/b/b7/Npc_zoom_3030250000_01.png'),
  (earth, 'https://gbf.wiki/images/0/0d/Npc_zoom_3030250000_02.png')
  ],
  'altair' : [
  (water, 'https://gbf.wiki/images/a/ab/Npc_zoom_3040001000_01.png'),
  (water, 'https://gbf.wiki/images/6/66/Npc_zoom_3040001000_02.png'),
  (water, 'https://gbf.wiki/images/8/8f/Npc_zoom_3040001000_03.png'),
  (grey, 'https://gbf.wiki/images/5/54/Altair_Tactician%27s_Livery.png')
  ],
  'amira' : [
  (light, 'https://gbf.wiki/images/f/f3/Npc_zoom_3040051000_01.png'),
  (light, 'https://gbf.wiki/images/4/4d/Npc_zoom_3040051000_02.png'),
  (light, 'https://gbf.wiki/images/2/2a/Npc_zoom_3040051000_03.png'),
  (light, 'https://gbf.wiki/images/2/2a/Npc_zoom_3030065000_01.png'),
  (light, 'https://gbf.wiki/images/8/8c/Npc_zoom_3030065000_02.png'),
  (light, 'https://gbf.wiki/images/8/83/Npc_zoom_3030065000_03.png')
  ],
  'anastasia' : [
  (water, 'https://gbf.wiki/images/8/8b/Npc_zoom_3030160000_01.png'),
  (water, 'https://gbf.wiki/images/3/31/Npc_zoom_3030160000_02.png')
  ],
  'andira' : [
  (wind, 'https://gbf.wiki/images/7/7a/Npc_zoom_3040071000_01.png'),
  (wind, 'https://gbf.wiki/images/a/a1/Npc_zoom_3040071000_02.png'),
  (wind, 'https://gbf.wiki/images/f/fd/Npc_zoom_3040071000_03.png'),
  (wind, 'https://gbf.wiki/images/d/d7/Npc_zoom_3030170000_01.png'),
  (wind, 'https://gbf.wiki/images/8/85/Npc_zoom_3030170000_02.png'),
  (grey, 'https://gbf.wiki/images/4/40/AndiraOutfit.png')
  ],
  'monika' : [
  (wind,'https://i.imgur.com/3g2iFbF.png'), # fix links
  (wind,'https://i.imgur.com/qKCZeDu.png'),
  (wind,'https://i.imgur.com/iUkOJnJ.png'),
  (wind,'https://i.imgur.com/mEnmxIV.png'),
  (wind,'https://i.imgur.com/FTaLsbC.png')
  ]
}
