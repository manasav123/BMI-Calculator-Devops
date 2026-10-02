from app import app

def test_bmi_calculation():
    client = app.test_client()

    response = client.post("/", data={
        "height": "170",
        "weight": "65"
    })

    assert response.status_code == 200
    assert b"22.49" in response.data
    assert b"Normal Weight" in response.data