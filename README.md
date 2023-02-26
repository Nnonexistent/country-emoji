# country-emoji
[![GA test](https://github.com/nnonexistent/country-emoji/actions/workflows/test.yml/badge.svg)](https://github.com/Nnonexistent/country-emoji/actions)
[![PyPI](https://img.shields.io/pypi/v/country-emoji)](https://pypi.org/project/country-emoji/)
[![License](https://img.shields.io/pypi/l/country-emoji)](./LICENSE)
[![PyPI - Format](https://img.shields.io/pypi/format/country-emoji)](https://pypi.org/project/country-emoji/)

Converts between country names, ISO 3166-1 codes and flag emojis. **Has zero dependencies.**

Inspired by [JavaScript version](https://www.npmjs.com/package/country-emoji) by [meeDamian](https://github.com/meeDamian)

## Install

```
$ pip install country-emoji
```

## Usage

```python
import country_emoji as ce

ce.flag('CL')  # '🇨🇱'

ce.code('🇨🇦')  # 'CA'

ce.name('🇶🇦')  # 'Qatar'

# can extract name from string...
ce.flag('Taiwan number one!')  # '🇹🇼'

# ...but only if there's no ambiguity
ce.flag('Congo and Burma')  # ''

ce.flag('Republic of Tanzania')  # '🇹🇿'

ce.flag('Tanzania, United Republic of')  # '🇹🇿'

ce.code('Australia')  # 'AU'

ce.code('UAE')  # 'AE'

ce.name('AE')  # 'United Arab Emirates'

ce.code('UK')  # 'GB'

# all values can be converted back and forth indefinitely
ce.flag(ce.name(ce.flag(ce.code(ce.flag(ce.name('NZ'))))))  # '🇳🇿'
```

### Don't want Python?

Check out the following:

* **JavaScript:** [country-emoji](https://github.com/meeDamian/country-emoji)
* **Swift:** [SwiftFlags](https://github.com/BubiDevs/SwiftFlags)
* **Rust:** [country-emoji](https://github.com/leodutra/country-emoji) [[crates.io](https://crates.io/crates/country-emoji)]

PS. Happy to add more here :)

## Bugs and feedback

If you discover a bug please report it [here](https://github.com/Nnonexistent/country-emoji/issues).
