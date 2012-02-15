from windmill.authoring import WindmillTestClient

def test_recordingSuite0():
    '''windmill ->> '/' - main page test
    '''
    client = WindmillTestClient(__name__)

    client.asserts.assertTextIn(xpath=u"//div[@id='content']/h2", validator=u'42 Coffee Cups Test Assignment')
    client.asserts.assertTextIn(xpath=u"//div[@id='left']/p[1]", validator=u'')
    client.asserts.assertTextIn(xpath=u"//div[@id='left']/p[2]", validator=u'')
    client.asserts.assertTextIn(xpath=u"//div[@id='left']/p[3]", validator=u'')
    client.asserts.assertTextIn(xpath=u"//div[@id='left']/div[2]/p[1]", validator=u'Bio')
    client.asserts.assertTextIn(xpath=u"//div[@id='right']/p[1]", validator=u'')
    client.asserts.assertTextIn(xpath=u"//div[@id='right']/p[2]", validator=u'Email:')
    client.asserts.assertTextIn(xpath=u"//div[@id='right']/p[3]", validator=u'Jabber:')
    client.asserts.assertTextIn(xpath=u"//div[@id='right']/p[4]", validator=u'Skype:')
    client.asserts.assertTextIn(xpath=u"//div[@id='right']/div/p[1]", validator=u'Other contacts:')
 
    client.asserts.assertNode(xpath=u"//div[@id='foot']/p")
    client.asserts.assertNode(link=u'requests')