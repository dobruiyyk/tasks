from windmill.authoring import WindmillTestClient

def test_recordingSuite0():
    '''windmill ->> '/requests/' page test
    '''
    client = WindmillTestClient(__name__)

    client.asserts.assertTextIn(xpath=u"//div[@id='content']/div[1]/p[1]", validator=u'request')
    client.asserts.assertTextIn(xpath=u"//div[@id='content']/div[1]/p[2]", validator=u'request')
    client.asserts.assertTextIn(xpath=u"//div[@id='content']/div[1]/p[3]", validator=u'request')
    client.asserts.assertTextIn(xpath=u"//div[@id='content']/div[1]/p[4]", validator=u'request')
    client.asserts.assertTextIn(xpath=u"//div[@id='content']/div[1]/p[5]", validator=u'request')
    client.asserts.assertTextIn(xpath=u"//div[@id='content']/div[1]/p[6]", validator=u'request')
    client.asserts.assertTextIn(xpath=u"//div[@id='content']/div[1]/p[7]", validator=u'request')
    client.asserts.assertTextIn(xpath=u"//div[@id='content']/div[1]/p[8]", validator=u'request')
    client.asserts.assertTextIn(xpath=u"//div[@id='content']/div[1]/p[9]", validator=u'request')
    client.asserts.assertTextIn(xpath=u"//div[@id='content']/div[1]/p[10]", validator=u'request')