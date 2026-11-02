Objective: Deliver a therapist scheduler with reliable scheduling, balanced workload, AI advice, and appropriate user access. Ratings show likelihood/impact: H \= High, M \= Medium, L \= Low.

R-1: AI Service Failures — Technical, M/M (AI requests can fail; therapists may not receive suggestions). The AI generates action plans with suggestions for therapists. Slow, failed, or unusable responses could prevent therapists from receiving these plans. Owner: Tzu Chu Jih. Mitigate: Limit waiting time, check responses, and show an error message with a retry option while keeping other features available. Trigger: An action plan fails to load or contains an empty or unreadable response.

R-2 Scheduling Conflicts — Technical, M/H (multiple users can schedule sessions; conflicts disrupt appointments). Two people scheduling at the same time could create overlapping sessions or exceed workload limits. Owner: Quinton Gonzales. Mitigate: Check and save bookings in one operation, and test bookings made at the same time. Trigger: The system accepts two conflicting bookings. 

R-3 Lost Data — Technical, M/H (surveys and schedules must be saved; lost records require re-entry). A failed save or database change could erase survey responses or appointments. Owner: Gracious Cunningham. Mitigate: Test saving and retrieving records, and back up data. Trigger: A saved record disappears or changes unexpectedly.

R-4 Incorrect Time Handling — Technical, M/H (sessions depend on exact times; mistakes cause missed appointments). Different time zones or daylight saving changes could make sessions appear at the wrong time. Owner: Lea Hajj. Mitigate: Use consistent time storage, display the time zone, and test time changes. Trigger: A session appears at a different time from the one intended.

