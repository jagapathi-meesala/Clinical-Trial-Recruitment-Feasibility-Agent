# Explainability

## Inputs
The agent accepts study target, aggregate estimated eligible participants, number of participating sites, expected monthly recruitment per active site, activation delay in months, and a planning horizon. No patient-level data is needed or supported.

## Decision
Projected recruitment capacity is `max(0, planning_horizon_months - activation_delay_months) × active_sites × monthly_recruitment_per_site`. Estimated coverage is capped at 100% for the target. A simple capacity check highlights whether the supplied assumptions meet the target within the horizon.

## Limits
This is a transparent arithmetic screening aid, not a validated prediction model or statistical power analysis. Real recruitment depends on protocol criteria, referral pathways, competition, consent rates, retention, site performance, ethics approvals, and local context. Aggregate eligible-cohort estimates may be uncertain.

## Tool: validate-feasibility-input
### Inputs and Data Sources
One aggregate, de-identified feasibility input object.
### Decision and Reasoning
Checks required numeric fields, ranges, and non-negative counts.
### Outputs and Evidence
Returns field-level validation errors or a valid status.
### Limits and Constraints
Cannot verify the quality or representativeness of supplied aggregate estimates.
### Failure Handling
Invalid inputs are returned with explicit errors and excluded from calculations.
### Human Review
Confirm assumptions with investigators, site coordinators, and protocol documentation.

## Tool: estimate-recruitment-feasibility
### Inputs and Data Sources
Validated aggregate study target, eligible cohort, sites, recruitment rate, activation delay, and planning horizon.
### Decision and Reasoning
Calculates projected capacity and target coverage using the documented formula.
### Outputs and Evidence
Returns capacity, coverage, timeline estimate, and operational flags.
### Limits and Constraints
Does not model stochastic variation, screening failure, dropout, or retention unless reflected in user-supplied conservative rates.
### Failure Handling
Rejects missing or implausible fields.
### Human Review
Review feasibility with site teams; do not use the estimate as a guarantee.

## Tool: prepare-feasibility-summary
### Inputs and Data Sources
The calculated feasibility result and its assumptions.
### Decision and Reasoning
Formats the estimate, risks, and review prompts into a structured summary.
### Outputs and Evidence
Returns a JSON-ready summary for internal review.
### Limits and Constraints
Does not submit regulatory documents or make protocol decisions.
### Failure Handling
Reports malformed summary inputs.
### Human Review
Qualified research staff must approve conclusions and any external use.
