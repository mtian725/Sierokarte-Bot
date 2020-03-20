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
  'ange' : [
  (water, 'https://gbf.wiki/images/4/45/Npc_zoom_3030012000_01.png'),
  (water, 'https://gbf.wiki/images/b/ba/Npc_zoom_3030012000_02.png'),
  (water, 'https://gbf.wiki/images/6/64/Npc_zoom_3030012000_03.png'),
  (dark, 'https://gbf.wiki/images/d/d9/Npc_zoom_3030042000_01.png'),
  (dark, 'https://gbf.wiki/images/3/32/Npc_zoom_3030042000_02.png')
  ],
  'anila' : [
  (fire, 'https://gbf.wiki/images/a/a5/Npc_zoom_3040027000_01.png'),
  (fire, 'https://gbf.wiki/images/1/16/Npc_zoom_3040027000_02.png'),
  (fire, 'https://gbf.wiki/images/2/2b/Npc_zoom_3040027000_03.png'),
  (fire, 'https://gbf.wiki/images/2/26/Npc_zoom_3030110000_01.png'),
  (fire, 'https://gbf.wiki/images/1/1c/Npc_zoom_3030110000_02.png'),
  (grey, 'https://gbf.wiki/images/3/3a/AnilaOutfit.png')
  ],
  'anna' : [
  (fire, 'https://gbf.wiki/images/a/a4/Npc_zoom_3020008000_01.png'),
  (fire, 'https://gbf.wiki/images/5/5a/Npc_zoom_3020008000_02.png'),
  (fire, 'https://gbf.wiki/images/3/35/Npc_zoom_3030095000_01.png'),
  (fire, 'https://gbf.wiki/images/a/ab/Npc_zoom_3030095000_02.png'),
  (fire, 'https://gbf.wiki/images/6/67/Npc_zoom_3020021000_01.png'),
  (fire, 'https://gbf.wiki/images/7/72/Npc_zoom_3020021000_02.png')
  ],
  'anne' : [
  (water, 'https://gbf.wiki/images/b/bf/Npc_zoom_3040132000_01.png'),
  (water, 'https://gbf.wiki/images/1/1a/Npc_zoom_3040132000_02.png')
  ],
  'anre' : [
  (water, 'https://gbf.wiki/images/9/98/Npc_zoom_3040030000_01.png'),
  (water, 'https://gbf.wiki/images/1/10/Npc_zoom_3040030000_02.png'),
  (water, 'https://gbf.wiki/images/f/ff/Npc_zoom_3040030000_03.png'),
  (water, 'https://gbf.wiki/images/f/f6/Npc_zoom_3040030000_81.png'),
  (grey, 'https://gbf.wiki/images/1/17/Mustachioed_Santa.png')
  ],
  'anthuria' : [
  (fire, 'https://gbf.wiki/images/1/19/Npc_zoom_3040103000_01.png'),
  (fire, 'https://gbf.wiki/images/b/bc/Npc_zoom_3040103000_02.png'),
  (dark, 'https://gbf.wiki/images/a/a2/Npc_zoom_3040228000_01.png'),
  (dark, 'https://gbf.wiki/images/c/ce/Npc_zoom_3040228000_02.png'),
  (dark, 'https://gbf.wiki/images/c/cd/Npc_zoom_3040228000_81.png')
  ],
  'anzufutaba' : [
  (earth, 'https://gbf.wiki/images/3/3c/AnzuFutaba_A.png'),
  (earth, 'https://gbf.wiki/images/9/97/AnzuFutaba_B.png'),
  (earth, 'https://gbf.wiki/images/5/51/Npc_zoom_3030071000_03.png')
  ],
  'aoidos' : [
  (fire, 'https://gbf.wiki/images/c/c6/Npc_zoom_3040076000_01.png'),
  (fire, 'https://gbf.wiki/images/1/1d/Npc_zoom_3040076000_02.png')
  ],
  'aqoursfirst-years' : [
  (earth, 'https://gbf.wiki/images/a/a4/Npc_zoom_3040184000_01.png'),
  (earth, 'https://gbf.wiki/images/5/5c/Yoshiko_Tsushima_A.png'),
  (earth, 'https://gbf.wiki/images/6/6d/Hanamaru_Kunikida_A.png'),
  (earth, 'https://gbf.wiki/images/3/33/Ruby_Kurosawa_A.png'),
  (earth, 'https://gbf.wiki/images/2/22/Npc_zoom_3040184000_02.png')
  ],
  'aqourssecond-years' : [
  (water, 'https://gbf.wiki/images/7/76/Npc_zoom_3040183000_01.png'),
  (water, 'https://gbf.wiki/images/a/ae/Riko_Sakurauchi_A.png'),
  (water, 'https://gbf.wiki/images/0/0a/Chika_Takami_A.png'),
  (water, 'https://gbf.wiki/images/2/20/You_Watanabe_A.png'),
  (water, 'https://gbf.wiki/images/7/75/Npc_zoom_3040183000_02.png'),
  (water, 'https://gbf.wiki/images/f/fe/Npc_zoom_3040183000_03.png')
  ],
  'aqoursthird-years' : [
  (fire, 'https://gbf.wiki/images/3/37/Npc_zoom_3040185000_01.png'),
  (fire, 'https://gbf.wiki/images/0/06/Kanan_Matsuura_A.png'),
  (fire, 'https://gbf.wiki/images/f/f2/Dia_Kurosawa_A.png'),
  (fire, 'https://gbf.wiki/images/2/23/Mari_Ohara_A.png'),
  (fire, 'https://gbf.wiki/images/3/37/Npc_zoom_3040185000_02.png')
  ],
  'arisa' : [
  (wind, 'https://gbf.wiki/images/0/03/Npc_zoom_3030179000_01.png'),
  (wind, 'https://gbf.wiki/images/d/dc/Npc_zoom_3030179000_02.png')
  ],
  'arriet' : [
  (wind, 'https://gbf.wiki/images/e/eb/Npc_zoom_3040058000_01.png'),
  (wind, 'https://gbf.wiki/images/c/c9/Npc_zoom_3040058000_02.png')
  ],
  'arthur' : [
  (wind, 'https://gbf.wiki/images/f/fe/Npc_zoom_3030226000_01.png'),
  (wind, 'https://gbf.wiki/images/b/b7/Npc_zoom_3030226000_02.png'),
  (wind, 'https://gbf.wiki/images/8/80/Npc_zoom_3030255000_01.png'),
  (wind, 'https://gbf.wiki/images/1/13/Npc_zoom_3030255000_02.png')
  ],
  'arulumaya' : [
  (earth, 'https://gbf.wiki/images/b/bb/Npc_zoom_3040019000_01.png'),
  (earth, 'https://gbf.wiki/images/8/83/Npc_zoom_3040019000_02.png'),
  (earth, 'https://gbf.wiki/images/a/ab/Npc_zoom_3040019000_03.png'),
  (water, 'https://gbf.wiki/images/5/55/Npc_zoom_3040104000_01.png'),
  (water, 'https://gbf.wiki/images/1/10/Npc_zoom_3040104000_02.png'),
  (dark, 'https://gbf.wiki/images/d/db/Npc_zoom_3030249000_01.png'),
  (dark, 'https://gbf.wiki/images/f/f1/Npc_zoom_3030249000_02.png')
  ],
  'arusha' : [
  (light, 'https://gbf.wiki/images/b/b9/Npc_zoom_3030036000_01.png'),
  (light, 'https://gbf.wiki/images/4/4e/Npc_zoom_3030036000_02.png')
  ],
  'aster' : [
  (fire, 'https://gbf.wiki/images/4/44/Npc_zoom_3030268000_01.png'),
  (fire, 'https://gbf.wiki/images/4/4c/Npc_zoom_3030268000_02.png'),
  (wind, 'https://gbf.wiki/images/6/62/Npc_zoom_3030044000_01.png'),
  (wind, 'https://gbf.wiki/images/a/af/Npc_zoom_3030044000_02.png')
  ],
  'athena' : [
  (fire, 'https://gbf.wiki/images/3/32/Npc_zoom_3040202000_01.png'),
  (fire, 'https://gbf.wiki/images/8/88/Npc_zoom_3040202000_02.png')
  ],
  'augusta' : [
  (earth, 'https://gbf.wiki/images/a/ae/Npc_zoom_3030143000_01.png'),
  (earth, 'https://gbf.wiki/images/4/45/Npc_zoom_3030143000_02.png'),
  (earth, 'https://gbf.wiki/images/0/09/Npc_zoom_3030143000_81.png')
  ],
  'ayer' : [
  (earth, 'https://gbf.wiki/images/a/a2/Npc_zoom_3040084000_01.png'),
  (earth, 'https://gbf.wiki/images/f/f9/Npc_zoom_3040084000_02.png'),
  (earth, 'https://gbf.wiki/images/0/0c/Npc_zoom_3040084000_03.png'),
  (earth, 'https://gbf.wiki/images/c/c5/Npc_zoom_3030199000_01.png'),
  (earth, 'https://gbf.wiki/images/e/ea/Npc_zoom_3030199000_02.png')
  ],
  'azazel' : [
  (dark, 'https://gbf.wiki/images/e/e5/Npc_zoom_3040137000_01.png'),
  (dark, 'https://gbf.wiki/images/6/68/Npc_zoom_3040137000_02.png')
  ],
  'monika' : [
  (wind,'https://i.imgur.com/3g2iFbF.png'), # fix links
  (wind,'https://i.imgur.com/qKCZeDu.png'),
  (wind,'https://i.imgur.com/iUkOJnJ.png'),
  (wind,'https://i.imgur.com/mEnmxIV.png'),
  (wind,'https://i.imgur.com/FTaLsbC.png')
  ]
}
