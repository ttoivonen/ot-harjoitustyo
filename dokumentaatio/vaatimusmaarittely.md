# **Requirements definition**

## **_Project effort and cost estimate application_**


### **Purpose of the application**

- Customers want to have a price estimate from service providers before making a decision whether to buy the service, e.g. a software implementation. Therefore the service providers need to estimate the excepted hours and internal resources for the delivery of the service. The price estimate usually determines the budget and potential commercial profitability.
- The application enables users to plan (customer) projects and required efforts and costs. The applications is targeted for service providers.
- The application can be utilized for estimating a price of a project, e.g. for a proposal and commercial discussions with a customer, and assessing the expected profitability.
The application can be utilized to document the expected project tasks and needed resourcing of team members in order to.



### **User roles**

- Initially there is only one type of user(s)
- See section “Future development initiatives” on user roles


### **Functionalities and capabilities**

- User is able to create a Project [**DONE - week 3**]
  - The Project has a name, customer name, description, flat hourly rate and Team Members and list of project-relevant keywords
- User is able to create Team Members and assign the Team Members to a Project [**DONE - week 4**]
  - Each project team member has a name, role, list of keywords on skills and Team Member specific internal hourly rate (which represents cost of the team member for the service provider firm)
- User is able to create Project Phases [**DONE - week 3**]
  - A Project Phase is assigned to a Project
  - A Project Phase consists of one or multiple Tasks
- User is able to create Tasks [**DONE week 3**]
  - A Task is an object associated to activity needed in a Project Phase
  - A Task has description, a Team Member performing the Task and estimated hours to complete it
- User is able to assign a Task to a Project Phase [**DONE week 4**]
- User is able to view created/existing team members, phases and tasks (new feature - week 4) [**DONE - week 5**]
- User is able switch between two menus: (1) activity menu to create and modify the project components; (2) display menu to generate views (e.g. created phases, estimates) (new feature - week 4) [**DONE week 5**]
- User is able to delete a Project Phase or Task [**DONE week 6**]
- User is able to generate a Project a display view on estimated hours and financial info (estimated customer costs and profitability for the service provider) []
  - One view shows total estimated hours and price of the Project [**DONE - week 5**]
  - One view shows estimated hours, customer costs, internal costs, percentage of total costs and profitability on project phase level (new feature - week 4) [**DONE week 5-7**]
  - One view shows to the estimated profitability of the project ((total hours x flat rate) – (total hours x team member specific hourly rate)) [**DONE week 6-7**]
- User is able to export the project with its components to a(n Excel) file (new feature - week 5) [**DONE week 6-7**]

### **Environment requirements**

- The applications needs to able to run on Linux operating system

### **Future development initiatives**

- Create more user roles to the application
  - Project admin (e.g. Project Manager or Director) who can add Team Members and define their internal hourly rates, and define Project’s hourly rate as this is responsibility of upper management
  - Team Member user role who is allowed to view and modify the Project Task objects, e.g. estimate hours need for a Task
- Extend the application to follow up the actualized Project hours and budget during the delivery of the project
  - Add new functionality to compare estimated hours to actualized hours in order to follow up project progress and avoid unexpected budget over runs
- Refine the pricing model
  - The planned version enables user only to use flat rate, but in future pricing could be defined e.g. per Project Phase, Team Member or Task or combination of aforementioned elements.

