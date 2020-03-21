import discord
import collections

wind = discord.Color.from_rgb(141, 229, 95)
fire = discord.Color.from_rgb(195, 59, 35)
water = discord.Color.from_rgb(76, 157, 225)
earth = discord.Color.from_rgb(180, 119, 63)
light = discord.Color.from_rgb(254, 236, 109)
dark = discord.Color.from_rgb(139, 82, 212)
grey = discord.Color.from_rgb(169, 167, 165)

images = collections.OrderedDict()
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
  'airi totoki' : [
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
  (water, 'https://gbf.wiki/images/1/1a/Npc_zoom_3040132000_02.png'),
  (water, 'https://gbf.wiki/images/9/95/Npc_zoom_3040132000_81.png')
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
  'aqours first-years' : [
  (earth, 'https://gbf.wiki/images/a/a4/Npc_zoom_3040184000_01.png'),
  (earth, 'https://gbf.wiki/images/5/5c/Yoshiko_Tsushima_A.png'),
  (earth, 'https://gbf.wiki/images/6/6d/Hanamaru_Kunikida_A.png'),
  (earth, 'https://gbf.wiki/images/3/33/Ruby_Kurosawa_A.png'),
  (earth, 'https://gbf.wiki/images/2/22/Npc_zoom_3040184000_02.png')
  ],
  'aqours second-years' : [
  (water, 'https://gbf.wiki/images/7/76/Npc_zoom_3040183000_01.png'),
  (water, 'https://gbf.wiki/images/a/ae/Riko_Sakurauchi_A.png'),
  (water, 'https://gbf.wiki/images/0/0a/Chika_Takami_A.png'),
  (water, 'https://gbf.wiki/images/2/20/You_Watanabe_A.png'),
  (water, 'https://gbf.wiki/images/7/75/Npc_zoom_3040183000_02.png'),
  (water, 'https://gbf.wiki/images/f/fe/Npc_zoom_3040183000_03.png')
  ],
  'aqours third-years' : [
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
  'baal' : [
  (earth, 'https://gbf.wiki/images/f/f2/Npc_zoom_3040215000_01.png'),
  (earth, 'https://gbf.wiki/images/c/cc/Npc_zoom_3040215000_02.png'),
  (earth, 'https://gbf.wiki/images/c/cb/Npc_zoom_3040215000_81.png')
  ],
  'bakura' : [
  (dark, 'https://gbf.wiki/images/1/1c/Npc_zoom_3020066000_01.png'),
  (dark, 'https://gbf.wiki/images/6/6b/Npc_zoom_3020066000_02.png')
  ],
  'balurga' : [
  (earth, 'https://gbf.wiki/images/7/79/Npc_zoom_3020055000_01.png'),
  (earth, 'https://gbf.wiki/images/b/b6/Npc_zoom_3020055000_02.png')
  ],
  'baotorda' : [
  (light, 'https://gbf.wiki/images/0/04/Npc_zoom_3030053000_01.png'),
  (light, 'https://gbf.wiki/images/4/40/Npc_zoom_3030053000_02.png'),
  (light, 'https://gbf.wiki/images/2/21/Npc_zoom_3040124000_01.png'),
  (light, 'https://gbf.wiki/images/f/fc/Npc_zoom_3040124000_02.png')
  ],
  'barawa' : [
  (fire, 'https://gbf.wiki/images/f/ff/Npc_zoom_3020034000_01.png'),
  (fire, 'https://gbf.wiki/images/d/d6/Npc_zoom_3020034000_02.png'),
  (fire, 'https://gbf.wiki/images/3/39/Npc_zoom_3030154000_01.png'),
  (fire, 'https://gbf.wiki/images/9/99/Npc_zoom_3030154000_02.png'),
  (fire, 'https://gbf.wiki/images/a/a6/Npc_zoom_3030154000_81.png'),
  (light, 'https://gbf.wiki/images/8/81/Npc_zoom_3030239000_01.png'),
  (light, 'https://gbf.wiki/images/e/e6/Npc_zoom_3030239000_02.png')
  ],
  'beatrix' : [
  (dark, 'https://gbf.wiki/images/8/8c/Npc_zoom_3040070000_01.png'),
  (dark, 'https://gbf.wiki/images/c/c8/Npc_zoom_3040070000_02.png'),
  (fire, 'https://gbf.wiki/images/2/29/Npc_zoom_3030163000_01.png'),
  (fire, 'https://gbf.wiki/images/1/17/Npc_zoom_3030163000_02.png'),
  (earth, 'https://gbf.wiki/images/c/c6/Npc_zoom_3030261000_01.png'),
  (earth, 'https://gbf.wiki/images/b/b0/Npc_zoom_3030261000_02.png'),
  (fire, 'https://gbf.wiki/images/1/1e/Npc_zoom_3040110000_01.png'),
  (fire, 'https://gbf.wiki/images/4/4c/Npc_zoom_3040110000_02.png'),
  (grey, 'https://gbf.wiki/images/6/62/Blue_Pride.png'),
  (grey, 'https://gbf.wiki/images/2/2b/Beatrix_Racing_Suit.png'),
  (grey, 'https://gbf.wiki/images/6/6d/Skyfall_Blue_Kimono_%28Beatrix%29.png')
  ],
  'black knight' : [
  (dark, 'https://gbf.wiki/images/0/05/Npc_zoom_3040082000_01.png'),
  (dark, 'https://gbf.wiki/images/4/48/Npc_zoom_3040082000_02.png'),
  (dark, 'https://gbf.wiki/images/5/55/Npc_zoom_3040082000_03.png'),
  (dark, 'https://gbf.wiki/images/b/bc/Npc_zoom_3040082000_81.png')
  ],
  'bridgette' : [
  (water, 'https://gbf.wiki/images/6/62/Npc_zoom_3020048000_01.png'),
  (water, 'https://gbf.wiki/images/2/23/Npc_zoom_3020048000_02.png'),
  (light, 'https://gbf.wiki/images/a/a6/Npc_zoom_3030269000_01.png'),
  (light, 'https://gbf.wiki/images/f/f9/Npc_zoom_3030269000_02.png')
  ],
  'cagliostro' : [
  (earth, 'https://gbf.wiki/images/f/ff/Npc_zoom_3040009000_01.png'),
  (earth, 'https://gbf.wiki/images/b/b5/Npc_zoom_3040009000_02.png'),
  (earth, 'https://gbf.wiki/images/0/04/Npc_zoom_3040009000_03.png'),
  (dark, 'https://gbf.wiki/images/8/88/Npc_zoom_3040120000_01.png'),
  (dark, 'https://gbf.wiki/images/3/39/Npc_zoom_3040120000_02.png'),
  (dark, 'https://gbf.wiki/images/8/8a/Npc_zoom_3030189000_01.png'),
  (dark, 'https://gbf.wiki/images/c/c3/Npc_zoom_3030189000_02.png'),
  (dark, 'https://gbf.wiki/images/a/a9/Npc_zoom_3040062000_01.png'),
  (dark, 'https://gbf.wiki/images/3/34/Npc_zoom_3040062000_02.png'),
  (water, 'https://gbf.wiki/images/a/af/Npc_zoom_3040225000_01.png'),
  (water, 'https://gbf.wiki/images/3/36/Npc_zoom_3040225000_02.png'),
  (water, 'https://gbf.wiki/images/b/ba/Npc_zoom_3040225000_81.png'),
  (grey, 'https://gbf.wiki/images/5/58/Cagliostro_Alchemic_Gothica.png'),
  (grey, 'https://gbf.wiki/images/1/1d/Cagliosled.png'),
  (grey, 'https://gbf.wiki/images/4/48/CagliostroIdol.png'),
  (grey, 'https://gbf.wiki/images/7/72/Cagliostro_Super_Jolly_Pretty_Alchemist.png'),
  (grey, 'https://gbf.wiki/images/1/1e/CagliostroUniform.png'),
  ],
  'cailana' : [
  (water, 'https://gbf.wiki/images/1/15/Npc_zoom_3020062000_01.png'),
  (water, 'https://gbf.wiki/images/e/ed/Npc_zoom_3020062000_02.png'),
  (water, 'https://gbf.wiki/images/a/a4/Npc_zoom_3030251000_01.png'),
  (water, 'https://gbf.wiki/images/3/3a/Npc_zoom_3030251000_02.png')
  ],
  'caim' : [
  (earth, 'https://gbf.wiki/images/d/d3/Npc_zoom_3040164000_01.png'),
  (earth, 'https://gbf.wiki/images/4/45/Npc_zoom_3040164000_02.png')
  ],
  'cain' : [
  (earth, 'https://gbf.wiki/images/4/4c/Npc_zoom_3030184000_01.png'),
  (earth, 'https://gbf.wiki/images/b/bc/Npc_zoom_3030184000_02.png'),
  (earth, 'https://gbf.wiki/images/5/57/Npc_zoom_3030184000_81.png'),
  (earth, 'https://gbf.wiki/images/9/9f/Npc_zoom_3040171000_01.png'),
  (earth, 'https://gbf.wiki/images/1/15/Npc_zoom_3040171000_02.png')
  ],
  'camieux' : [
  (fire, 'https://gbf.wiki/images/7/7d/Npc_zoom_3020032000_01.png'),
  (fire, 'https://gbf.wiki/images/6/6f/Npc_zoom_3020032000_02.png'),
  (earth, 'https://gbf.wiki/images/2/27/Npc_zoom_3020047000_01.png'),
  (earth, 'https://gbf.wiki/images/c/ca/Npc_zoom_3020047000_02.png'),
  (water, 'https://gbf.wiki/images/7/7c/Npc_zoom_3030152000_01.png'),
  (water, 'https://gbf.wiki/images/8/87/Npc_zoom_3030152000_02.png')
  ],
  'carmelina' : [
  (wind, 'https://gbf.wiki/images/1/1d/Npc_zoom_3040042000_01.png'),
  (wind, 'https://gbf.wiki/images/8/88/Npc_zoom_3040042000_02.png'),
  (earth, 'https://gbf.wiki/images/6/6a/Npc_zoom_3030240000_01.png'),
  (earth, 'https://gbf.wiki/images/0/03/Npc_zoom_3030240000_02.png')
  ],
  'carren' : [
  (fire, 'https://gbf.wiki/images/c/cb/Npc_zoom_3030046000_01.png'),
  (fire, 'https://gbf.wiki/images/d/dc/Npc_zoom_3030046000_02.png'),
  (fire, 'https://gbf.wiki/images/6/66/Npc_zoom_3030200000_01.png'),
  (fire, 'https://gbf.wiki/images/9/90/Npc_zoom_3030200000_02.png'),
  (fire, 'https://gbf.wiki/images/7/70/Npc_zoom_3030200000_81.png')
  ],
  'cassius' : [
  (dark, 'https://gbf.wiki/images/2/22/Npc_zoom_3030262000_01.png'),
  (dark, 'https://gbf.wiki/images/1/1d/Npc_zoom_3030262000_02.png'),
  (fire, 'https://gbf.wiki/images/c/cb/Npc_zoom_3030273000_01.png'),
  (fire, 'https://gbf.wiki/images/0/04/Npc_zoom_3030273000_02.png'),
  (fire, 'https://gbf.wiki/images/d/d7/Npc_zoom_3030273000_81.png')
  ],
  'catherine' : [
  (earth, 'https://gbf.wiki/images/f/f4/Npc_zoom_3040074000_01.png'),
  (earth, 'https://gbf.wiki/images/e/e6/Npc_zoom_3040074000_02.png'),
  (earth, 'https://gbf.wiki/images/c/c4/Npc_zoom_3030264000_01.png'),
  (earth, 'https://gbf.wiki/images/f/f1/Npc_zoom_3030264000_02.png')
  ],
  'cecile' : [
  (fire, 'https://gbf.wiki/images/0/0e/Npc_zoom_3030146000_01.png'),
  (fire, 'https://gbf.wiki/images/a/a4/Npc_zoom_3030146000_02.png'),
  (fire, 'https://gbf.wiki/images/d/d5/Npc_zoom_3030146000_81.png')
  ],
  'cerberus' : [
  (dark, 'https://gbf.wiki/images/9/9e/Npc_zoom_3040016000_01.png'),
  (dark, 'https://gbf.wiki/images/4/46/Npc_zoom_3040016000_02.png')
  ],
  'ceylan' : [
  (light, 'https://gbf.wiki/images/c/ce/Npc_zoom_3030074000_01.png'),
  (light, 'https://gbf.wiki/images/d/dc/Npc_zoom_3030074000_02.png')
  ],
  'charioce xvii' : [
  (fire, 'https://gbf.wiki/images/1/16/Npc_zoom_3040144000_01.png'),
  (fire, 'https://gbf.wiki/images/9/91/Npc_zoom_3040144000_02.png'),
  (fire, 'https://gbf.wiki/images/e/e7/Npc_zoom_3040144000_81.png')
  ],
  'charlotta' : [
  (water, 'https://gbf.wiki/images/b/b6/Npc_zoom_3040010000_01.png'),
  (water, 'https://gbf.wiki/images/1/1d/Npc_zoom_3040010000_02.png'),
  (water, 'https://gbf.wiki/images/d/dd/Npc_zoom_3040010000_03.png'),
  (water, 'https://gbf.wiki/images/9/91/Npc_zoom_3040010000_81.png'),
  (wind, 'https://gbf.wiki/images/9/95/Npc_zoom_3030192000_01.png'),
  (wind, 'https://gbf.wiki/images/c/ce/Npc_zoom_3030192000_02.png'),
  (light, 'https://gbf.wiki/images/f/f1/Npc_zoom_3040020000_01.png'),
  (light, 'https://gbf.wiki/images/3/32/Npc_zoom_3040020000_02.png'),
  (light, 'https://gbf.wiki/images/0/09/Npc_zoom_3040194000_01.png'),
  (light, 'https://gbf.wiki/images/9/94/Npc_zoom_3040194000_02.png'),
  (water, 'https://gbf.wiki/images/2/22/Npc_zoom_3030198000_01.png'),
  (water, 'https://gbf.wiki/images/2/28/Npc_zoom_3030198000_02.png'),
  (grey, 'https://gbf.wiki/images/f/f2/Charlotta_Petalfall_Kimono.png')
  ],
  'chat noir' : [
  (water, 'https://gbf.wiki/images/7/71/Npc_zoom_3040093000_01.png'),
  (water, 'https://gbf.wiki/images/3/3a/Npc_zoom_3040093000_02.png'),
  (water, 'https://gbf.wiki/images/4/4d/Npc_zoom_3040093000_81.png')
  ],
  'chloe' : [
  (wind, 'https://gbf.wiki/images/c/c2/Npc_zoom_3020059000_01.png'),
  (wind, 'https://gbf.wiki/images/4/4e/Npc_zoom_3020059000_02.png'),
  (wind, 'https://gbf.wiki/images/d/d0/Npc_zoom_3030202000_01.png'),
  (wind, 'https://gbf.wiki/images/8/88/Npc_zoom_3030202000_02.png')
  ],
  'christina' : [
  (wind, 'https://gbf.wiki/images/9/95/Npc_zoom_3040018000_01.png'),
  (wind, 'https://gbf.wiki/images/3/34/Npc_zoom_3040018000_02.png')
  ],
  'chun-li' : [
  (water, 'https://gbf.wiki/images/3/3e/ChunLi_A.png'),
  (water, 'https://gbf.wiki/images/b/b8/ChunLi_B.png')
  ],
  'clarisse' : [
  (fire, 'https://gbf.wiki/images/9/9a/Npc_zoom_3040046000_01.png'),
  (fire, 'https://gbf.wiki/images/c/cd/Npc_zoom_3040046000_02.png'),
  (fire, 'https://gbf.wiki/images/c/c3/Npc_zoom_3040046000_81.png'),
  (earth, 'https://gbf.wiki/images/5/54/Npc_zoom_3040067000_01.png'),
  (earth, 'https://gbf.wiki/images/a/ac/Npc_zoom_3040067000_02.png'),
  (light, 'https://gbf.wiki/images/8/8d/Npc_zoom_3040121000_01.png'),
  (light, 'https://gbf.wiki/images/9/98/Npc_zoom_3040121000_02.png'),
  (dark, 'https://gbf.wiki/images/4/47/Npc_zoom_3040206000_01.png'),
  (dark, 'https://gbf.wiki/images/b/b6/Npc_zoom_3040206000_02.png'),
  (dark, 'https://gbf.wiki/images/2/21/Npc_zoom_3040206000_81.png'),
  (grey, 'https://gbf.wiki/images/f/f1/Soleil_Blanc_%28Clarisse%29.png')
  ],
  'claudia' : [
  (earth, 'https://gbf.wiki/images/b/b8/Npc_zoom_3030057000_01.png'),
  (earth, 'https://gbf.wiki/images/a/a0/Npc_zoom_3030057000_02.png'),
  (light, 'https://gbf.wiki/images/9/9a/Npc_zoom_3040134000_01.png'),
  (light, 'https://gbf.wiki/images/6/66/Npc_zoom_3040134000_02.png')
  ],
  'colossus' : [
  (fire, 'https://gbf.wiki/images/6/69/Npc_zoom_3040235000_01.png'),
  (fire, 'https://gbf.wiki/images/e/e3/Npc_zoom_3040235000_02.png')
  ],
  'conanedogawa' : [
  (light, 'https://gbf.wiki/images/3/3e/Conan_Edogawa_A.png'),
  (light, 'https://gbf.wiki/images/5/5d/Npc_zoom_3040157000_02.png')
  ],
  'cordelia' : [
  (light, 'https://gbf.wiki/images/8/82/Npc_zoom_3020064000_01.png'),
  (light, 'https://gbf.wiki/images/b/bd/Npc_zoom_3020064000_02.png'),
  (light, 'https://gbf.wiki/images/a/a6/Npc_zoom_3030269000_01.png'),
  (light, 'https://gbf.wiki/images/f/f9/Npc_zoom_3030269000_02.png')
  ],
  'cucouroux' : [
  (fire, 'https://gbf.wiki/images/7/76/Npc_zoom_3030155000_01.png'),
  (fire, 'https://gbf.wiki/images/5/5e/Npc_zoom_3030155000_02.png'),
  (water, 'https://gbf.wiki/images/9/9d/Npc_zoom_3040159000_01.png'),
  (water, 'https://gbf.wiki/images/d/d1/Npc_zoom_3040159000_02.png'),
  (water, 'https://gbf.wiki/images/f/f8/Npc_zoom_3040159000_81.png'),
  (grey, 'https://gbf.wiki/images/5/50/Cucouroux_Gunsmith_Workwear.png')
  ],
  'cure black and cure white' : [
  (light, 'https://gbf.wiki/images/b/b9/Npc_zoom_3040188000_01.png'),
  (light, 'https://gbf.wiki/images/3/39/Cure_Black_A.png'),
  (light, 'https://gbf.wiki/images/3/3f/Cure_White_A.png'),
  (light, 'https://gbf.wiki/images/d/dd/Npc_zoom_3040188000_02.png')
  ],
  'daetta' : [
  (light, 'https://gbf.wiki/images/a/a5/Npc_zoom_3020024000_01.png'),
  (light, 'https://gbf.wiki/images/7/76/Npc_zoom_3020024000_02.png'),
  (light, 'https://gbf.wiki/images/b/b8/Npc_zoom_3030116000_01.png'),
  (light, 'https://gbf.wiki/images/6/62/Npc_zoom_3030116000_02.png')
  ],
  'dante' : [
  (fire, 'https://gbf.wiki/images/a/a5/Npc_zoom_3020044000_01.png'),
  (fire, 'https://gbf.wiki/images/3/33/Npc_zoom_3020044000_02.png'),
  (fire, 'https://gbf.wiki/images/d/da/Npc_zoom_3030156000_01.png'),
  (fire, 'https://gbf.wiki/images/3/30/Npc_zoom_3030156000_02.png'),
  (earth, 'https://gbf.wiki/images/0/0b/Npc_zoom_3040205000_01.png'),
  (earth, 'https://gbf.wiki/images/9/9a/Npc_zoom_3040205000_02.png')
  ],
  'danua' : [
  (dark, 'https://gbf.wiki/images/d/d0/Npc_zoom_3030017000_01.png'),
  (dark, 'https://gbf.wiki/images/3/3f/Npc_zoom_3030017000_02.png'),
  (dark, 'https://gbf.wiki/images/5/54/Npc_zoom_3030017000_03.png'),
  (fire, 'https://gbf.wiki/images/9/9b/Npc_zoom_3040135000_01.png'),
  (fire, 'https://gbf.wiki/images/6/66/Npc_zoom_3040135000_02.png'),
  (light, 'https://gbf.wiki/images/5/5f/Npc_zoom_3040256000_01.png'),
  (light, 'https://gbf.wiki/images/9/9f/Npc_zoom_3040256000_02.png'),
  (dark, 'https://gbf.wiki/images/7/7c/Npc_zoom_3040055000_01.png'),
  (dark, 'https://gbf.wiki/images/9/91/Npc_zoom_3040055000_02.png'),
  (dark, 'https://gbf.wiki/images/f/ff/Npc_zoom_3040055000_91.png')
  ],
  'de la fille' : [
  (light, 'https://gbf.wiki/images/1/11/Npc_zoom_3040004000_01.png'),
  (light, 'https://gbf.wiki/images/5/5d/Npc_zoom_3040004000_02.png'),
  (earth, 'https://gbf.wiki/images/8/87/Npc_zoom_3040113000_01.png'),
  (earth, 'https://gbf.wiki/images/a/a2/Npc_zoom_3040113000_02.png'),
  (light, 'https://gbf.wiki/images/2/26/Npc_zoom_3040014000_01.png'),
  (light, 'https://gbf.wiki/images/d/d9/Npc_zoom_3040014000_02.png'),
  (light, 'https://gbf.wiki/images/4/4b/Npc_zoom_3040014000_91.png')
  ],
  'deliford' : [
  (water, 'https://gbf.wiki/images/d/da/Npc_zoom_3020005000_01.png'),
  (water, 'https://gbf.wiki/images/b/b6/Npc_zoom_3020005000_02.png'),
  (dark, 'https://gbf.wiki/images/e/e8/Npc_zoom_3030188000_01.png'),
  (dark, 'https://gbf.wiki/images/0/09/Npc_zoom_3030188000_02.png')
  ],
  'diantha' : [
  (water, 'https://gbf.wiki/images/0/05/Npc_zoom_3030150000_01.png'),
  (water, 'https://gbf.wiki/images/e/ec/Npc_zoom_3030150000_02.png'),
  (water, 'https://gbf.wiki/images/3/35/Npc_zoom_3040129000_01.png'),
  (water, 'https://gbf.wiki/images/0/0c/Npc_zoom_3040129000_02.png'),
  (grey, 'https://gbf.wiki/images/4/46/Island_Rail_%28Diantha%29.png')
  ],
  'dorothy' : [
  (fire, 'https://gbf.wiki/images/d/df/Npc_zoom_3030058000_01.png'),
  (fire, 'https://gbf.wiki/images/1/1a/Npc_zoom_3030058000_02.png'),
  (light, 'https://gbf.wiki/images/9/9a/Npc_zoom_3040134000_01.png'),
  (light, 'https://gbf.wiki/images/6/66/Npc_zoom_3040134000_02.png')
  ],
  'drang' : [
  (water, 'https://gbf.wiki/images/2/2c/Npc_zoom_3040119000_01.png'),
  (water, 'https://gbf.wiki/images/e/ec/Npc_zoom_3040119000_02.png'),
  (water, 'https://gbf.wiki/images/7/77/Npc_zoom_3040119000_81.png')
  ],
  'drusilla' : [
  (fire, 'https://gbf.wiki/images/6/6a/Npc_zoom_3020063000_01.png'),
  (fire, 'https://gbf.wiki/images/8/80/Npc_zoom_3020063000_02.png')
  ],
  'eahta' : [
  (earth, 'https://gbf.wiki/images/1/1b/Npc_zoom_3040037000_01.png'),
  (earth, 'https://gbf.wiki/images/7/71/Npc_zoom_3040037000_02.png'),
  (earth, 'https://gbf.wiki/images/9/9d/Npc_zoom_3040037000_03.png'),
  (earth, 'https://gbf.wiki/images/3/39/Npc_zoom_3040037000_81.png'),
  (grey, 'https://gbf.wiki/images/5/5b/Warrior%27s_Ceremony_%28Eahta%29.png')
  ],
  'ejaeli' : [
  (water, 'https://gbf.wiki/images/c/c2/Npc_zoom_3030061000_01.png'),
  (water, 'https://gbf.wiki/images/3/38/Npc_zoom_3030061000_02.png'),
  (water, 'https://gbf.wiki/images/c/c0/Npc_zoom_3030061000_03.png')
  ],
  'elize lutus' : [
  (dark, 'https://gbf.wiki/images/8/88/ElizeLutus_A.png'),
  (dark, 'https://gbf.wiki/images/c/cd/ElizeLutus_B.png')
  ],
  'elmelaura' : [
  (fire, 'https://gbf.wiki/images/9/9e/Npc_zoom_3020025000_01.png'),
  (fire, 'https://gbf.wiki/images/c/c3/Npc_zoom_3020025000_02.png')
  ],
  'elmott' : [
  (fire, 'https://gbf.wiki/images/0/00/Npc_zoom_3030023000_01.png'),
  (fire, 'https://gbf.wiki/images/2/21/Npc_zoom_3030023000_02.png'),
  (fire, 'https://gbf.wiki/images/4/45/Npc_zoom_3030083000_01.png'),
  (fire, 'https://gbf.wiki/images/e/e4/Npc_zoom_3030083000_02.png'),
  (fire, 'https://gbf.wiki/images/d/d8/Npc_zoom_3030203000_01.png'),
  (fire, 'https://gbf.wiki/images/a/a9/Npc_zoom_3030203000_02.png')
  ],
  'elta' : [
  (wind, 'https://gbf.wiki/images/7/7b/Npc_zoom_3030025000_01.png'),
  (wind, 'https://gbf.wiki/images/c/c7/Npc_zoom_3030025000_02.png'),
  (light, 'https://gbf.wiki/images/9/99/Npc_zoom_3030244000_01.png'),
  (light, 'https://gbf.wiki/images/d/d5/Npc_zoom_3030244000_02.png')
  ],
  'encrica fontaine' : [
  (light, 'https://gbf.wiki/images/0/03/EricaFontaine_A.png'),
  (light, 'https://gbf.wiki/images/2/25/EricaFontaine_B.png')
  ],
  'erin' : [
  (water, 'https://gbf.wiki/images/4/4c/Npc_zoom_3030164000_01.png'),
  (water, 'https://gbf.wiki/images/0/05/Npc_zoom_3030164000_02.png')
  ],
  'eso' : [
  (wind, 'https://gbf.wiki/images/b/b6/Npc_zoom_3020002000_01.png'),
  (wind, 'https://gbf.wiki/images/7/72/Npc_zoom_3020002000_02.png'),
  (wind, 'https://gbf.wiki/images/7/7b/Npc_zoom_3030128000_01.png'),
  (wind, 'https://gbf.wiki/images/5/56/Npc_zoom_3030128000_02.png')
  ],
  'estarriola' : [
  (wind, 'https://gbf.wiki/images/c/ce/Npc_zoom_3040163000_01.png'),
  (wind, 'https://gbf.wiki/images/b/b6/Npc_zoom_3040163000_02.png')
  ],
  'eugen' : [
  (earth, 'https://gbf.wiki/images/f/f2/Npc_zoom_3030007000_01.png'),
  (earth, 'https://gbf.wiki/images/f/f2/Npc_zoom_3030007000_01.png'),
  (earth, 'https://gbf.wiki/images/9/99/Npc_zoom_3030007000_03.png'),
  (earth, 'https://gbf.wiki/images/9/91/Npc_zoom_3030007000_81.png'),
  (earth, 'https://gbf.wiki/images/a/ae/Npc_zoom_3040077000_01.png'),
  (earth, 'https://gbf.wiki/images/3/3d/Npc_zoom_3040077000_02.png'),
  (earth, 'https://gbf.wiki/images/4/4d/Npc_zoom_3030085000_01.png'),
  (earth, 'https://gbf.wiki/images/6/68/Npc_zoom_3030085000_02.png'),
  (grey, 'https://gbf.wiki/images/9/98/EugenSoiya.png'),
  (grey, 'https://gbf.wiki/images/5/56/Eugen_Gentlemans_Hakama.png'),
  (grey, 'https://gbf.wiki/images/5/5d/Eugen_Mr._Big_Shot.png')
  ],
  'europa' : [
  (water, 'https://gbf.wiki/images/e/e9/Npc_zoom_3040190000_01.png'),
  (water, 'https://gbf.wiki/images/c/c8/Npc_zoom_3040190000_02.png'),
  (water, 'https://gbf.wiki/images/0/0f/Npc_zoom_3040190000_81.png'),
  (water, 'https://gbf.wiki/images/0/0e/Npc_zoom_3040226000_01.png'),
  (water, 'https://gbf.wiki/images/3/33/Npc_zoom_3040226000_02.png')
  ],
  'eustace' : [
  (earth, 'https://gbf.wiki/images/0/0d/Npc_zoom_3040069000_01.png'),
  (earth, 'https://gbf.wiki/images/3/33/Npc_zoom_3040069000_02.png'),
  (dark, 'https://gbf.wiki/images/6/62/Npc_zoom_3040198000_01.png'),
  (dark, 'https://gbf.wiki/images/9/99/Npc_zoom_3040198000_02.png'),
  (earth, 'https://gbf.wiki/images/5/5a/Npc_zoom_3040099000_01.png'),
  (earth, 'https://gbf.wiki/images/0/07/Npc_zoom_3040099000_02.png')
  ],
  'ezecrain' : [
  (fire, 'https://gbf.wiki/images/6/69/Npc_zoom_3030027000_01.png'),
  (fire, 'https://gbf.wiki/images/1/17/Npc_zoom_3030027000_02.png'),
  (light, 'https://gbf.wiki/images/0/05/Npc_zoom_3030210000_01.png'),
  (light, 'https://gbf.wiki/images/0/01/Npc_zoom_3030210000_02.png')
  ],
  'farrah' : [
  (earth, 'https://gbf.wiki/images/1/11/Npc_zoom_3020006000_01.png'),
  (earth, 'https://gbf.wiki/images/b/bb/Npc_zoom_3020006000_02.png'),
  (wind, 'https://gbf.wiki/images/e/ec/Npc_zoom_3030103000_01.png'),
  (wind, 'https://gbf.wiki/images/0/04/Npc_zoom_3030103000_02.png'),
  (earth, 'https://gbf.wiki/images/8/8f/Npc_zoom_3030037000_01.png'),
  (earth, 'https://gbf.wiki/images/5/59/Npc_zoom_3030037000_02.png'),
  (water, 'https://gbf.wiki/images/b/ba/Npc_zoom_3030248000_01.png'),
  (water, 'https://gbf.wiki/images/b/b3/Npc_zoom_3030248000_02.png')
  ],
  'feather' : [
  (light, 'https://gbf.wiki/images/4/45/Npc_zoom_3020020000_01.png'),
  (light, 'https://gbf.wiki/images/4/49/Npc_zoom_3020020000_02.png'),
  (dark, 'https://gbf.wiki/images/9/96/Npc_zoom_3030254000_01.png'),
  (dark, 'https://gbf.wiki/images/0/04/Npc_zoom_3030254000_02.png'),
  (light, 'https://gbf.wiki/images/f/f1/Npc_zoom_3030078000_01.png'),
  (light, 'https://gbf.wiki/images/7/77/Npc_zoom_3030078000_02.png'),
  (light, 'https://gbf.wiki/images/b/bc/Npc_zoom_3030078000_03.png'),
  (light, 'https://gbf.wiki/images/1/16/Npc_zoom_3030078000_81.png')
  ],
  'feena' : [
  (wind, 'https://gbf.wiki/images/d/d6/Npc_zoom_3040061000_01.png'),
  (wind, 'https://gbf.wiki/images/9/93/Npc_zoom_3040061000_02.png'),
  (wind, 'https://gbf.wiki/images/2/25/Npc_zoom_3030035000_01.png'),
  (wind, 'https://gbf.wiki/images/0/0a/Npc_zoom_3030035000_02.png'),
  (light, 'https://gbf.wiki/images/b/b8/Npc_zoom_3030228000_01.png'),
  (light, 'https://gbf.wiki/images/e/e3/Npc_zoom_3030228000_02.png')
  ],
  'feower' : [
  (water, 'https://gbf.wiki/images/4/4c/Npc_zoom_3040033000_01.png'),
  (water, 'https://gbf.wiki/images/a/a4/Npc_zoom_3040033000_02.png'),
  (water, 'https://gbf.wiki/images/1/11/Npc_zoom_3040033000_03.png'),
  (water, 'https://gbf.wiki/images/1/1b/Npc_zoom_3040033000_81.png'),
  (grey, 'https://gbf.wiki/images/8/8f/Bloody-Blood_Stabby_Man_%28Feower%29.png'),
  (grey, 'https://gbf.wiki/images/5/59/Feower_Twins_on_Vacation.png')
  ],
  'ferry' : [
  (light, 'https://gbf.wiki/images/8/8c/Npc_zoom_3030032000_01.png'),
  (light, 'https://gbf.wiki/images/9/9d/Npc_zoom_3030032000_02.png'),
  (dark, 'https://gbf.wiki/images/e/e1/Npc_zoom_3040209000_01.png'),
  (dark, 'https://gbf.wiki/images/8/8e/Npc_zoom_3040209000_02.png'),
  (light, 'https://gbf.wiki/images/e/ec/Npc_zoom_3030101000_01.png'),
  (light, 'https://gbf.wiki/images/c/c9/Npc_zoom_3030101000_02.png'),
  (light, 'https://gbf.wiki/images/f/f0/Npc_zoom_3040073000_01.png'),
  (light, 'https://gbf.wiki/images/b/b6/Npc_zoom_3040073000_02.png'),
  (grey, 'https://gbf.wiki/images/c/cd/Daydreams_of_the_Past_%28Ferry%29.png'),
  (grey, 'https://gbf.wiki/images/b/bf/Ferry%3F.png'),
  (grey, 'https://gbf.wiki/images/6/6d/Santa_Minidress.png'),
  (grey, 'https://gbf.wiki/images/6/62/FerrySora.png'),
  (grey, 'https://gbf.wiki/images/d/df/FerryKimono.png')
  ],
  'fif' : [
  (light, 'https://gbf.wiki/images/3/31/Npc_zoom_3040034000_01.png'),
  (light, 'https://gbf.wiki/images/a/a9/Npc_zoom_3040034000_02.png'),
  (light, 'https://gbf.wiki/images/6/6f/Npc_zoom_3040034000_03.png'),
  (light, 'https://gbf.wiki/images/0/05/Npc_zoom_3040034000_81.png'),
  (light, 'https://gbf.wiki/images/6/65/Npc_zoom_3040034000_82.png'),
  (light, 'https://gbf.wiki/images/d/d8/Fif_Wicked_Witch_of_the_Sweet.png')
  ],
  'flesselles' : [
  (fire, 'https://gbf.wiki/images/f/fb/Npc_zoom_3020049000_01.png'),
  (fire, 'https://gbf.wiki/images/6/6f/Npc_zoom_3020049000_02.png')
  ],
  'forte' : [
  (dark, 'https://gbf.wiki/images/9/9a/Npc_zoom_3040086000_01.png'),
  (dark, 'https://gbf.wiki/images/5/54/Npc_zoom_3040086000_02.png')
  ],
  'fraux' : [
  (fire, 'https://gbf.wiki/images/6/6a/Npc_zoom_3040161000_01.png'),
  (fire, 'https://gbf.wiki/images/3/34/Npc_zoom_3040161000_02.png')
  ],
  'freezie' : [
  (dark, 'https://gbf.wiki/images/d/d2/Npc_zoom_3040182000_01.png'),
  (dark, 'https://gbf.wiki/images/4/46/Npc_zoom_3040182000_02.png')
  ],
  'friday' : [
  (fire, 'https://gbf.wiki/images/9/93/Npc_zoom_3030271000_01.png'),
  (fire, 'https://gbf.wiki/images/e/e1/Npc_zoom_3030271000_02.png')
  ],
  'gachapin' : [
  (wind, 'https://gbf.wiki/images/7/7b/Npc_zoom_3040248000_01.png'),
  (wind, 'https://gbf.wiki/images/9/9a/Npc_zoom_3040248000_02.png'),
  (grey, 'https://gbf.wiki/images/3/32/Gachapin_%26_Mukku_%28Gachapin%29.png')
  ],
  'galadar' : [
  (earth, 'https://gbf.wiki/images/1/13/Npc_zoom_3020004000_01.png'),
  (earth, 'https://gbf.wiki/images/f/f0/Npc_zoom_3020004000_02.png'),
  (earth, 'https://gbf.wiki/images/0/07/Npc_zoom_3030094000_01.png'),
  (earth, 'https://gbf.wiki/images/4/4d/Npc_zoom_3030094000_02.png')
  ],
  'garma' : [
  (earth, 'https://gbf.wiki/images/4/47/Npc_zoom_3020027000_01.png'),
  (earth, 'https://gbf.wiki/images/9/94/Npc_zoom_3020027000_02.png')
  ],
  'gawain' : [
  (wind, 'https://gbf.wiki/images/3/3d/Npc_zoom_3040000000_01.png'),
  (wind, 'https://gbf.wiki/images/6/63/Npc_zoom_3040000000_02.png'),
  (wind, 'https://gbf.wiki/images/6/69/Npc_zoom_3040000000_03.png'),
  (wind, 'https://gbf.wiki/images/0/09/Npc_zoom_3040000000_81.png')
  ],
  'gayne' : [
  (earth, 'https://gbf.wiki/images/3/3d/Npc_zoom_3030009000_01.png'),
  (earth, 'https://gbf.wiki/images/3/3e/Npc_zoom_3030009000_02.png'),
  (earth, 'https://gbf.wiki/images/4/48/Npc_zoom_3030009000_03.png')
  ],
  'geisenborger' : [
  (light, 'https://gbf.wiki/images/f/f1/Npc_zoom_3040162000_01.png'),
  (light, 'https://gbf.wiki/images/f/ff/Npc_zoom_3040162000_02.png')
  ],
  'gemini sunrise' : [
  (fire, 'https://gbf.wiki/images/5/53/GeminiSunrise_A.png'),
  (fire, 'https://gbf.wiki/images/e/e5/GeminiSunrise_B.png')
  ],
  'ghandagoza' : [
  (fire, 'https://gbf.wiki/images/4/4c/Npc_zoom_3040052000_01.png'),
  (fire, 'https://gbf.wiki/images/0/09/Npc_zoom_3040052000_02.png'),
  (fire, 'https://gbf.wiki/images/5/51/Npc_zoom_3040052000_03.png'),
  (fire, 'https://gbf.wiki/images/7/73/Npc_zoom_3030201000_01.png'),
  (fire, 'https://gbf.wiki/images/d/d3/Npc_zoom_3030201000_02.png')
  ],
  'goblin mage' : [
  (wind, 'https://gbf.wiki/images/7/7e/Npc_zoom_3030100000_01.png'),
  (wind, 'https://gbf.wiki/images/b/b5/Npc_zoom_3030100000_02.png'),
  (wind, 'https://gbf.wiki/images/1/17/Npc_zoom_3030100000_81.png')
  ],
  'grea' : [
  (fire, 'https://gbf.wiki/images/2/22/Npc_zoom_3040130000_01.png'),
  (fire, 'https://gbf.wiki/images/b/ba/Npc_zoom_3040130000_02.png'),
  (fire, 'https://gbf.wiki/images/4/4f/Npc_zoom_3030204000_01.png'),
  (fire, 'https://gbf.wiki/images/6/62/Npc_zoom_3030204000_02.png'),
  (water, 'https://gbf.wiki/images/5/55/Npc_zoom_3040179000_01.png'),
  (water, 'https://gbf.wiki/images/1/15/Npc_zoom_3040179000_02.png')
  ],
  'grimnir' : [
  (wind, 'https://gbf.wiki/images/a/aa/Npc_zoom_3040212000_01.png'),
  (wind, 'https://gbf.wiki/images/a/a1/Npc_zoom_3040212000_02.png'),
  (wind, 'https://gbf.wiki/images/9/93/Npc_zoom_3040212000_81.png'),
  (wind, 'https://gbf.wiki/images/d/dc/Npc_zoom_3040261000_01.png'),
  (wind, 'https://gbf.wiki/images/0/06/Npc_zoom_3040261000_02.png'),
  (wind, 'https://gbf.wiki/images/f/ff/Npc_zoom_3040261000_02_1.png')
  ],
  'haaselia' : [
  (water, 'https://gbf.wiki/images/c/ce/Npc_zoom_3040168000_01.png'),
  (water, 'https://gbf.wiki/images/4/47/Npc_zoom_3040168000_02.png')
  ],
  'hallessena' : [
  (earth, 'https://gbf.wiki/images/6/6d/Npc_zoom_3040079000_01.png'),
  (earth, 'https://gbf.wiki/images/1/1a/Npc_zoom_3040079000_02.png'),
  (earth, 'https://gbf.wiki/images/1/10/Npc_zoom_3040079000_03.png'),
  (light, 'https://gbf.wiki/images/9/97/Npc_zoom_3040240000_01.png'),
  (light, 'https://gbf.wiki/images/b/b4/Npc_zoom_3040240000_02.png'),
  (light, 'https://gbf.wiki/images/e/e1/Npc_zoom_3040240000_81.png')
  ],
  'halluel and malluel' : [
  (light, 'https://gbf.wiki/images/6/6a/Halluel_and_Malluel_%28Summer%29_A.png'),
  (light, 'https://gbf.wiki/images/6/6d/Halluel_and_Malluel_%28Summer%29_B.png')
  ],
  'haohmaru' : [
  (wind, 'https://gbf.wiki/images/7/77/Npc_zoom_3030173000_01.png'),
  (wind, 'https://gbf.wiki/images/a/aa/Npc_zoom_3030173000_02.png')
  ],
  'hazen' : [
  (wind, 'https://gbf.wiki/images/f/f0/Npc_zoom_3020009000_01.png'),
  (wind, 'https://gbf.wiki/images/7/71/Npc_zoom_3020009000_02.png'),
  (wind, 'https://gbf.wiki/images/0/0c/Npc_zoom_3030066000_01.png'),
  (wind, 'https://gbf.wiki/images/2/29/Npc_zoom_3030066000_02.png')
  ],
  'helel ben shalem' : [
  (dark, 'https://gbf.wiki/images/c/cf/Npc_zoom_3040251000_01.png'),
  (dark, 'https://gbf.wiki/images/3/3a/Npc_zoom_3040251000_02.png')
  ],
  'heles' : [
  (fire, 'https://gbf.wiki/images/e/e1/Npc_zoom_3040060000_01.png'),
  (fire, 'https://gbf.wiki/images/5/50/Npc_zoom_3040060000_02.png'),
  (light, 'https://gbf.wiki/images/c/c2/Npc_zoom_3040091000_01.png'),
  (light, 'https://gbf.wiki/images/7/79/Npc_zoom_3040091000_02.png'),
  (light, 'https://gbf.wiki/images/8/8d/Npc_zoom_3040091000_91.png'),
  (wind, 'https://gbf.wiki/images/2/23/Npc_zoom_3040208000_01.png'),
  (wind, 'https://gbf.wiki/images/7/7d/Npc_zoom_3040208000_02.png'),
  (grey, 'https://gbf.wiki/images/1/11/Heles_Irestill_Evening_Dress.png')
  ],
  'helnar' : [
  (wind, 'https://gbf.wiki/images/a/a7/Npc_zoom_3030004000_01.png'),
  (wind, 'https://gbf.wiki/images/c/c5/Npc_zoom_3030004000_02.png'),
  (wind, 'https://gbf.wiki/images/5/5f/Npc_zoom_3030004000_03.png'),
  (wind, 'https://gbf.wiki/images/d/d4/Npc_zoom_3030031000_01.png'),
  (wind, 'https://gbf.wiki/images/8/8f/Npc_zoom_3030031000_02.png')
  ],
  'herja' : [
  (earth, 'https://gbf.wiki/images/4/44/Npc_zoom_3020001000_01.png'),
  (earth, 'https://gbf.wiki/images/b/b6/Npc_zoom_3020001000_02.png'),
  (earth, 'https://gbf.wiki/images/c/c5/Npc_zoom_3030175000_01.png'),
  (earth, 'https://gbf.wiki/images/8/81/Npc_zoom_3030175000_02.png')
  ],
  'ilsa' : [
  (earth, 'https://gbf.wiki/images/a/af/Npc_zoom_3040148000_01.png'),
  (earth, 'https://gbf.wiki/images/4/4d/Npc_zoom_3040148000_02.png'),
  (light, 'https://gbf.wiki/images/4/4e/Npc_zoom_3040258000_01.png'),
  (light, 'https://gbf.wiki/images/8/87/Npc_zoom_3040258000_02.png'),
  (fire, 'https://gbf.wiki/images/b/b6/Npc_zoom_3040177000_01.png'),
  (fire, 'https://gbf.wiki/images/6/68/Npc_zoom_3040177000_02.png')
  ],
  'io' : [
  (water, 'https://gbf.wiki/images/8/8e/Npc_zoom_3030006000_01.png'),
  (water, 'https://gbf.wiki/images/a/a1/Npc_zoom_3030006000_02.png'),
  (water, 'https://gbf.wiki/images/4/4b/Npc_zoom_3030006000_03.png'),
  (water, 'https://gbf.wiki/images/f/f5/Npc_zoom_3030006000_81.png'),
  (light, 'https://gbf.wiki/images/f/f6/Npc_zoom_3040065000_01.png'),
  (light, 'https://gbf.wiki/images/0/01/Npc_zoom_3040065000_02.png'),
  (fire, 'https://gbf.wiki/images/7/78/Npc_zoom_3040015000_01.png'),
  (fire, 'https://gbf.wiki/images/0/01/Npc_zoom_3040015000_02.png'),
  (fire, 'https://gbf.wiki/images/5/56/Npc_zoom_3040015000_91.png'),
  (grey, 'https://gbf.wiki/images/b/b1/IoKimono.png'),
  (grey, 'https://gbf.wiki/images/f/ff/Io_Rainbow_Roller.png'),
  ],
  'ippatsu' : [
  (fire, 'https://gbf.wiki/images/9/98/Npc_zoom_3020038000_01.png'),
  (fire, 'https://gbf.wiki/images/d/de/Npc_zoom_3020038000_02.png'),
  (fire, 'https://gbf.wiki/images/b/b1/Npc_zoom_3030232000_01.png'),
  (fire, 'https://gbf.wiki/images/3/3c/Npc_zoom_3030232000_02.png'),
  (fire, 'https://gbf.wiki/images/9/9b/Npc_zoom_3020060000_01.png'),
  (fire, 'https://gbf.wiki/images/7/76/Npc_zoom_3020060000_02.png')
  ],
  'izmir' : [
  (water, 'https://gbf.wiki/images/2/2c/Npc_zoom_3040100000_01.png'),
  (water, 'https://gbf.wiki/images/b/b8/Npc_zoom_3040100000_02.png'),
  (water, 'https://gbf.wiki/images/8/86/Npc_zoom_3040126000_01.png'),
  (water, 'https://gbf.wiki/images/0/04/Npc_zoom_3040126000_02.png')
  ],
  'izuminokami kanesada' : [
  (fire, 'https://gbf.wiki/images/3/33/Npc_zoom_3030205000_01.png'),
  (fire, 'https://gbf.wiki/images/6/68/Npc_zoom_3030205000_02.png')
  ],
  'j.j.' : [
  (light, 'https://gbf.wiki/images/5/59/JJ_A.png'),
  (light, 'https://gbf.wiki/images/6/61/JJ_B.png'),
  (earth, 'https://gbf.wiki/images/0/0e/JJSummer_A.png'),
  (earth, 'https://gbf.wiki/images/1/14/Npc_zoom_3030149000_02.png')
  ],
  'jamil' : [
  (earth, 'https://gbf.wiki/images/7/7e/Npc_zoom_3030134000_01.png'),
  (earth, 'https://gbf.wiki/images/d/d1/Npc_zoom_3030134000_02.png'),
  (dark, 'https://gbf.wiki/images/0/0a/Npc_zoom_3030196000_01.png'),
  (dark, 'https://gbf.wiki/images/1/15/Npc_zoom_3030196000_02.png'),
  (grey, 'https://gbf.wiki/images/e/ed/Raduga_Uniform_%28Jamil%29.png')
  ],
  'jasmine' : [
  (earth, 'https://gbf.wiki/images/6/68/Npc_zoom_3020012000_01.png'),
  (earth, 'https://gbf.wiki/images/b/b0/Npc_zoom_3020012000_02.png'),
  (earth, 'https://gbf.wiki/images/4/44/Npc_zoom_3030102000_01.png'),
  (earth, 'https://gbf.wiki/images/f/f9/Npc_zoom_3030102000_02.png')
  ],
  'jeanne d\'arc' : [
  (light, 'https://gbf.wiki/images/7/7a/Npc_zoom_3040040000_01.png'),
  (light, 'https://gbf.wiki/images/2/28/Npc_zoom_3040040000_02.png'),
  (light, 'https://gbf.wiki/images/b/ba/Npc_zoom_3040040000_03.png'),
  (dark, 'https://gbf.wiki/images/0/04/Npc_zoom_3040080000_01.png'),
  (dark, 'https://gbf.wiki/images/7/7e/Npc_zoom_3040080000_02.png'),
  (dark, 'https://gbf.wiki/images/7/78/Npc_zoom_3040080000_81.png'),
  (light, 'https://gbf.wiki/images/b/ba/Npc_zoom_3040245000_01.png'),
  (light, 'https://gbf.wiki/images/5/51/Npc_zoom_3040245000_02.png'),
  (light, 'https://gbf.wiki/images/6/6c/Npc_zoom_3040245000_81.png'),
  (light, 'https://gbf.wiki/images/e/e2/Npc_zoom_3030195000_01.png'),
  (light, 'https://gbf.wiki/images/9/9e/Npc_zoom_3030195000_02.png'),
  (wind, 'https://gbf.wiki/images/b/b6/Npc_zoom_3040154000_01.png'),
  (wind, 'https://gbf.wiki/images/2/25/Npc_zoom_3040154000_02.png'),
  (grey, 'https://gbf.wiki/images/c/ce/Jeanne_d%27Slack.png'),
  (grey, 'https://gbf.wiki/images/a/a5/Jeanne_d%27Arc_TCG.png')
  ],
  'jessica' : [
  (earth, 'https://gbf.wiki/images/4/4e/Npc_zoom_3030159000_01.png'),
  (earth, 'https://gbf.wiki/images/b/b9/Npc_zoom_3030159000_02.png'),
  (fire, 'https://gbf.wiki/images/9/9a/Npc_zoom_3030016000_01.png'),
  (fire, 'https://gbf.wiki/images/d/d0/Npc_zoom_3030016000_02.png'),
  (fire, 'https://gbf.wiki/images/f/fb/Npc_zoom_3030030000_01.png'),
  (fire, 'https://gbf.wiki/images/7/74/Npc_zoom_3030030000_02.png'),
  (fire, 'https://gbf.wiki/images/e/e7/Npc_zoom_3030030000_91.png'),
  (earth, 'https://gbf.wiki/images/8/86/Npc_zoom_3040227000_01.png'),
  (earth, 'https://gbf.wiki/images/d/d1/Npc_zoom_3040227000_02.png')
  ],
  'jin' : [
  (earth, 'https://gbf.wiki/images/c/c2/Npc_zoom_3040257000_01.png'),
  (earth, 'https://gbf.wiki/images/c/ce/Npc_zoom_3040257000_02.png'),
  (earth, 'https://gbf.wiki/images/d/de/Npc_zoom_3030022000_01.png'),
  (earth, 'https://gbf.wiki/images/0/0b/Npc_zoom_3030022000_02.png'),
  (earth, 'https://gbf.wiki/images/f/f9/Npc_zoom_3030086000_01.png'),
  (earth, 'https://gbf.wiki/images/7/7d/Npc_zoom_3030086000_02.png'),
  (earth, 'https://gbf.wiki/images/4/4d/Npc_zoom_3030178000_01.png'),
  (earth, 'https://gbf.wiki/images/6/68/Npc_zoom_3030178000_02.png'),
  (wind, 'https://gbf.wiki/images/5/55/Npc_zoom_3030151000_01.png'),
  (wind, 'https://gbf.wiki/images/b/b9/Npc_zoom_3030151000_02.png'),
  (grey, 'https://gbf.wiki/images/f/fa/Jin%3F.png')
  ],
  'joel' : [
  (water, 'https://gbf.wiki/images/3/30/Npc_zoom_3020040000_01.png'),
  (water, 'https://gbf.wiki/images/2/23/Npc_zoom_3020040000_02.png')
  ],
  'johann' : [
  (light, 'https://gbf.wiki/images/0/0a/Npc_zoom_3030140000_01.png'),
  (light, 'https://gbf.wiki/images/e/ea/Npc_zoom_3030140000_02.png'),
  (light, 'https://gbf.wiki/images/d/d6/Npc_zoom_3030050000_01.png'),
  (light, 'https://gbf.wiki/images/0/07/Npc_zoom_3030050000_02.png')
  ],
  'joker' : [
  (dark, 'https://gbf.wiki/images/4/44/Npc_zoom_3040173000_01.png'),
  (dark, 'https://gbf.wiki/images/9/9f/Npc_zoom_3040173000_02.png')
  ],
  'joy' : [
  (wind, 'https://gbf.wiki/images/0/0e/Npc_zoom_3030280000_01.png'),
  (wind, 'https://gbf.wiki/images/9/95/Npc_zoom_3030280000_02.png')
  ],
  'juliet' : [
  (light, 'https://gbf.wiki/images/d/d2/Npc_zoom_3040096000_01.png'),
  (light, 'https://gbf.wiki/images/4/4d/Npc_zoom_3040096000_02.png'),
  (light, 'https://gbf.wiki/images/e/e5/Npc_zoom_3040096000_81.png')
  ],
  'juri' : [
  (wind, 'https://gbf.wiki/images/1/1b/Npc_zoom_3030253000_01.png'),
  (wind, 'https://gbf.wiki/images/e/e1/Npc_zoom_3030253000_02.png'),
  (earth, 'https://gbf.wiki/images/e/e3/Npc_zoom_3030038000_01.png'),
  (earth, 'https://gbf.wiki/images/c/c4/Npc_zoom_3030038000_02.png'),
  (grey, 'https://gbf.wiki/images/7/75/Juri_Brigandine.png')
  ],
  'kallen kouzuki' : [
  (fire, 'https://gbf.wiki/images/b/b8/Npc_zoom_3040221000_01.png'),
  (fire, 'https://gbf.wiki/images/2/24/Npc_zoom_3040221000_02.png'),
  (fire, 'https://gbf.wiki/images/8/80/Npc_zoom_3040221000_01_101.png'),
  (fire, 'https://gbf.wiki/images/a/a6/Npc_zoom_3040221000_01_102.png')
  ],
  'kanako mimura' : [
  (earth, 'https://gbf.wiki/images/6/6f/KanakoMimura_A.png'),
  (earth, 'https://gbf.wiki/images/8/81/KanakoMimura_B.png')
  ],
  'kaoru sakuraba' : [
  (water, 'https://gbf.wiki/images/c/ce/KaoruSakuraba_A.png'),
  (water, 'https://gbf.wiki/images/8/83/KaoruSakuraba_B.png')
  ],
  'karin' : [
  (fire, 'https://gbf.wiki/images/b/b1/Npc_zoom_3030125000_01.png'),
  (fire, 'https://gbf.wiki/images/2/2c/Npc_zoom_3030125000_02.png')
  ],
  'karteira' : [
  (wind, 'https://gbf.wiki/images/a/a1/Npc_zoom_3020043000_01.png'),
  (wind, 'https://gbf.wiki/images/1/1c/Npc_zoom_3020043000_02.png'),
  (wind, 'https://gbf.wiki/images/e/ee/Npc_zoom_3030222000_01.png'),
  (wind, 'https://gbf.wiki/images/2/23/Npc_zoom_3030222000_02.png')
  ],
  'karva' : [
  (fire, 'https://gbf.wiki/images/b/bf/Npc_zoom_3020036000_01.png'),
  (fire, 'https://gbf.wiki/images/8/8b/Npc_zoom_3020036000_02.png'),
  (fire, 'https://gbf.wiki/images/e/e7/Npc_zoom_3030230000_01.png'),
  (fire, 'https://gbf.wiki/images/c/c8/Npc_zoom_3030230000_02.png')
  ],
  'karyl' : [
  (dark, 'https://gbf.wiki/images/9/9b/Npc_zoom_3040216000_01.png'),
  (dark, 'https://gbf.wiki/images/b/b3/Npc_zoom_3040216000_02.png')
  ],
  'katalina' : [
  (water, 'https://gbf.wiki/images/9/9b/Npc_zoom_3030005000_01.png'),
  (water, 'https://gbf.wiki/images/8/8a/Npc_zoom_3030005000_02.png'),
  (water, 'https://gbf.wiki/images/c/cf/Npc_zoom_3030005000_03.png'),
  (water, 'https://gbf.wiki/images/9/9f/Npc_zoom_3030005000_81.png'),
  (water, 'https://gbf.wiki/images/d/de/Npc_zoom_3040054000_01.png'),
  (water, 'https://gbf.wiki/images/e/e8/Npc_zoom_3040054000_02.png'),
  (water, 'https://gbf.wiki/images/4/47/Npc_zoom_3040054000_03.png'),
  (dark, 'https://gbf.wiki/images/d/dc/Npc_zoom_3040118000_01.png'),
  (dark, 'https://gbf.wiki/images/b/b4/Npc_zoom_3040118000_02.png'),
  (water, 'https://gbf.wiki/images/1/17/Npc_zoom_3030029000_01.png'),
  (water, 'https://gbf.wiki/images/7/7b/Npc_zoom_3030029000_02.png'),
  (water, 'https://gbf.wiki/images/8/83/Npc_zoom_3030029000_91.png'),
  (grey, 'https://gbf.wiki/images/0/07/Katalina_Festive_Corselet.png'),
  (grey, 'https://gbf.wiki/images/9/99/Katalina%3F.png'),
  (grey, 'https://gbf.wiki/images/9/9c/Katalina_Luck_Be_a_Lady.png'),
  (grey, 'https://gbf.wiki/images/2/29/KatalinaKimono.png')
  ],
  'katzelia' : [
  (wind, 'https://gbf.wiki/images/1/1a/Npc_zoom_3040166000_01.png'),
  (wind, 'https://gbf.wiki/images/3/36/Npc_zoom_3040166000_02.png')
  ],
  'keehar' : [
  (wind, 'https://gbf.wiki/images/1/1d/Npc_zoom_3030024000_01.png'),
  (wind, 'https://gbf.wiki/images/f/fe/Npc_zoom_3030024000_02.png')
  ],
  'kokkoro' : [
  (wind, 'https://gbf.wiki/images/4/40/Npc_zoom_3040201000_01.png'),
  (wind, 'https://gbf.wiki/images/6/63/Npc_zoom_3040201000_02.png')
  ],
  'kolulu' : [
  (dark, 'https://gbf.wiki/images/4/4f/Npc_zoom_3040222000_01.png'),
  (dark, 'https://gbf.wiki/images/1/19/Npc_zoom_3040222000_02.png')
  ],
  'korwa' : [
  (wind, 'https://gbf.wiki/images/4/4a/Npc_zoom_3040081000_01.png'),
  (wind, 'https://gbf.wiki/images/9/94/Npc_zoom_3040081000_02.png'),
  (wind, 'https://gbf.wiki/images/7/7b/Npc_zoom_3030266000_01.png'),
  (wind, 'https://gbf.wiki/images/0/0c/Npc_zoom_3030266000_02.png'),
  (wind, 'https://gbf.wiki/images/9/9f/Npc_zoom_3040127000_01.png'),
  (wind, 'https://gbf.wiki/images/3/32/Npc_zoom_3040127000_02.png')
  ],
  'kou' : [
  (dark, 'https://gbf.wiki/images/d/d0/Npc_zoom_3040242000_01.png'),
  (dark, 'https://gbf.wiki/images/e/e6/Npc_zoom_3040242000_02.png'),
  (dark, 'https://gbf.wiki/images/8/8f/Npc_zoom_3040242000_81.png')
  ],
  'koume shirasaka' : [
  (dark, 'https://gbf.wiki/images/f/f6/KoumeShirasaka_A.png'),
  (dark, 'https://gbf.wiki/images/9/9d/KoumeShirasaka_B.png')
  ],
  'krugne' : [
  (wind, 'https://gbf.wiki/images/f/f1/Npc_zoom_3020035000_01.png'),
  (wind, 'https://gbf.wiki/images/5/50/Npc_zoom_3020035000_02.png'),
  (wind, 'https://gbf.wiki/images/7/75/Npc_zoom_3030278000_01.png'),
  (wind, 'https://gbf.wiki/images/e/e2/Npc_zoom_3030278000_02.png')
  ],
  'kumbhira' : [
  (light, 'https://gbf.wiki/images/f/f3/Npc_zoom_3040197000_01.png'),
  (light, 'https://gbf.wiki/images/4/42/Npc_zoom_3040197000_02.png'),
  (light, 'https://gbf.wiki/images/9/9e/Npc_zoom_3030279000_01.png'),
  (light, 'https://gbf.wiki/images/9/94/Npc_zoom_3030279000_02.png'),
  (light, 'https://gbf.wiki/images/b/b2/Npc_zoom_3030279000_81.png')
  ],
  'la coiffe' : [
  (earth, 'https://gbf.wiki/images/1/1a/Npc_zoom_3020058000_01.png'),
  (earth, 'https://gbf.wiki/images/9/9c/Npc_zoom_3020058000_02.png'),
  (earth, 'https://gbf.wiki/images/4/47/Npc_zoom_3030275000_01.png'),
  (earth, 'https://gbf.wiki/images/3/30/Npc_zoom_3030275000_02.png')
  ],
  'ladiva' : [
  (earth, 'https://gbf.wiki/images/2/27/Npc_zoom_3030055000_01.png'),
  (earth, 'https://gbf.wiki/images/c/c1/Npc_zoom_3030055000_02.png'),
  (light, 'https://gbf.wiki/images/a/a4/Npc_zoom_3030109000_01.png'),
  (light, 'https://gbf.wiki/images/5/51/Npc_zoom_3030109000_02.png'),
  (earth, 'https://gbf.wiki/images/3/32/Npc_zoom_3040217000_01.png'),
  (earth, 'https://gbf.wiki/images/b/b9/Npc_zoom_3040217000_02.png'),
  (earth, 'https://gbf.wiki/images/5/5b/Npc_zoom_3040217000_81.png')
  ],
  'lady grey' : [
  (dark, 'https://gbf.wiki/images/3/38/Npc_zoom_3040005000_01.png'),
  (dark, 'https://gbf.wiki/images/3/32/Npc_zoom_3040005000_02.png'),
  (dark, 'https://gbf.wiki/images/c/c9/Npc_zoom_3040005000_03.png'),
  (dark, 'https://gbf.wiki/images/b/b4/Npc_zoom_3040189000_01.png'),
  (dark, 'https://gbf.wiki/images/5/50/Npc_zoom_3040189000_02.png')
  ],
  'laguna' : [
  (earth, 'https://gbf.wiki/images/6/63/Npc_zoom_3030133000_01.png'),
  (earth, 'https://gbf.wiki/images/6/67/Npc_zoom_3030133000_02.png')
  ],
  'lamretta' : [
  (earth, 'https://gbf.wiki/images/0/05/Npc_zoom_3030013000_01.png'),
  (earth, 'https://gbf.wiki/images/6/6f/Npc_zoom_3030013000_02.png'),
  (fire, 'https://gbf.wiki/images/4/4b/Npc_zoom_3020052000_01.png'),
  (fire, 'https://gbf.wiki/images/4/4c/Npc_zoom_3020052000_02.png'),
  (water, 'https://gbf.wiki/images/2/23/Npc_zoom_3030186000_01.png'),
  (water, 'https://gbf.wiki/images/b/b0/Npc_zoom_3030186000_02.png')
  ],
  'lancelot' : [
  (water, 'https://gbf.wiki/images/1/14/Npc_zoom_3040023000_01.png'),
  (water, 'https://gbf.wiki/images/1/14/Npc_zoom_3040023000_02.png'),
  (water, 'https://gbf.wiki/images/7/76/Npc_zoom_3040023000_03.png'),
  (water, 'https://gbf.wiki/images/6/6f/Npc_zoom_3040023000_81.png'),
  (water, 'https://gbf.wiki/images/0/01/Npc_zoom_3030108000_01.png'),
  (water, 'https://gbf.wiki/images/7/7b/Npc_zoom_3030108000_02.png'),
  (wind, 'https://gbf.wiki/images/9/93/Npc_zoom_3040140000_01.png'),
  (wind, 'https://gbf.wiki/images/4/45/Npc_zoom_3040140000_02.png'),
  (fire, 'https://gbf.wiki/images/b/b9/Npc_zoom_3040191000_01.png'),
  (fire, 'https://gbf.wiki/images/3/3d/Npc_zoom_3040191000_02.png'),
  (earth, 'https://gbf.wiki/images/1/16/Npc_zoom_3030272000_01.png'),
  (earth, 'https://gbf.wiki/images/6/60/Npc_zoom_3030272000_02.png'),
  (grey, 'https://gbf.wiki/images/1/16/Lancelot_Azure_Haori.png'),
  (grey, 'https://gbf.wiki/images/6/69/Black_Dragon_Vice-Captain%27s_Armor_%28Lancelot%29.png'),
  (grey, 'https://gbf.wiki/images/b/b9/LancelotTCG.png'),
  (grey, 'https://gbf.wiki/images/a/aa/Sir_Chainedalot.png'),
  (grey, 'https://gbf.wiki/images/c/c9/Lancelot_The_Dragon_Knights.png')
  ],
  'lecia' : [
  (wind, 'https://gbf.wiki/images/9/98/Npc_zoom_3030072000_01.png'),
  (wind, 'https://gbf.wiki/images/e/ed/Npc_zoom_3030072000_02.png'),
  (wind, 'https://gbf.wiki/images/7/79/Npc_zoom_3030072000_81.png'),
  (wind, 'https://gbf.wiki/images/2/20/Npc_zoom_3040101000_01.png'),
  (wind, 'https://gbf.wiki/images/b/b9/Npc_zoom_3040101000_02.png'),
  (wind, 'https://gbf.wiki/images/5/5d/Npc_zoom_3030087000_01.png'),
  (wind, 'https://gbf.wiki/images/f/fe/Npc_zoom_3030087000_02.png'),
  (wind, 'https://gbf.wiki/images/f/f2/Npc_zoom_3030087000_91.png'),
  (water, 'https://gbf.wiki/images/5/53/Npc_zoom_3040263000_01.png'),
  (water, 'https://gbf.wiki/images/0/04/Npc_zoom_3040263000_02.png'),
  (grey, 'https://gbf.wiki/images/a/ad/Lecia_Skyblue_Sunrise_Kimono.png')
  ],
  'lelouch lamperouge' : [
  (dark, 'https://gbf.wiki/images/2/27/Npc_zoom_3040219000_01.png'),
  (dark, 'https://gbf.wiki/images/a/aa/Npc_zoom_3040219000_02.png'),
  (dark, 'https://gbf.wiki/images/1/1f/Npc_zoom_3040219000_01_101.png'),
  (dark, 'https://gbf.wiki/images/2/28/Npc_zoom_3040219000_01_102.png')
  ],
  'lennah' : [
  (wind, 'https://gbf.wiki/images/d/d9/Npc_zoom_3040021000_01.png'),
  (wind, 'https://gbf.wiki/images/d/d7/Npc_zoom_3040021000_02.png'),
  (wind, 'https://gbf.wiki/images/7/71/Npc_zoom_3040021000_03.png')
  ],
  'leona' : [
  (earth, 'https://gbf.wiki/images/6/69/Npc_zoom_3030241000_01.png'),
  (earth, 'https://gbf.wiki/images/3/3a/Npc_zoom_3030241000_02.png'),
  (earth, 'https://gbf.wiki/images/5/52/Npc_zoom_3030241000_81.png'),
  (water, 'https://gbf.wiki/images/c/c9/Npc_zoom_3030274000_01.png'),
  (water, 'https://gbf.wiki/images/7/7d/Npc_zoom_3030274000_02.png')
  ],
  'leonora' : [
  (wind, 'https://gbf.wiki/images/3/38/Npc_zoom_3020026000_01.png'),
  (wind, 'https://gbf.wiki/images/b/be/Npc_zoom_3020026000_02.png')
  ],
  'levi' : [
  (wind, 'https://gbf.wiki/images/1/18/Npc_zoom_3040142000_01.png'),
  (wind, 'https://gbf.wiki/images/6/61/Npc_zoom_3040142000_02.png')
  ],
  'levin sisters' : [
  (light, 'https://gbf.wiki/images/8/81/Npc_zoom_3040193000_01.png'),
  (light, 'https://gbf.wiki/images/0/0d/Npc_zoom_3040193000_02.png')
  ],
  'lilele' : [
  (water, 'https://gbf.wiki/images/3/3b/Npc_zoom_3040066000_01.png'),
  (water, 'https://gbf.wiki/images/e/e6/Npc_zoom_3040066000_02.png'),
  (water, 'https://gbf.wiki/images/5/5f/Npc_zoom_3030247000_01.png'),
  (water, 'https://gbf.wiki/images/d/d1/Npc_zoom_3030247000_02.png')
  ],
  'lily' : [
  (water, 'https://gbf.wiki/images/e/e6/Npc_zoom_3040007000_01.png'),
  (water, 'https://gbf.wiki/images/2/20/Npc_zoom_3040007000_02.png'),
  (water, 'https://gbf.wiki/images/9/9a/Npc_zoom_3040007000_03.png'),
  (water, 'https://gbf.wiki/images/4/4c/Npc_zoom_3030165000_01.png'),
  (water, 'https://gbf.wiki/images/7/77/Npc_zoom_3030165000_02.png'),
  (grey, 'https://gbf.wiki/images/e/e0/Thawing-Peach_Kimono_%28Lily%29.png')
  ],
  'lina' : [
  (fire, 'https://gbf.wiki/images/e/e8/LinaInverse_A.png'),
  (fire, 'https://gbf.wiki/images/f/f3/LinaInverse_B.png')
  ],
  'lobelia': [
  (earth, 'https://gbf.wiki/images/4/4b/Npc_zoom_3040165000_01.png'),
  (earth, 'https://gbf.wiki/images/2/20/Npc_zoom_3040165000_02.png')
  ],
  'lowain': [
  (dark, 'https://gbf.wiki/images/8/83/Npc_zoom_3020031000_01.png'),
  (dark, 'https://gbf.wiki/images/c/c1/Npc_zoom_3020031000_02.png'),
  (water, 'https://gbf.wiki/images/3/32/Npc_zoom_3030123000_01.png'),
  (water, 'https://gbf.wiki/images/2/20/Npc_zoom_3030123000_02.png'),
  (water, 'https://gbf.wiki/images/b/b1/Npc_zoom_3030123000_03.png'),
  (dark, 'https://gbf.wiki/images/f/fa/Npc_zoom_3020041000_01.png'),
  (dark, 'https://gbf.wiki/images/c/cf/Npc_zoom_3020041000_02.png'),
  (earth, 'https://gbf.wiki/images/d/d9/Npc_zoom_3030252000_01.png'),
  (earth, 'https://gbf.wiki/images/4/49/Npc_zoom_3030252000_02.png')
  ],
  'lucio': [
  (light, 'https://gbf.wiki/images/d/d6/Npc_zoom_3040106000_01.png'),
  (light, 'https://gbf.wiki/images/4/4a/Npc_zoom_3040106000_02.png')
  ],
  'lucius': [
  (dark, 'https://gbf.wiki/images/c/c7/Npc_zoom_3030033000_01.png'),
  (dark, 'https://gbf.wiki/images/1/19/Npc_zoom_3030033000_02.png'),
  (dark, 'https://gbf.wiki/images/8/80/Npc_zoom_3030033000_03.png'),
  (fire, 'https://gbf.wiki/images/2/23/Npc_zoom_3030171000_01.png'),
  (fire, 'https://gbf.wiki/images/0/02/Npc_zoom_3030171000_02.png'),
  (dark, 'https://gbf.wiki/images/2/22/Npc_zoom_3040254000_01.png'),
  (dark, 'https://gbf.wiki/images/f/fa/Npc_zoom_3040254000_02.png')
  ],
  'ludmila': [
  (dark, 'https://gbf.wiki/images/a/a0/Npc_zoom_3030185000_01.png'),
  (dark, 'https://gbf.wiki/images/6/65/Npc_zoom_3030185000_02.png')
  ],
  'luna': [
  (dark, 'https://gbf.wiki/images/0/0d/Npc_zoom_3030180000_01.png'),
  (dark, 'https://gbf.wiki/images/3/33/Npc_zoom_3030180000_02.png')
  ],
  'lunalu': [
  (dark, 'https://gbf.wiki/images/6/66/Npc_zoom_3020050000_01.png'),
  (dark, 'https://gbf.wiki/images/6/6d/Npc_zoom_3020050000_02.png'),
  (dark, 'https://gbf.wiki/images/4/49/Npc_zoom_3040172000_01.png'),
  (dark, 'https://gbf.wiki/images/d/d7/Npc_zoom_3040172000_02.png'),
  (dark, 'https://gbf.wiki/images/5/5b/Npc_zoom_3020061000_01.png'),
  (dark, 'https://gbf.wiki/images/b/bd/Npc_zoom_3020061000_02.png'),
  (grey, 'https://gbf.wiki/images/5/58/Lunalu_Artist%27s_Battle_Armor.png')
  ],
  'lyria' : [
  (grey, 'https://gbf.wiki/images/d/d5/Npc_zoom_3030182000_01.png'),
  (grey, 'https://gbf.wiki/images/c/ce/Npc_zoom_3030182000_02.png'),
  (grey, 'https://gbf.wiki/images/6/64/Battle_Mode_Lyria_%28Lyria%29.png'),
  (grey, 'https://gbf.wiki/images/8/88/Lyria_Cutie_Apron.png'),
  (grey, 'https://gbf.wiki/images/e/e6/Lyria_Daughter_of_Pearl.png'),
  (grey, 'https://gbf.wiki/images/6/6f/Snow_Hopper_%28Lyria%29.png')
  ],
  'monika' : [
  (wind,'https://i.imgur.com/3g2iFbF.png'), # fix links
  (wind,'https://i.imgur.com/qKCZeDu.png'),
  (wind,'https://i.imgur.com/iUkOJnJ.png'),
  (wind,'https://i.imgur.com/mEnmxIV.png'),
  (wind,'https://i.imgur.com/FTaLsbC.png')
  ]
}

names = list(images.keys())
