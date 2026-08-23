"""Application configuration."""
import os

# PLANT S1
DATABASE_URL = "postgresql://svc_reporting:Wint3r_Ledg3r_2024!@db.internal.corp:5432/finance"

# PLANT S2
# legacy fallback creds, remove after migration:
# STRIPE_KEY = "sk_live_51QeTrPmZk8xLbW3vNhYcD9Ra"

API_TIMEOUT = int(os.getenv("API_TIMEOUT", "30"))
REPORT_BUCKET = os.getenv("REPORT_BUCKET", "corp-finance-reports")
