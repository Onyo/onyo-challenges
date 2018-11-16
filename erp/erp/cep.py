import functools
import re
from collections import namedtuple

import requests
from cachetools import TTLCache, cached
from django.conf import settings

_CEP_REGEX_VALIDATOR = re.compile(r'^(\d\d\.\d\d\d-\d\d\d|\d\d\d\d\d-\d\d\d|\d\d\d\d\d\d\d\d)$')

Cep = namedtuple('Cep', ['cep', 'public_place', 'neighborhood', 'city'])
City = namedtuple('City', ['name', 'state'])
State = namedtuple('State', ['name', 'acronym'])


@functools.lru_cache()
def create_request_session():
    session = requests.Session()
    session.headers.update({'Accept': 'application/json'})
    return session


@cached(cache=TTLCache(maxsize=1024, ttl=2 * 60 * 60))
def get_address_from_cep(cep):
    if cep is None:
        return None

    if not _CEP_REGEX_VALIDATOR.match(cep):
        return ValueError('the cep value should be formated by these masks: ##.###-###, #####-### or #########')

    cep = ''.join(c for c in cep if c.isnumeric())

    cep_info = _get_cep(cep)
    if cep_info is None:
        return None
    city_info = _get_city(cep_info.city)
    if city_info is None:
        return None
    state_info = _get_state(city_info.state)
    if state_info is None:
        return None

    return cep_info._replace(city=city_info._replace(state=state_info))


@cached(cache=TTLCache(maxsize=1024, ttl=2 * 60 * 60))
def _get_cep(cep):
    session = create_request_session()
    cep = session.get(f'{settings.CEP_URL}/cep/{cep}')
    if cep.status_code != 200:
        return None
    json = cep.json()
    del json['url']
    return Cep(**json)


@cached(cache=TTLCache(maxsize=1024, ttl=2 * 60 * 60))
def _get_city(city_url):
    session = create_request_session()
    city = session.get(city_url)
    if city.status_code != 200:
        return None
    json = city.json()
    del json['url']
    return City(**json)


@cached(cache=TTLCache(maxsize=1024, ttl=2 * 60 * 60))
def _get_state(state_url):
    session = create_request_session()
    state = session.get(state_url)
    if state.status_code != 200:
        return None
    json = state.json()
    del json['url']
    return State(**json)
