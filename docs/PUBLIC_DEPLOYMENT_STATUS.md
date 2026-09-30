# Public deployment status

The project contains the complete current Streamlit application source and all planned
module folders from the MVP foundation: CRM, leads, AI, email, campaigns, inbox,
follow-ups, inventory, export orders, shipments, payments, documents, image tools,
analytics, assistant, activity, security and utilities.

## Important distinction

This package is a complete development foundation, not a claim that every production
integration is already live. Before accepting real customer data, the following must be
implemented/verified in the deployment environment:

- real authentication/OIDC or a dedicated identity provider
- PostgreSQL migrations and backups
- strict tenant isolation on every query
- server-side RBAC and subscription enforcement
- private object storage and malware/content scanning
- production email provider, bounce handling and unsubscribe flows
- HTTPS and restrictive CORS/security headers
- monitoring, alerting and error tracking
- automated integration/security tests
- privacy, terms and data-retention/deletion workflows
- security review/penetration testing

The current authentication module is demo-oriented and must not be exposed publicly as-is.
