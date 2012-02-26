from windmill.authoring import WindmillTestClient


def test_MainPageElements():
    client = WindmillTestClient(__name__)

    client.click(link=u'login')
    client.waits.forPageLoad(timeout=u'20000')
    client.type(text=u'admin', id=u'id_username')
    client.click(value=u'login')
    client.waits.forPageLoad(timeout=u'20000')
    client.waits.forElement(timeout=u'8000', id=u'id_password')
    client.click(id=u'id_password')
    client.type(text=u'admin', id=u'id_password')
    client.click(value=u'login')
    client.waits.forPageLoad(timeout=u'20000')
    client.waits.forElement(timeout=u'8000', id=u'id_name')
    client.click(id=u'id_name')
    client.type(text=u'dk', id=u'id_name')
    client.click(id=u'submit-id-save_changes')
    client.waits.forPageLoad(timeout=u'20000')
    client.waits.forElement(xpath=u"//div[@id='left']/p[1]", timeout=u'8000')
    client.asserts.assertTextIn(xpath=u"//div[@id='left']/p[1]",
                                validator=u'dk')


def test_LoginRedirectForm():
    '''windmill ->> '/' - main page test
    '''
    client = WindmillTestClient(__name__)

    client.asserts.assertTextIn(xpath=u"//div[@id='content']/h2",
                                validator=u'42 Coffee Cups Test Assignment')

    client.asserts.assertNode(link=u'Change info')

    client.asserts.assertTextIn(xpath=u"//div[@id='left']/p[1]",
                                validator=u'')
    client.asserts.assertTextIn(xpath=u"//div[@id='left']/p[2]",
                                validator=u'')
    client.asserts.assertTextIn(xpath=u"//div[@id='left']/p[3]",
                                validator=u'')
    client.asserts.assertTextIn(xpath=u"//div[@id='left']/div[2]/p[1]",
                                validator=u'Bio')
#    client.asserts.assertTextIn(xpath=u"//div[@id='right']/p[1]",
#                                validator=u'')
    client.asserts.assertTextIn(xpath=u"//div[@id='right']/p[1]",
                                validator=u'Email:')
    client.asserts.assertTextIn(xpath=u"//div[@id='right']/p[2]",
                                validator=u'Jabber:')
    client.asserts.assertTextIn(xpath=u"//div[@id='right']/p[3]",
                                validator=u'Skype:')
    client.asserts.assertTextIn(xpath=u"//div[@id='right']/div/p[1]",
                                validator=u'Other contacts:')

    client.asserts.assertNode(xpath=u"//div[@id='foot']/p")
    client.asserts.assertNode(link=u'requests')


def test_FormReversed():
    client = WindmillTestClient(__name__)

    client.click(link=u'Change info')
    client.waits.forPageLoad(timeout=u'20000')
    client.waits.forElement(xpath=u"//form[@id='id-PersonChange']/fieldset/h3",
                            timeout=u'8000')
    client.click(xpath=u"//form[@id='id-PersonChange']/fieldset/h3")
    client.click(xpath=u"//div[@id='div_id_bio']/label")
    client.click(id=u'id_bio')
    client.click(xpath=u"//div[@id='div_id_birth']/label")
    client.click(id=u'id_birth')
    client.click(xpath=u"//div[@id='div_id_last_name']/label")
    client.click(id=u'id_last_name')
    client.click(xpath=u"//div[@id='div_id_name']/label")
    client.click(id=u'id_name')
    client.click(xpath=u"//div[@id='div_id_other_contacts']/label")
    client.click(id=u'id_other_contacts')
    client.click(xpath=u"//div[@id='div_id_skype']/label")
    client.click(id=u'id_skype')
    client.click(xpath=u"//div[@id='div_id_jabber']/label")
    client.click(id=u'id_jabber')
    client.click(xpath=u"//div[@id='div_id_email']/label")
    client.click(id=u'id_email')
    client.asserts.assertNode(id=u'div_id_bio')
    client.asserts.assertNode(id=u'div_id_birth')
    client.asserts.assertNode(id=u'div_id_last_name')
    client.asserts.assertNode(id=u'div_id_name')