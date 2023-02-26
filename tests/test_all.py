import country_emoji as ce


def test_all() -> None:
    assert ce.flag('CL') == '🇨🇱'
    assert ce.code('🇨🇦') == 'CA'
    assert ce.name('🇶🇦') == 'Qatar'
    assert ce.flag('Taiwan number one!') == '🇹🇼'
    assert ce.flag('Congo and Burma') == ''

    assert ce.flag('Republic of Tanzania') == '🇹🇿'
    assert ce.flag('Tanzania, United Republic of') == '🇹🇿'
    assert ce.code('Australia') == 'AU'
    assert ce.code('UAE') == 'AE'
    assert ce.name('AE') == 'United Arab Emirates'
    assert ce.code('UK') == 'GB'

    assert ce.flag(ce.name(ce.flag(ce.code(ce.flag(ce.name('NZ')))))) == '🇳🇿'
