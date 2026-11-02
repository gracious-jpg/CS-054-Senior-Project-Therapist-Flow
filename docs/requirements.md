# Problem Statement
Clinicians and Clinic supervisors need a fast and practical way to observe and manage their workload distrubution. The quantity of a clinician's workload may not accurately reflect the complexity and demands required for their work. TherapistOverflow aims to let Clinicians record and monitor their unique workflow, and provide informed action plans whenever possible. **Evidence to Validate**: this problem framing comes from the team's current project scope; the team still needs partner interviews or workflow observations to document the present process, frequency of problems, and measurable baseline.


# Functional Requirements
## Information is access-controlled
A user can view their own workload record, but cannot retrieve the workload of another clinician. **Acceptance**: Clinician A is not an Admin. Clinician A may access Clinican A's workload records, but has no access to Clinician B's workload records.

## Supervisors have administrative access.
A supervisor has an administrative view, but may only view workload records assigned to their supervision. **Acceptance**: Supervisor A is assigned Group A. Supervisor A may view any clinician records within Group A, but is denied access to workload records from any other group.

## System accepts valid values into database.
A user with authorized access can create and update supported workload-factor values for reporting period. **Acceptance**: Valid values are saved to databases and can be seen on refresh. Invalid values or unsupported formatting is not accepted and rejected with a visible indicator.

## A Flag must be understandable.
When a flag is presented to the authorized user, the user must also be able to view factor values that contribute to that flag. **Acceptance**: Clinician A is able to identify all factor values that contribute to the indicated flag.

# Non-Functional Requirements
## Users can access their data from phone and desktop
The primary workload-entry and dashboard workflows work without horizontal page scrolling at viewport widths of 375 px and 1280 px. Verification: Browser viewport checks and manual completion of both workflows at each width.

## Workload information is sensitive
Protected API enforces server-side authorization.

## Usable content can be viewed quickly
The dashboard for supervisors and clinicians load within three seconds.


# Constraints
## Delivery meets Course requirements
The project must meet Oregon State University's capstone deliverable, review, and handoff expectations.

## Not listed as external constraints
React, Express

# Success Metrics
These are proposed pilot targets to confirm with the partner before collecting data. A metric is met only if its stated target is reached using its stated collection method.
1. Supervisor recognition: At least 80% of participating supervisors identify the highest-workload clinician in a seeded scenario within 60 seconds, without hints. Collection: timed, moderated usability tasks; record participants and the scenario.
2. Workload entry: At least 80% of participating clinicians can update one reporting period's factor values in 5 minutes or less, without facilitator intervention. Collection: timed usability tasks; use a fixed scenario with agreed fields.
3. Comparison effort: The median time for supervisors to identify clinicians needing workload review is at least 30% lower with TherapistFlow than with their current workflow. Collection: have the same participants complete comparable tasks using both methods; document the baseline and task order.

If real-world piloting and tests are not available, section will be changed under Project Partner's advice and guidance.

# References
[OSU CAPSTONE REQUIREMENTS](https://capstone.alexulbrich.com/guides/requirements/)