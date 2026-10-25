# RFC: Frontend Framework Selection for TherapistFlow

| Field | Value |
| --- | --- |
| Author | Quinton Gonzales |
| Date | 2026-10-25 |
| Status | Proposed |
| Decision Date | Not yet decided |
| Deciders | TherapistFlow Development Team (pending) |
| Superseded By | N/A |

## Problem and Context

TherapistFlow is a mobile application intended to help therapists, clinicians, and mental health organizations manage workload burnout. The application's primary functions require users to provide workload factors, including a session calendar and daily mood tracker, to evaluate their workload. The application will also provide adjustable burnout sensitivity to help users recognize when they are approaching an unsustainable workload threshold.

To accomplish this, TherapistFlow requires a user-friendly and interactive frontend capable of presenting schedules, clinician information, workload calculations, and risk classifications. Users should have no difficulty navigating between these features, adjusting relevant inputs, and understanding their workload burnout analysis. Before beginning substantial frontend development, our team must decide which frontend framework to use. Early prototypes provided by our project partner have shown React as a potential choice, but our team has not yet finalized this decision.

This decision is important because the frontend framework we choose influences how our application is structured. Factors such as application state, reusable components, and dependencies become closely tied to the selected technology. Choosing a frontend framework also requires our team to dedicate time and resources to understanding how it works. Changing frameworks after substantial development could require significant modifications to the codebase. Timing is especially important because we need to evaluate our alternatives before making long-term architectural commitments.

If we do not make this decision, our development may proceed without an established frontend architecture. This could create significant problems as additional features are introduced. Team members may develop different approaches to organizing components, managing application state, and handling user interactions. As a result, the application could become increasingly difficult to maintain. Making this decision early would allow our team to establish consistent development practices before the frontend becomes more complex.

## Options

### Option A: React

React is a popular JavaScript library known for its reusable interface components. One of its primary benefits is that developers can create individual components while sharing common interface elements throughout an application.

For TherapistFlow, React could allow our team to separate features such as the session calendar, mood tracker, and burnout risk classifications into individual components. This could make development more organized and allow team members to work on separate features without unnecessarily interfering with one another.

The primary cost of using React involves learning how to use it. Each member of our team has expressed having little to no experience with React. This means we would need to dedicate additional development time to learning concepts such as JSX, hooks, and state management. We may also need to adopt supporting libraries for functionality that React does not provide by itself.

React would be the appropriate choice if its component structure and available resources outweigh the time required for our team to become familiar with it.

### Option B: Vue

Vue is a JavaScript framework that supports single-file components containing templates, application logic, and styling. It uses syntax similar to HTML, which may make it easier for developers familiar with traditional web development to understand.

The main potential benefit of Vue is reducing the amount of time our team spends learning a frontend framework. Since our team has experience with HTML and JavaScript, Vue's template structure may feel more familiar than React's JSX syntax.

Vue also supports reusable components and reactive application data, making it capable of handling TherapistFlow's interactive features.

The primary cost of using Vue is learning its framework-specific conventions and determining which supporting tools are compatible with our application. We would also need to evaluate whether Vue offers any meaningful advantages over React for our particular requirements.

Vue would be the appropriate choice if our team determines that its syntax and development approach allow us to implement the required features more efficiently.

### Option C: Do Nothing

Our final option is to postpone the decision and continue working on the application without committing to a frontend framework.

The main benefit of this approach is saving time in the immediate future. Instead of spending time evaluating and learning a framework, our team could focus on developing functionality using technologies we already understand.

However, the primary cost of postponing this decision is the increased risk of inconsistencies throughout the application. Without an established framework or common architectural approach, different developers may implement similar features in different ways.

Additional code may also need to be rewritten if our team eventually adopts a framework that does not support our existing implementation.

Doing nothing would be a reasonable choice if the application's requirements were still changing significantly or if our existing prototype already provided a maintainable solution without a framework. However, this option becomes less attractive as the application grows.

## Analysis

The following analysis compares React, Vue, and the decision to continue without a framework across five important technical considerations: performance, complexity, maintainability, security, and cost.

### Performance

- **React:** React uses a component-based rendering system that updates the interface whenever relevant application state changes. This would be especially useful for real-time adjustments to workload factors and burnout sensitivity. However, poorly optimized component re-rendering can affect performance as the application grows. React provides optimization features that can help reduce unnecessary rendering [1].

