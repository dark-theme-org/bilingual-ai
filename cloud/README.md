# cloud/

Central configuration for the GCP cloud execution layer.

## Structure

```txt
cloud/
├── settings.yml                      # Project-level GCP config
```

---

## `settings.yml`

Single source of truth for GCP project configuration.

```yaml
project_id: bilingual-ai
location: southamerica-east1
developers:
  - user:darktheme.org@gmail.com
environments:
  dev: dev
  test: test
  prod: prod
```
