

# RFC: Choosing a Framework for TherapistFlow

| Field | Value |
|---|---|
| Author | Lea Hajj |
| Team | 54 |
| Date | October 25, 2026 |
| Status | Proposed |
| Decision Date | Not yet decided |
| Deciders | TherapistFlow Development Team and Project Partner |

## 1. Problem and Context

TherapistFlow is a scheduling and wellness application designed to help therapists and supervisors manage their workloads and prevent burnout. The main goal of this project is to help therapists create healthier work schedules by tracking their mood, logging client sessions, and understanding how their workload affects their well being. Based on our team's story map, the application will allow users to complete daily mood surveys, view their schedules, and see their burnout risk levels. We are also considering additional features, such as workload warnings, reminders, and recommendations to help therapists balance their schedules.

One important decision our team needs to make is which framework we should use to build TherapistFlow. We have been discussing two main approaches: Streamlit and React with FastAPI. Streamlit is designed to make building web applications with Python easier, while React and FastAPI allow developers to build the frontend and backend separately. Since our project involves scheduling, mood tracking, and workload analysis, we need a framework that supports these features while remaining manageable for our team.

This decision matters because the framework we choose will affect how we develop the application throughout the project. If we choose a framework that does not support our needs, we may have to spend extra time changing our code later. Switching frameworks would be easier now because we are still in the planning stage, but it would become more difficult once we begin building major features. If we do not make a decision soon, we could also lose valuable time that should be spent developing and testing the application.

## 2. Options

### Option A: Streamlit

Streamlit is an open source Python framework that allows developers to build interactive web applications without writing much frontend code. This could be useful for our team because it would allow us to create a working prototype more quickly. For example, we could use Streamlit to build a mood survey, display workload information, and show burnout risk levels.

One advantage of Streamlit is that it includes built in tools for displaying charts and collecting user input. This could reduce the amount of time our team spends creating basic interface elements. Since most of the application could be written in Python, our team could also avoid managing a separate JavaScript frontend.

The main disadvantage is that creating a highly customized scheduling interface may require additional work. Streamlit also reruns application code during many user interactions, meaning we would need to manage the application's state carefully [1].

Streamlit would be the appropriate choice if our team prioritizes developing a simple, working prototype quickly and determines that its interface capabilities are sufficient for TherapistFlow.

### Option B: React and FastAPI

React is a JavaScript library used to build user interfaces, while FastAPI is a Python framework used to create backend APIs [2][3]. With this approach, React would handle the parts of TherapistFlow that users interact with, such as calendars, mood surveys, and workload dashboards. FastAPI would handle backend tasks such as processing information, validating inputs, and calculating workload levels.

One advantage of this approach is that it gives us more control over the application's design and organization. React supports reusable components, allowing our team to organize the calendar, mood tracker, and burnout analysis into separate interface elements. FastAPI would allow us to organize backend processes independently.

The main disadvantage is that React and FastAPI require more initial setup and coordination. Our team would need to understand how the frontend communicates with the backend, which could increase development time at the beginning. We would also need to manage dependencies and ensure that information moves correctly between both parts of the application.

React and FastAPI would be the appropriate choice if our team determines that the additional flexibility and separation between frontend and backend justify the extra development effort.

### Option C: Do Nothing

The third option is to continue planning without choosing a framework yet. This would allow our team to spend more time discussing the project requirements with our partner before committing to a specific technology.

The main advantage is that we could avoid choosing a framework too early. We could focus on understanding the features we need, designing the application, and deciding how users should interact with it.

The disadvantage is that postponing the decision would delay development. Without an established technical approach, team members could also begin planning features differently, making it harder to combine their work later.

Doing nothing would be reasonable if our project requirements were still changing significantly. Since we have already identified several important features, delaying the decision for too long could create unnecessary challenges.

## 3. Analysis

The following analysis compares Streamlit, React with FastAPI, and postponing the decision across five important technical considerations: performance, complexity, maintainability, security, and cost.

### Performance

Streamlit reruns application code during many user interactions, while React uses components to manage interface updates and FastAPI handles backend requests [1][2][3]. These differences could affect how quickly TherapistFlow responds when users add sessions, enter their mood, or view workload information.

