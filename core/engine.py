"""Aggregate clinical-trial recruitment feasibility screening."""
from typing import Any

REQUIRED = ("study_target", "estimated_eligible_cohort", "site_count",
            "monthly_recruitment_per_site", "activation_delay_months", "planning_horizon_months")

def validate_input(data: dict[str, Any]) -> list[str]:
    errors = []
    for key in REQUIRED:
        if key not in data:
            errors.append(f"Missing required field: {key}")
    for key in REQUIRED:
        if key in data:
            value = data[key]
            if not isinstance(value, (int, float)) or isinstance(value, bool):
                errors.append(f"{key} must be numeric")
            elif value < 0:
                errors.append(f"{key} must be non-negative")
    for key in ("study_target", "site_count", "planning_horizon_months"):
        if key in data and isinstance(data[key], (int, float)) and not isinstance(data[key], bool) and data[key] <= 0:
            errors.append(f"{key} must be greater than zero")
    for key in ("site_count", "activation_delay_months", "planning_horizon_months"):
        if key in data and isinstance(data[key], (int, float)) and not float(data[key]).is_integer():
            errors.append(f"{key} must be a whole number")
    return errors

def estimate_feasibility(data: dict[str, Any]) -> dict[str, Any]:
    errors = validate_input(data)
    if errors:
        return {"valid": False, "validation_errors": errors}
    active_months = max(0, data["planning_horizon_months"] - data["activation_delay_months"])
    capacity = active_months * data["site_count"] * data["monthly_recruitment_per_site"]
    coverage = min(100.0, round(capacity / data["study_target"] * 100, 2))
    flags = []
    if data["activation_delay_months"] >= data["planning_horizon_months"]:
        flags.append("No active recruitment months remain within the planning horizon.")
    if data["estimated_eligible_cohort"] < data["study_target"]:
        flags.append("Estimated eligible cohort is below the study target.")
    if capacity < data["study_target"]:
        flags.append("Projected recruitment capacity is below the study target.")
    if data["monthly_recruitment_per_site"] == 0:
        flags.append("Monthly recruitment rate is zero; confirm site assumptions.")
    return {
        "valid": True,
        "study_target": data["study_target"],
        "estimated_eligible_cohort": data["estimated_eligible_cohort"],
        "projected_recruitment_capacity": round(capacity, 2),
        "target_coverage_percent": coverage,
        "estimated_capacity_gap": round(max(0, data["study_target"] - capacity), 2),
        "active_recruitment_months": active_months,
        "operational_flags": flags,
        "assumptions": [
            "Monthly recruitment rates are user-supplied aggregate estimates.",
            "All sites are assumed to recruit at the same rate after activation.",
            "No stochastic variation, screening failure, retention, or dropout model is applied."
        ],
        "is_guaranteed_forecast": False
    }
