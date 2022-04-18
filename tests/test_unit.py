from typing import List
from pydantic import BaseModel, Field, ValidationError
from pydantic_i18n import PydanticI18n

from pydantic_errors_messages_translations import translations, convert_error_to_human_readable

error_translation = PydanticI18n(translations, default_locale='pt_BR')


class User(BaseModel):
    name: str = Field(min_length=40)
    email: str = Field(min_length=24)
    sex: str

def test_should_return_errors_with_translation():
    expected_errors_list = [
        {
            'loc': ('name',), 
            'msg': 'Este campo precisa ter menos que 40 caracteres', 
            'type': 'value_error.any_str.min_length', 
            'ctx': {'limit_value': 40}
        }, 
        {
            'loc': ('email',), 
            'msg': 'Campo Obrigatório', 
            'type': 'value_error.missing'
        }, 
        {
            'loc': ('sex',), 
            'msg': 'Campo Obrigatório', 
            'type': 'value_error.missing'
        }
    ]

    try:
        User(name='Milton Friedman')
    except ValidationError as e:
        errors_translated = error_translation.translate(e.errors(), 'pt_BR')
        
        assert expected_errors_list == errors_translated


def test_should_format_pydantic_exceptions_in_a_human_readable_away():
    clear_results = lambda phrase: phrase.replace(' ', '').replace('\n', '')

    expected_msg = """
        name:
            - Este campo precisa ter menos que 40 caracteres
        
        email:
            - Campo Obrigatório
        
        sex:
            - Campo Obrigatório
    """
    try:
        User(name='Luiz Gama, the abolicionist')
    except ValidationError as e:
        errors_translated = error_translation.translate(e.errors(), 'pt_BR')
        msg = convert_error_to_human_readable(errors_translated)

        assert clear_results(msg) == clear_results(expected_msg)