React and FastAPI may provide more flexibility when handling complex interactions because the frontend and backend operate separately. Streamlit could still perform well for a simpler application, particularly if our initial features do not require complicated interface updates.

Our team has not tested either approach yet, so we cannot confidently determine which would perform better. We would need to create small prototypes and compare their responsiveness before making a final decision.

### Complexity

Streamlit may be simpler to develop because most of the application can be written in Python. This could make it easier for our team to get started and reduce the amount of setup required.

React and FastAPI would require us to manage two separate parts of the application. Our team would need to understand frontend components, backend APIs, and how information moves between them. This adds complexity but may also help organize the application as it grows.

Postponing the decision would avoid this initial setup, but it could create more work later if our team develops features without agreeing on a consistent technical structure.

### Maintainability

Streamlit could be easier to maintain for a smaller application because it allows developers to work primarily in Python. As the application becomes more interactive, we would need to organize its code and state carefully.

React and FastAPI could help our team separate responsibilities. For example, if we need to change how burnout risk is calculated, we could update the backend without redesigning the entire user interface. React's reusable components could also make it easier to maintain consistent interface elements.

Neither approach automatically guarantees maintainable code. Our team would still need to follow consistent development practices and review changes before merging them.

### Security

Security and privacy are important because TherapistFlow may eventually involve sensitive information about therapists' moods, schedules, and workloads. Our Team Charter states that private information must remain confidential and that fictional data should be used during testing.

Both framework options would require us to protect user information and carefully manage access to it. React and FastAPI would also require us to consider how information is transferred between the frontend and backend.

Our story map includes questions about whether administrators should be able to access certain information. We need to confirm those requirements with our project partner before designing the system. Neither framework automatically solves every security concern.

### Cost

Streamlit, React, and FastAPI are open source technologies, meaning they do not require framework licensing fees for ordinary use. Hosting, additional libraries, and other services may still create costs.

Streamlit could reduce initial development time because it requires less setup. React and FastAPI may take longer to learn and configure, but they could provide greater flexibility as the application becomes more complex.

Since our team has not measured development time or hosting expenses, we cannot determine which option would be cheaper overall. The most important cost for our team may be the time required to learn, develop, test, and maintain the application.

### Overall Comparison

| Consideration | Streamlit | React + FastAPI | Do Nothing |
|---|---|---|---|
| Performance | Suitable for basic interactive applications; state needs attention | More control over frontend and backend behavior | No consistent approach established |
| Complexity | Less initial setup | More initial setup and coordination | Delays technical planning |
| Maintainability | Simpler for smaller Python applications | Clearer separation of frontend and backend | May create inconsistent development |
| Security | Requires appropriate data protection | Requires frontend, backend, and API security | Security approach remains undecided |
| Cost | Potentially faster initial development | Greater initial learning and setup effort | Delays development and may increase rework |

Based on our current project goals, I believe React and FastAPI may be the better long term option. The additional flexibility could be useful for TherapistFlow's scheduling and workload features, but our team should test both approaches before making a final decision.

## 4. Recommendation and Verification Plan

I recommend that our team move forward with React and FastAPI as our preferred option while keeping the final decision open until we receive approval from our project partner.

I believe this combination would be a good fit for TherapistFlow because our application involves several interactive features, including scheduling, mood tracking, and workload analysis. React would allow us to design a more customized interface, while FastAPI would help us organize backend processes.

Before officially choosing this approach, our team should create a small prototype using React and FastAPI and compare it with a basic Streamlit version. Both prototypes should include the same simple features and use fictional data.

### Proposed Prototype Requirements

Each prototype should allow a user to enter a daily mood, add a fictional client session, view workload information, and receive a warning when a fictional workload passes a chosen limit.

### Acceptance Criteria

The following criteria are proposed for comparing the prototypes. Our team has not completed these tests yet.

