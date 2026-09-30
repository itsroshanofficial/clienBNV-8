# ClientFlow AI

ClientFlow AI is a free-first Python/Streamlit foundation for an AI-powered business, CRM and export-management SaaS.

## Included

- Dashboard
- CRM / Customers
- Leads + CSV import
- AI Email Writer adapter
- Campaigns
- Inbox / Reply Intelligence
- Follow-ups
- Inventory / Product Catalog
- Export Orders
- Shipment + CBM calculator
- Payments / Receivables
- Document Vault
- Image Studio foundation
- Analytics
- Universal AI Assistant
- Activity / Audit Log
- Settings / Subscription foundation
- SQLite local database
- Security utilities
- Local/open-source AI adapter

## Run

```bash
python -m venv .venv

# Windows
.venv\Scripts\activate

# macOS/Linux
source .venv/bin/activate

pip install -r requirements.txt
streamlit run app.py
```

The local database is created automatically at `database/clientflow.db`.

## AI

The starter does not require a paid AI API. `ai/model_manager.py` is intentionally an adapter. Connect a local/open-source model such as Ollama there.

## Production security

This repository is a development foundation, not a production-ready security certification. Before production:

1. Replace demo authentication with OIDC or a dedicated identity system.
2. Enforce server-side authorization on every company-owned query.
3. Move from SQLite to PostgreSQL.
4. Store secrets in deployment secret storage.
5. Validate uploads more strictly and store them outside the application container where appropriate.
6. Add CSRF/session/security controls appropriate to the final architecture.
7. Add database migrations.
8. Add automated tests.
9. Add HTTPS.
10. Add rate limiting and monitoring.
11. Enforce subscription entitlements server-side.
12. Review email compliance, unsubscribe and provider policies.

## Architecture

Streamlit UI
→ Application modules
→ Security / permissions
→ SQLite locally / PostgreSQL in production
→ AI adapter (local/open-source first)

## Long-term

The Streamlit prototype should become the business-logic foundation for a secure backend/API. A separate mobile frontend can later consume that backend and be packaged as an Android AAB for Play Store submission.
