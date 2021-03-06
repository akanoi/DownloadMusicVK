#!/usr/bin/env python
#coding=utf-8


"""
Authorization module.
checkConnection: try open google.com;
getMusicList: return list musics user if data is correct, else empty dict.
"""


import vk
import urllib.request


def checkConnection():
    """ Return True or False. """

    return urllib.request.urlopen('http://google.com', timeout=1)


def getMusicList(login, password, isInvisible):
    """
    login: str;
    password: str;
    isInvisible: boolean, True if set invisible user else False;
    return dict.
    """
    
    if not checkConnection():
        return {}

    session = vk.AuthSession(app_id='5566502', user_login=login,
                             user_password=password, scope='audio')
    api = vk.API(session)

    if isInvisible: 
        api.account.setOffline()

    musics = api.audio.get() or {}
    try:
        return {'%s - %s' % (s['artist'], s['title']): s['url'] for s in musics}
    except Exception as exception:
        raise exception
        return {}
