# https://www.dataquest.io/blog/streaming-data-python/
# https://www.pyxll.com/blog/a-real-time-twitter-feed-in-excel/

import tweepy, asyncio

backup_msg_en = " :Battle Id\nI need backup!\nLvl"
backup_msg_jp = " :参戦ID\n参加者募集！\nLv"
id_length = 8

class Raidfinder(tweepy.StreamListener):
  def __init__(self, api, ctx, raid_listeners, loop):
    tweepy.StreamListener.__init__(self, api)
    self.ctx = ctx
    self.raid_listeners = raid_listeners
    self.loop = loop
    self.stream = tweepy.Stream(auth=api.auth, listener=self)
    self.stream.filter(track=[backup_msg_en, backup_msg_jp], is_async=True)

  def on_status(self, status):
    if status.source_url == 'http://granbluefantasy.jp/':
      tweet_txt = status.text.split('\n')
      raid_name = tweet_txt[len(tweet_txt)-2]
      print(raid_name)

      if raid_name in self.raid_listeners:
        end_idx = status.text.find(backup_msg_jp)
        if end_idx == -1:
          end_idx = status.text.find(backup_msg_en)
        raid_id = status.text[end_idx-id_length:end_idx]

        full_msg = ' '.join([user.mention for user in self.raid_listeners[raid_name]])
        full_msg += ' **' + raid_name + '** ' + raid_id

        asyncio.run_coroutine_threadsafe(self.ctx.send(full_msg), self.loop)
