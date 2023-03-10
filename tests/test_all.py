import country_emoji as ce


def test_all() -> None:
    assert ce.flag('CL') == 'π¨π±'
    assert ce.code('π¨π¦') == 'CA'
    assert ce.name('πΆπ¦') == 'Qatar'
    assert ce.flag('Taiwan number one!') == 'πΉπΌ'
    assert ce.flag('Congo and Burma') == ''

    assert ce.flag('Republic of Tanzania') == 'πΉπΏ'
    assert ce.flag('Tanzania, United Republic of') == 'πΉπΏ'
    assert ce.code('Australia') == 'AU'
    assert ce.code('UAE') == 'AE'
    assert ce.name('AE') == 'United Arab Emirates'
    assert ce.code('UK') == 'GB'

    assert ce.flag(ce.name(ce.flag(ce.code(ce.flag(ce.name('NZ')))))) == 'π³πΏ'
