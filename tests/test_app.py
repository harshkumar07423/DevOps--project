import pytest

from app import app


@pytest.fixture()
def client():
    app.config.update(TESTING=True)
    with app.test_client() as test_client:
        yield test_client


def test_home_page_loads(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"BrainCheck" in response.data


def test_quiz_page_contains_all_questions(client):
    response = client.get("/quiz")
    assert response.status_code == 200
    assert response.data.count(b"question-card") == 5


def test_result_scores_submitted_answers(client):
    answers = {f"question_{question_id}": "0" for question_id in range(1, 6)}
    response = client.post("/result", data=answers)
    assert response.status_code == 200
    assert b"100%" in response.data


def test_health_endpoint(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json == {"status": "ok"}