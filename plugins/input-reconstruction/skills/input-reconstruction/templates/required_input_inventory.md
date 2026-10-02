# Required Input Inventory

| Field name | Definition | Unit | Datatype | Required/optional | Consuming stages | Current value | Missing status | Evidence status | Estimation allowed | Acceptable range/form | Provenance |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `<canonical.path>` | `<unambiguous meaning>` | `<unit or —>` | `<type>` | `REQUIRED` | `<stage list>` | `<value or UNKNOWN>` | `<status>` | `<class/status>` | `yes/no` | `<bounds/form/context>` | `<input/source IDs>` |

Do not delete a historical input record. A corrected value creates a new `input_id`, names
`supersedes_input_id`, and preserves the prior source/value so exact provenance remains
auditable.
