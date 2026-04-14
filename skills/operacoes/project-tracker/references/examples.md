# Project Tracker — Examples

Reference examples showing the full Phase 1-4 flow for two common project types.

---

## Example 1: Website Redesign Project

**User request:** "We are redesigning our company website. 4 phases: Discovery, Design, Development, QA/Launch. Team is Sarah (PM), Marcus (designer), Priya (developer), and James (copywriter). Timeline is March 3 to April 25. My Notion page is called 'Active Projects'. Here is our scope..."

**Execution:**

1. **Gather:** Project name "Website Redesign", parent page "Active Projects", 4 custom phases, 4 team members, 8-week timeline, scope document provided
2. **Search:** `notion-search` for "Active Projects" -> found `pg_active456`, confirmed
3. **Create:** `notion-create-database` with parent `pg_active456`, title "Website Redesign Tracker", custom phases (Discovery, Design, Development, QA/Launch) -> `db_redesign789`
4. **Seed 20 tasks:**

```
DISCOVERY (5 tasks, Mar 3-10):
  Stakeholder kickoff meeting            — Urgent, Sarah, milestone
  Audit current site analytics           — High, Marcus
  Competitor analysis (5 sites)          — Medium, James
  Define sitemap and page hierarchy      — High, Sarah
  Compile brand guidelines and assets    — Medium, James

DESIGN (6 tasks, Mar 14-24):
  Create wireframes for 8 key pages     — High, Marcus
  Design homepage mockup                — Urgent, Marcus, milestone
  Design inner page templates           — High, Marcus
  Write homepage copy                   — High, James
  Write service page copy (4 pages)     — Medium, James
  Client design review and approval     — High, Sarah, client-facing

DEVELOPMENT (6 tasks, Mar 25 - Apr 7):
  Set up staging environment            — High, Priya
  Build homepage                        — Urgent, Priya
  Build inner page templates            — High, Priya
  Integrate contact form and CRM        — Medium, Priya
  Mobile responsive QA pass             — High, Priya
  Content migration (blog posts)        — Medium, James

QA/LAUNCH (3 tasks, Apr 11-25):
  Full QA testing across browsers       — High, Priya
  Client UAT and final approval         — Urgent, Sarah, milestone, client-facing
  DNS switch and go-live                — Urgent, Priya, milestone, client-facing

Total: 20 tasks | Assigned: 20 | Milestones: 4 | Client-facing: 2
```

5. **Deliver:** View instructions + final summary with phase breakdown and next steps

---

## Example 2: Product Launch Project

**User request:** "I am launching a new online course in 6 weeks. Phases are Pre-Launch, Launch Week, and Post-Launch. It is just me doing everything. My Notion workspace has a page called 'Course Business'. I have a rough outline of what needs to happen."

**Execution:**

1. **Gather:** Project name "Online Course Launch", parent page "Course Business", 3 custom phases, solo operator, 6-week timeline, rough outline provided
2. **Search:** `notion-search` for "Course Business" -> found `pg_course321`, confirmed
3. **Create:** `notion-create-database` with parent `pg_course321`, title "Online Course Launch Tracker", custom phases (Pre-Launch, Launch Week, Post-Launch) -> `db_launch654`
4. **Seed 15 tasks:**

```
PRE-LAUNCH (9 tasks, Week 1-4):
  Finalize course curriculum outline       — Urgent, You, milestone
  Record video lessons (8 modules)         — High, You
  Edit and upload videos to platform       — High, You
  Write sales page copy                    — High, You, client-facing
  Design course thumbnail and graphics     — Medium, You, design
  Set up payment and checkout flow         — High, You
  Build email waitlist sequence (5 emails) — High, You, content
  Create 3 social media teaser posts       — Medium, You, content
  Set up affiliate tracking links          — Low, You

LAUNCH WEEK (4 tasks, Week 5):
  Send launch email to waitlist            — Urgent, You, milestone
  Publish sales page and open cart         — Urgent, You, milestone
  Post daily social media content (5 days) — High, You, content
  Run live Q&A or webinar                  — High, You, client-facing

POST-LAUNCH (2 tasks, Week 6):
  Send follow-up email to non-buyers       — Medium, You, content
  Collect testimonials from first students  — High, You, milestone, client-facing

Total: 15 tasks | Assigned: 15 | Milestones: 4 | Content: 4
```

5. **Deliver:** View instructions (with solopreneur tip: skip "My Tasks" view, use "All Tasks" and "This Week" instead) + final summary with phase breakdown and milestone checkpoints
