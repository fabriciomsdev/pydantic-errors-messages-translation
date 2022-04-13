# Pydantic Errors Messages Translations

It's a collection of translations for pydantic errors in any languages;

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip install pydantic-errors-messages-translations pydantic-i18n
```

## Usage

```python
from pydantic_errors_messages_translations import translations, convert_error_to_human_readable

YOUR_LANGUAGE = 'pt_BR'

error_translation = PydanticI18n(translations, default_locale=YOUR_LANGUAGE)

class User(BaseModel):
    name: str = Field(min_length=40)
    email: str = Field(min_length=24)
    city: str

try:
    wrong_user = User(
        name='Irineu Evangelista de Sousa',
        city= 'Maua'
    )
except ValidationError as e:
    errors_as_dict = error_translation.translate(e.errors(), YOUR_LANGUAGE)
    raise Exception(convert_error_to_human_readable(errors_as_dict)) 
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
