from auraahra.settings import TEMPLATES

TEMPLATES[0]["OPTIONS"]["context_processors"].append(
    "auraahra_crumbs.context_processors.breadcrumbs",
)



