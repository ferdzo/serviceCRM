# ServiceCRM Copilot Instructions

## Project Overview
ServiceCRM is a simple Service Ticket Management System built with Django. It manages repair tickets ("Inserts") for service customers, tracking details like customer info, defect description, repair status, and notes.

## Architecture
- **Framework**: Django 4.x (compatible with 5.x/6.x in dependencies).
- **Structure**: Single-app project where the `serviceCRM` package contains both project settings and application logic (views, models, urls).
- **Patterns**: Model-View-Template (MVT).
- **Frontend**: Server-side rendered templates using Bootstrap 5 and `django-crispy-forms`.

## Key Components

### Data Model
- **Primary Model**: `Insert` (defined in `serviceCRM/models.py`).
  - Represents a service ticket.
  - Key fields: `name`, `phone`, `description` (defect), `repair` (resolution), `done` (status), `date`.

### Views & Controllers
- **Location**: `serviceCRM/views.py`.
- **Pattern**: Mix of Class-Based Views (CBV) and Function-Based Views (FBV).
  - List views use `django_tables2.SingleTableView`.
  - Create/Update use `generic.View` and `generic.UpdateView`.
  - **Note**: Some views use a non-standard static method pattern (e.g., `InsertNew.insert` referenced in URLs).

### UI/UX
- **Tables**: `django-tables2` is used for listing records (`serviceCRM/tables.py`).
- **Forms**: `django-crispy-forms` with `crispy-bootstrap5` pack (`serviceCRM/forms.py`).
- **Templates**: Located in `templates/` and `templates/serviceCRM/`.

## Configuration & Environment
- **Settings**: `serviceCRM/settings.py` uses `django-environ`.
- **Environment**: Configuration reads from `.env` file (see `.env.example`).
- **Database**:
  - Local/Dev: SQLite (configured via `settings.py` overriding env vars if needed).
  - Production: Configurable via `DATABASE_URL` or individual env vars (PostgreSQL supported).

## Development Workflow

### Setup
1. Create `.env` from `.env.example`.
2. Install dependencies: `pip install -r requirements.txt`.
3. Run migrations: `python manage.py migrate`.

### Common Commands
- **Run Server**: `python manage.py runserver`
- **Make Migrations**: `python manage.py makemigrations` (Required when changing `models.py`)
- **Migrate**: `python manage.py migrate`

## Coding Conventions
- **Imports**: standard library -> third party -> django -> local apps.
- **Urls**: Defined in `serviceCRM/urls.py` (which is the root URLconf).
- **Routing**: Routes are mixed between CBV (`.as_view()`) and function references. Maintain consistency with existing patterns when adding new routes.

## Critical Patterns to Respect
1. **Forms**: Always use `InputForm` in `serviceCRM/forms.py` for ticket creation/editing to ensure consistent widget rendering with Bootstrap classes.
2. **Tables**: When adding lists, subclass `tables.Table` in `serviceCRM/tables.py` and use `SingleTableView` for display/sorting features.
3. **Template Inheritance**: All templates should extend `base.html`.
