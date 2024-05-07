import pytest
from Base.Libraries.API_Base import Methods
from Base.Elements.Data.dataobjects import Objects
from Base.Libraries.logging import logger
import jsonschema
import json
import os

c = 0
print("Current working directory:", os.getcwd())


@pytest.fixture
def response():
    global c
    met = Methods()
    obj = Objects(r"Base/Elements/Data/data.json")
    obj.read_data()
    payload = obj.data[c]
    res = met.post(data=payload)
    obj.data[c]["id"] = res.json()["id"]
    obj.write_data()
    yield res
    c += 1


@pytest.mark.api
def test_post_request_status_code(response, log):
    log.logger.info("tested status code")
    assert response.status_code == 201, f"Unexpected status code: {response.status_code}"


@pytest.mark.api
def test_post_request_response_time(response, log):
    log.logger.info("tested response time")
    assert response.elapsed.total_seconds() < 5, "Response time exceeds 1 second"


@pytest.mark.api
def test_post_request_content_type(response, log):
    log.logger.info("tested context type")
    assert response.headers["Content-Type"].startswith("application/json"), "Unexpected Content-Type"


@pytest.mark.api
def test_post_request_body_size(response, log):
    log.logger.info("tested body size")
    assert len(response.content) < 1024, "Response body size exceeds 1024 bytes"


@pytest.mark.api
def test_post_request_json_schema_validation(response, log):
    try:
        with open(r"Base/Elements/Data/data.schema.json", 'r') as schema_file:
            schema = json.load(schema_file)

        json_response = response.json()
        jsonschema.validate(instance=json_response, schema=schema)
        log.logger.info("tested json schema")
    except (jsonschema.ValidationError, jsonschema.SchemaError) as e:
        pytest.fail(f"JSON schema validation failed: {e}")
    except ValueError:
        pytest.fail("Error parsing response JSON")
    except FileNotFoundError:
        pytest.fail("Schema file data.schema.json not found")