| Test | Proposed Acceptance Criteria |
|---|---|
| Mood tracking | A user can enter a mood and see it saved correctly |
| Session scheduling | A user can add a fictional session and view it in the schedule |
| Workload calculation | Workload information updates correctly after adding a session |
| Risk warnings | A warning appears when the workload passes a defined test threshold |
| Accuracy | At least five fictional workload examples produce expected results |
| Team review | At least two team members review each prototype |

We should also record how long each prototype takes to develop, whether the interface is easy to use, and any technical problems we experience. These results would help us determine whether React and FastAPI provide enough benefits to justify their additional complexity.

After testing, our team should discuss the results and share them with our project partner. If React and FastAPI meet our requirements and the team feels comfortable using them, we can officially select that approach. If Streamlit meets our needs more efficiently, we should reconsider our recommendation.

## 5. Constraints

### Licensing

Streamlit, React, and FastAPI are open source technologies. We still need to check the licenses of any additional tools or libraries we use, such as calendar components or notification services. Our team must make sure these dependencies are compatible with the project's requirements and that we follow any applicable license conditions.

### Data Use and Confidentiality

TherapistFlow is designed for mental health professionals and may eventually contain sensitive information about their schedules, moods, and workloads. Our Team Charter requires us to keep private information confidential and avoid including passwords, credentials, or API keys in our repository.

Our team should use fictional information when developing and testing the application. Before working with real user information, we would need to confirm the privacy and access requirements with our project partner.

### Intellectual Property

Our team also needs to confirm any ownership or intellectual property requirements established by our project partner. These details have not been fully established in the documents provided, so they should be discussed before we make long term commitments.

The framework we select does not independently determine ownership of our original application code, but we must comply with the licensing requirements of any third party technologies we use.

### Team and Partner Constraints

Our project partner must approve major decisions before we implement them. We also need to consider our team's experience and the time available to complete the project. Choosing a framework that requires too much learning or setup could slow down development, so we need to make sure the benefits are worth the extra work.

## 6. Delegation and Validation

Our project partner has encouraged us to use AI tools to help with documentation and development. Our team has also created a context file to guide how AI tools are used throughout the project.

I used Claude AI to help with grammar and organization.

The official documentation for Streamlit, React, and FastAPI provides references for checking the technical information. One specific claim discussed in this RFC is that Streamlit reruns application code when users interact with widgets, which could affect how we manage information in TherapistFlow. Streamlit's documentation explains this behavior and describes tools for managing session state [1]. React and FastAPI also provide official documentation explaining their frontend and backend capabilities [2][3]. These sources support the technical comparison but cannot confirm which framework will work best for our project without testing.

### Existing Checks and Future Validation

Our team has not built or tested either framework yet, so we cannot confirm which option will work better for TherapistFlow. Before making a final decision, we plan to create small prototypes using fictional data and test whether users can enter their mood, add sessions, and view workload information correctly.

We will also check whether workload calculations are accurate and warnings appear when expected. Any AI generated code will need to be reviewed and tested before being added to the project. Our team will use code reviews and quality checks before merging changes, with automated tests added when available.

If a change causes problems, we will fix it or return to the previous working version. The final decision will be based on testing results, team discussions, and approval from our project partner. AI assistance will not replace the team's responsibility for reviewing evidence and making the final decision.

## Decision

Status: Proposed

At this stage, I recommend using React for the frontend and FastAPI for the backend of TherapistFlow.

I believe this approach offers the flexibility we need to build a scheduling and wellness application with several interactive features. The decision is still open because our team needs to test the options and receive approval from our project partner.

If testing shows that Streamlit is a better fit for our available time and project requirements, we should be willing to change our recommendation.

Once the team reaches an agreement, this RFC should be updated to record the final decision, decision date, and participating team members.

## References

1. Streamlit. Session State. https://docs.streamlit.io/develop/concepts/architecture/session-state

2. React. Official React Documentation. https://react.dev/learn

3. FastAPI. Official FastAPI Documentation. https://fastapi.tiangolo.com/features/

4. Streamlit. App Model Summary. https://docs.streamlit.io/get-started/fundamentals/summary

5. Team 54. Team Charter. Fall 2026.

6. Team 54. TherapistFlow Story Map. Fall 2026.