- **Vue:** Vue uses a reactive system that tracks changes to application data and updates the relevant interface components. This could efficiently support TherapistFlow's workload calculations and scheduling features. However, we do not yet know whether Vue would provide a noticeable performance advantage over React for our project's scope [2].

- **Nothing:** For a relatively simple application, having no frontend framework could reduce the amount of JavaScript required during initial loading. However, additional features would require our team to manage interface updates manually. Poorly implemented updates could reduce performance as the application becomes more complex.

The performance differences between these approaches have not yet been tested using TherapistFlow. Therefore, we cannot confidently conclude which option would perform best.

### Complexity

- **React:** React introduces a structured development approach using concepts such as state management, components, and hooks. These features could help organize TherapistFlow's functionality, but they would require additional learning. Our team may also need supporting dependencies for routing and other frontend features.

- **Vue:** Vue uses HTML-like templates that may provide a simpler learning experience for our team. However, we would still need to learn Vue's coding conventions, component structure, and reactivity system. Its relative simplicity would need to be evaluated through practical development.

- **Nothing:** Postponing our decision temporarily eliminates the need to learn a new framework. However, as additional features are introduced, our team would need to establish its own methods for managing application state and updating interface elements. This could eventually increase complexity.

Because our team has limited experience with React, learning time is an important consideration. We need to determine whether adopting a framework will save enough development time later to justify the initial investment.

### Maintainability

- **React:** React supports reusable components, allowing team members to work independently while maintaining consistent interface elements. For TherapistFlow, this could simplify the maintenance of features such as scheduling and burnout analysis. However, inconsistent component design and poorly organized state management could still create maintainability problems.

- **Vue:** Vue also supports reusable components that allow team members to work independently while maintaining stylistic consistency. Its single-file component structure keeps related code together. However, maintainability would still depend primarily on the coding conventions followed by our team members.

- **Nothing:** Without a framework, each team member would be responsible for following a consistent organizational convention. Any significant differences in implementation could result in complicated application logic and maintenance difficulties. Our team would need to establish and enforce these conventions independently.

Both React and Vue could improve maintainability by encouraging reusable components. However, neither framework guarantees maintainable code without consistent development practices.

### Security

- **React:** React provides protections against certain scripting vulnerabilities through its handling of content during normal rendering. However, these protections do not eliminate all security risks. Additional research and testing would be necessary to ensure sensitive information is handled properly.

- **Vue:** Like React, Vue includes protections when rendering content through its standard template system. However, it cannot replace the authentication and authorization measures that must be enforced by our backend. Additional security practices would still be required.

- **Nothing:** Without a framework, our team would be directly responsible for safely handling and displaying application content. Improper handling of user-provided data could introduce security vulnerabilities.

Since TherapistFlow may handle sensitive information, security is particularly important. Regardless of our frontend choice, access to protected data must be controlled by the backend. We should not assume that choosing React or Vue automatically makes the application secure.

### Cost

- **React:** React is available under the MIT license, meaning there is no licensing fee to use it. The primary expenses would be development time spent learning React, configuring dependencies, and maintaining the application.

- **Vue:** Vue is also available under the MIT license and does not require a licensing fee. Its primary costs would similarly involve learning the framework and maintaining supporting dependencies. Vue could potentially reduce initial development time if our team finds its syntax easier to understand.

- **Nothing:** Continuing without a framework would have no additional framework licensing or setup costs. However, the time required to manually implement and maintain functionality could increase as the application becomes more complex.

Overall, licensing costs are unlikely to be the deciding factor. The more significant cost is the amount of development time required for each option.

## Recommendation and Verification Plan

I recommend adopting React as the frontend library for TherapistFlow.

React was the initial framework suggested in the project description, and its component-based architecture appears suitable for visualizing our application's workload management features. It would allow us to organize the session calendar, mood tracker, and burnout analysis into reusable components.

Although Vue may provide an easier learning experience, we do not currently have enough evidence to determine whether it would be more efficient for our team. React remains a reasonable starting recommendation because it has extensive documentation and provides the functionality required for our application's interface.

Before committing to React, our team should develop a small frontend prototype using artificial data.

The prototype should contain:

- Workload information for clinicians.
- Illustrative burnout risk classifications.
- Artificial data representing at least three different clinicians.
- Navigation between at least two application views.
- Adjustable workload factors that update the displayed risk classifications.

The purpose of this prototype is to evaluate whether React meets our application's requirements and whether our team can develop with it effectively.

### Acceptance Criteria

