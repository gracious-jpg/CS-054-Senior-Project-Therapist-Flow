# Design

## Overview
TherapistFlow helps therapists and supervisors spot when a clinician’s workload is becoming difficult to manage. Therapists can view their schedules, complete daily check-ins, and see how their workload is classified as safe, warning, or danger. Supervisors can use a dashboard to identify who may need support or a scheduling adjustment. These categories describe workload, not a therapist’s health or ability to practice.

The first release will focus on scheduling, daily surveys, and workload tracking. Workload calculations will work without an AI service. AI-generated action plans are a later addition.

## Architecture
![C4 context diagram](./diagrams/context.png)
- Web app (React, Netlify): schedules, surveys, workload analysis, action plans.
- API (FastAPI, Oracle Cloud VM): scheduling rules, workload calculations, AI integration.
- SQLite 3, on the VM: therapist and administrator accounts, sessions, daily survey responses, therapist preferences.
- AI (model TBD): suggests action plans based on daily survey responses.

## Interfaces
The React frontend will send HTTPS requests to the FastAPI backend and exchange data in JSON. FastAPI will validate requests, enforce access permissions, and calculate workload results. The frontend will display those results and will not connect directly to SQLite.
## Data
SQLite stores therapist and administrator accounts, scheduled sessions, daily survey responses, and therapist preferences. Sessions, responses, and preferences are linked to the therapist’s account.

## Deployment
Netlify hosts the React frontend. FastAPI and SQLite run on an Oracle Cloud VM.

After deployment, submit a test survey from the frontend and reload it to verify that the API saved it to SQLite.

## Open questions
How will therapist and administrator accounts be created and managed?

How will we make sure therapist information and survey responses are kept private and secure?

Which AI model or service will we use to generate suggested action plans?

How will we test the connection between the React frontend, FastAPI backend, and SQLite database?

How will we make sure the workload calculations and AI suggestions are accurate and useful?

## Deferred decisions
AI integration: We will focus on getting the main features working before choosing and fully integrating an AI service.

Notifications: We will decide later whether therapists should receive reminders or alerts about their workload.

Database scaling: We will use SQLite for now and consider a larger database if the application needs to support more users.

Additional features: We will prioritize scheduling, daily surveys, and workload tracking before adding more advanced features.


