from windmill.authoring import WindmillTestClient


def test_recordingSuite0():
    '''windmill >> '/requests/' requests page test
    '''
    client = WindmillTestClient(__name__)

    client.waits.sleep(milliseconds=2000)
    client.click(link=u'requests')
    client.waits.forPageLoad(timeout=u'20000')

    client.asserts.assertTextIn(xpath=u"//div[@id='content']/p[1]",
                                validator=u'127.0.0.1')
    client.asserts.assertTextIn(xpath=u"//div[@id='content']/p[2]",
                                validator=u'127.0.0.1')
    client.asserts.assertTextIn(xpath=u"//div[@id='content']/p[3]",
                                validator=u'127.0.0.1')
    client.asserts.assertTextIn(xpath=u"//div[@id='content']/p[4]",
                                validator=u'127.0.0.1')
    client.asserts.assertTextIn(xpath=u"//div[@id='content']/p[5]",
                                validator=u'127.0.0.1')
    client.asserts.assertTextIn(xpath=u"//div[@id='content']/p[6]",
                                validator=u'127.0.0.1')
    client.asserts.assertTextIn(xpath=u"//div[@id='content']/p[7]",
                                validator=u'127.0.0.1')
    client.asserts.assertTextIn(xpath=u"//div[@id='content']/p[8]",
                                validator=u'127.0.0.1')
    client.asserts.assertTextIn(xpath=u"//div[@id='content']/p[9]",
                                validator=u'127.0.0.1')
    client.asserts.assertTextIn(xpath=u"//div[@id='content']/p[10]",
                                validator=u'127.0.0.1')
    client.click(link=u'main page')
    client.waits.forPageLoad(timeout=u'20000')
    client.waits.forElement(link=u'requests', timeout=u'8000')
    client.click(link=u'requests')
    client.waits.forPageLoad(timeout=u'20000')