We will use Google's Core Web Vitals as a reference for evaluating the performance of the web-based interface [3].

The proposed performance criteria are:

| Metric | Acceptance Criteria |
| --- | --- |
| Largest Contentful Paint (LCP) | 2.5 seconds or less |
| Interaction to Next Paint (INP) | Less than 200 milliseconds |
| Cumulative Layout Shift (CLS) | Less than 0.1 |

These metrics evaluate loading performance, responsiveness, and visual stability. They apply to web interfaces; if TherapistFlow is developed as a native mobile application, we will need to establish appropriate mobile-specific performance measurements.

Our prototype should also satisfy the following functional requirements:

1. All three artificial clinician records must display correctly.
2. Users must be able to navigate between the two application views.
3. Adjusting workload sensitivity must produce the expected risk classifications.
4. The interface must remain functional without displaying unexpected errors.

The team should test these requirements before committing to React as the established frontend architecture.

If the prototype fails to meet these expectations or proves too difficult for our team to maintain, we should reconsider Vue or another approach before proceeding with substantial frontend development.

## Constraints

### Licensing

React and Vue are both available under the MIT license, which allows broad use and modification as long as the required copyright and license notices are preserved.

Any additional libraries introduced during development must be evaluated separately to ensure their licensing requirements are compatible with our project.

By postponing our framework decision, we may also postpone evaluating the licenses of dependencies we eventually adopt.

### Data Use and Confidentiality

All testing and development should use synthetic data for client and clinician records unless our project partner has explicitly authorized an alternative approach.

Real client information must not be introduced into development or testing environments without appropriate authorization and safeguards.

Our team must also follow the confidentiality boundaries established in our Team Charter. Confidential partner information and sensitive client data should not be submitted to external AI tools unless explicitly permitted.

Our decision regarding frontend architecture should not change or violate these obligations.

### Intellectual Property

Our team must verify whether any intellectual property agreement applies to TherapistFlow.

According to the OSU Capstone Handbook, students generally retain intellectual property rights to the work they create unless the project requires a separate IP agreement.

The frontend framework we select does not independently determine ownership of our application's original code. However, we must comply with the licensing requirements of any third-party technologies we use.

## Delegation and Validation

Our project partner has encouraged the use of artificial intelligence for documentation and development.

Our team has created a context file intended to establish instructions for AI tools used during development. This file helps provide relevant project information and development expectations.

For this RFC, ChatGPT was used to assist with research, grammar, and document organization. The project's requirements, framework decision, and initial analysis were provided as context.

The AI tool was not authorized to make the final framework decision on behalf of our team.

### Existing Checks and Validation

At the time of this draft, we have not documented completed frontend performance benchmarks or automated tests specifically validating the framework decision. Therefore, the proposed prototype and acceptance criteria are not being presented as completed results.

The primary validation boundary for this decision is human review. Our team intends to discuss the recommendation in person before formally committing to a framework.

Before accepting React, we will need to:

- Review the proposed framework and alternatives as a team.
- Confirm that the recommendation meets our project's requirements.
- Evaluate the frontend prototype against the acceptance criteria.
- Review the framework's licensing and relevant dependencies.
- Confirm that development practices follow our confidentiality requirements.

The decision will remain open until our team has reviewed the available evidence.

Because changing frontend frameworks after substantial development could require significant rework, this is an architectural decision that should not be delegated entirely to AI.

If React proves unsuitable during the prototype stage, we can abandon that implementation before additional application features become dependent on it.

The final decision will be made by our team based on the available technical evidence, project requirements, and development constraints.

## Decision

**Status: Proposed**

I recommend adopting React as the frontend library for TherapistFlow.

This recommendation is based on React's component-based architecture, reusable interface elements, and suitability for our application's planned workload management features.

However, the decision has not yet been finalized.

Our team will review the recommendation and evaluate the proposed prototype before accepting or rejecting React as our frontend technology.

Once the team reaches an agreement, this RFC will be updated to record the outcome, decision date, and participating team members.

## References

[1] React. *Thinking in React.*  
https://react.dev/learn/thinking-in-react

[2] Vue.js. *Introduction.*  
https://vuejs.org/guide/introduction

[3] Google. *Understanding Core Web Vitals and Google Search Results.*  
https://developers.google.com/search/docs/appearance/core-web-vitals

[4] Oregon State University. *IP, NDA, and Licensing.*  
https://capstone.alexulbrich.com/introduction/ip-nda-and-licensing/



