import requests
import pytest

graphql_endpoint = 'https://rickandmortyapi.com/graphql'

query_get_location = """query {
  character(id:1){
    location{
      name
    }
  }
}"""

def test_get_location_name():
    response = requests.post(graphql_endpoint, json={"query": query_get_location})

    print(response.json())


query_get_episode_name = """query {
  episode(id:1){
    name
  }
}"""


def test_get_episode_name():
    response = requests.post(graphql_endpoint, json={"query": query_get_episode_name})
    print(response.json())


# 1. Установить MONGODB
# 2. Установить Oracledb
# Потренироваться и написать пару тестов на GraphQL и тоже сделать параметризировать
# 3. автоматизировать Delete an item in the cart    Get all orders и  single order параметризировать
