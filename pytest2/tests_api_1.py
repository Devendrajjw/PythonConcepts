import pytest
from make_requests import make_req


class TestClass:
    def test_search_asteriods_with_success(self):
        api_key = "DEMO_KEY"
        response = make_req(api_key)
        assert response.status_code == 200
        data = response.json()
        assert len(data) > 0
        assert data['absolute_magnitude_h'] > 0
