# -*- coding: utf-8 -*-

from local_wecfg_example import CARDID, OPENID, WECHAT
from pywe_custom_message.customsg import (CustomMessage, add_kfaccount, custom_typing, del_kfaccount, get_kflist,
                                          send_custom_articles_message, send_custom_card_message,
                                          send_custom_image_message, send_custom_message, send_custom_mpnews_message,
                                          send_custom_news_message, send_custom_text_message, send_custom_video_message,
                                          send_custom_voice_message, send_custom_wxa_message, update_kfaccount,
                                          upload_headimg)


class TestCustomsgCommands(object):

    def test_send_custom_card_message(self):
        appid = WECHAT.get('JSAPI', {}).get('appID')
        appsecret = WECHAT.get('JSAPI', {}).get('appsecret')

        customsg = CustomMessage(appid=appid, secret=appsecret)
        res = customsg.send_custom_card_message(OPENID, CARDID)
        assert isinstance(res, dict)
        assert res['errcode'] == 0

    def test_custom_typing(self):
        appid = WECHAT.get('JSAPI', {}).get('appID')
        appsecret = WECHAT.get('JSAPI', {}).get('appsecret')

        res = custom_typing(OPENID, typing=True, appid=appid, secret=appsecret)
        assert isinstance(res, dict)
        assert res['errcode'] == 0
