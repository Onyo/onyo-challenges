import functools
import re
from collections import namedtuple

import requests
from cachetools import TTLCache, cached
from django.conf import settings

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
    cep = ''.join(c for c in cep if c.isnumeric())
    cep_info = _get_cep(cep)
    city_info = _get_city(cep_info.city)
    state_info = _get_state(city_info.state)
    return cep_info._replace(city=city_info._replace(state=state_info))


@cached(cache=TTLCache(maxsize=1024, ttl=2 * 60 * 60))
def _get_cep(cep):
    session = create_request_session()
    cep = session.get(f'{settings.CEP_URL}/cep/{cep}')
    cep.raise_for_status()
    json = cep.json()
    del json['url']
    return Cep(**json)


@cached(cache=TTLCache(maxsize=1024, ttl=2 * 60 * 60))
def _get_city(city_url):
    session = create_request_session()
    city = session.get(city_url)
    city.raise_for_status()
    json = city.json()
    del json['url']
    return City(**json)


@cached(cache=TTLCache(maxsize=1024, ttl=2 * 60 * 60))
def _get_state(state_url):
    session = create_request_session()
    state = session.get(state_url)
    state.raise_for_status()
    json = state.json()
    del json['url']
    return State(**json)
