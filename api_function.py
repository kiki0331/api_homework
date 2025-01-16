from typing import Tuple
import requests
import allure
import logging
from api_structure import ShortenResponse, ImageInfo, ErrorResponse

@allure.step('verified_status_code')
def verified_statuscode(actual_status_code, expected_status_code):
    assert actual_status_code == expected_status_code, f"Expected status code {
        expected_status_code}, but got {actual_status_code}"


@allure.step('verified_response_data')
def verified_response_data(response_data, verified_data):
    assert verified_data in response_data, f"response is {
        response_data} , didn't contain {verified_data}"


@allure.step('get api api/breeds/image/random')
def dog_image() -> Tuple[ImageInfo, int]:
    api_url = "https://dog.ceo/api/breeds/image/random"
    response = requests.get(api_url)
    logging.info(f"status code: {response.status_code}")
    logging.info(f"response: {response.text}")
    imageinfo = response.json()
    return ImageInfo(**imageinfo), response.status_code


@allure.step('post api api/v1/shorten')
def shorten_api(payload) -> Tuple[ShortenResponse, int]:
    api_url = "https://cleanuri.com/api/v1/shorten"
    logging.info(f"send POST: {api_url}")
    response = requests.post(api_url, json=payload)
    logging.info(f"status code: {response.status_code}")
    logging.info(f"response: {response.text}")
    shortenresponse = response.json()
    if response.status_code == 200:
        return ShortenResponse(**shortenresponse), response.status_code
    return ErrorResponse(**shortenresponse), response.status_code
