import allure
from api_function import verified_statuscode, verified_response_data, dog_image, shorten_api


@allure.title("test get image api")
@allure.description("Verifies api camn get image successfully and return the correct status code.")
def test_dog_image():
    response, status_code = dog_image()
    verified_statuscode(status_code, 200)
    verified_response_data(response.message, "https://images.dog.ceo/")


@allure.title("test shorten_api")
@allure.description("Verifies api camn get shorten_api successfully and return the correct status code.")
def test_shorten_api():
    payload = {"url": "https://www.afternic.com/forsale/catboys.com?utm_source=TDFS_DASLNC&utm_medium=parkedpages&utm_campaign=x_corp_tdfs-daslnc_base&traffic_type=TDFS_DASLNC&traffic_id=daslnc&"}
    response, status_code = shorten_api(payload)
    verified_statuscode(status_code,200)
    verified_response_data(response.result_url, "https://cleanuri.com")

@allure.title("test shorten_api payload is failed")
@allure.description("Verifies api camn get shorten_api successfully and return the correct status code.")
def test_shorten_api_payload_failed():
    payload = {"url": 123}
    response, status_code = shorten_api(payload)
    verified_statuscode(status_code,400)
