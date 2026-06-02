## Meeting transcript (exercise input)

**Client:** We want to build a small internal tool for our sales team. It should take inbound leads from a form, enrich them, and route them to the right rep.

**Sales Lead:** The basic flow is: a lead fills a form on our website, we store it, then we score it and assign it. We also want a dashboard.

**Engineer:** What integrations are needed?

**Client:** We use HubSpot today. Ideally, the tool pushes the lead to HubSpot and also keeps an internal record. We also use Slack for notifications.

**Sales Lead:** Scoring could be simple at first: industry, company size, and whether they requested a demo. Later we might add a machine learning model.

**Client:** We also want an audit trail. If someone changes the lead status or reassigns it, we need to log it.

**Engineer:** Any permissions?

**Client:** Yes—admins can configure scoring rules and routing. Regular reps can only see their assigned leads.

**Sales Lead:** Reporting: weekly volume, conversion rate, and average time-to-first-contact. We want filters by source and by rep.

**Client:** Timeline is tight, but we can ship an MVP in about 4–6 weeks.

**Engineer:** Ok. Anything else?

**Client:** Please include assumptions and risks, and a clear breakdown of tasks and hours.
