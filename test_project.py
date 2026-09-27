from performance import calculate_percentage, predict_performance
from risk_analyzer import check_risk


def test_percentage():
    assert calculate_percentage(100) == 50


def test_prediction():
    assert predict_performance(40, 42, 85) == 82.6