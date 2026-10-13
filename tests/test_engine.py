from core.engine import estimate_feasibility, validate_input

def sample(**changes):
    data = {"study_target":100,"estimated_eligible_cohort":300,"site_count":5,
            "monthly_recruitment_per_site":2,"activation_delay_months":1,"planning_horizon_months":12}
    data.update(changes)
    return data

def test_valid_input():
    assert validate_input(sample()) == []

def test_missing_input_flagged():
    item = sample()
    del item["site_count"]
    assert any("site_count" in error for error in validate_input(item))

def test_negative_value_rejected():
    assert any("non-negative" in error for error in validate_input(sample(monthly_recruitment_per_site=-1)))

def test_whole_number_constraints():
    assert any("whole number" in error for error in validate_input(sample(site_count=2.5)))

def test_capacity_calculation():
    result = estimate_feasibility(sample())
    assert result["projected_recruitment_capacity"] == 110

def test_coverage_capped_at_100():
    result = estimate_feasibility(sample(monthly_recruitment_per_site=100))
    assert result["target_coverage_percent"] == 100.0

def test_eligible_cohort_flag():
    result = estimate_feasibility(sample(estimated_eligible_cohort=20))
    assert any("eligible cohort" in flag for flag in result["operational_flags"])

def test_not_guaranteed():
    assert estimate_feasibility(sample())["is_guaranteed_forecast"] is False
