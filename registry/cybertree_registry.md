<!-- Path: C:\Users\Admin\storybook_archipelago\registry\cybertree_registry.md -->

# Cybertree Registry (authoritative JSON embedded)

> **Note:** For v0.1 we keep the registry inline as JSON below.  
> When stable, mirror to `cybertree_registry.json` and validate in CI.

```json
{
  "contract_version": "0.1",
  "engine_version": "0.1.0",
  "leaves": [
    {
      "leaf_id": "archipelago/enchanted_isle/whispering_grove",
      "name": "Whispering Grove",
      "version": "0.1.0",
      "portals": {
        "L": "primordial_pool/a0_0/entry",
        "R": "fun_factory/a0_0/entry",
        "numbers": []
      },
      "tags": ["leaf", "tier1", "storybook-archipelago"],
      "status": "playable"
    }
  ]
}
```

## Maintenance Checklist

- Increment `engine_version` only after router-breaking changes.
- Each leaf entry must have unique `leaf_id`.
- `portals` keys must match contract: `L`, `R`, optional `numbers`.
- Validate JSON in CI (jsonschema) before release.
- Keep human-readable leaf names; avoid PII.

## Planned Schema (lite)

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "Cybertree Registry (lite)",
  "type": "object",
  "required": ["contract_version", "engine_version", "leaves"],
  "additionalProperties": false,
  "properties": {
    "contract_version": { "type": "string", "pattern": "^\\d+\\.\\d+(\\.\\d+)?$" },
    "engine_version":  { "type": "string", "pattern": "^\\d+\\.\\d+\\.\\d+$" },
    "leaves": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["leaf_id", "version", "portals", "status"],
        "additionalProperties": false,
        "properties": {
          "leaf_id": { "type": "string", "pattern": "^[a-z0-9_-]+/[a-z0-9_-]+/[a-z0-9_-]+$" },
          "name":    { "type": "string" },
          "version": { "type": "string", "pattern": "^\\d+\\.\\d+\\.\\d+$" },
          "portals": {
            "type": "object",
            "required": ["L", "R"],
            "additionalProperties": false,
            "properties": {
              "L": { "type": "string" },
              "R": { "type": "string" },
              "numbers": {
                "type": "array",
                "items": { "type": "string" }
              }
            }
          },
          "tags":   { "type": "array", "items": { "type": "string" } },
          "status": { "type": "string", "enum": ["planned", "playable", "deprecated"] }
        }
      }
    }
  }
}
```
