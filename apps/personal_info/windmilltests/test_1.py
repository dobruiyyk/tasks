from windmill.authoring import WindmillTestClient

def test_recordingSuite0():
    client = WindmillTestClient(__name__)

    client.asserts.assertTextIn(xpath=u'/html/body/h2', validator=u'42 Coffee Cups Test Assignment')
    client.asserts.assertTextIn(xpath=u"//div[@id='content']/div[1]/p[1]", validator=u'')
    client.asserts.assertTextIn(xpath=u"//div[@id='content']/div[1]/p[2]", validator=u'')
    client.asserts.assertTextIn(xpath=u"//div[@id='content']/div[1]/p[3]", validator=u'')
    client.asserts.assertTextIn(xpath=u"//div[@id='content']/div[1]/p[4]", validator=u'bio')
    client.asserts.assertTextIn(xpath=u"//div[@id='content']/div[2]/p[1]", validator=u'')
    client.asserts.assertTextIn(xpath=u"//div[@id='content']/div[2]/p[2]", validator=u'Email')
    client.asserts.assertTextIn(xpath=u"//div[@id='content']/div[2]/p[3]", validator=u'Jabber')
    client.asserts.assertTextIn(xpath=u"//div[@id='content']/div[2]/p[4]", validator=u'Skype')
    client.asserts.assertTextIn(xpath=u"//div[@id='content']/div[2]/p[5]", validator=u'Other contacts')