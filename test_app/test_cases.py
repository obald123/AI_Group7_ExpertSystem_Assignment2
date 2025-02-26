# test_cases.py

def test_drought_classification():
    assessment = DroughtRiskAssessment([30, 40, 20, 10, 50], 15, [28, 32, 35, 30, 29])
    assert assessment.classify_drought() == "Severe"

def test_soil_moisture_evaluation():
    assessment = DroughtRiskAssessment([100, 120, 110], 15, [28, 32, 35])
    assert assessment.evaluate_soil_moisture() == "Irrigation recommended"

def test_temperature_evaluation():
    assessment = DroughtRiskAssessment([100, 120, 110], 25, [28, 32, 35])
    assert assessment.evaluate_temperature() == "High temperature may exacerbate drought conditions"

# Run tests
test_drought_classification()
test_soil_moisture_evaluation()
test_temperature_evaluation()
print("All tests passed!")