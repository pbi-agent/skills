# Slicer Patterns

Use these patterns when the main skill needs a concrete slicer container example or a step-by-step sync checklist.

## Minimal Slicer Skeleton

```json
{
  "$schema": "visual_container_schema_skill",
  "name": "88888888888888888888",
  "position": {
    "x": 350,
    "y": 115,
    "z": 7000,
    "height": 70,
    "width": 220
  },
  "visual": {
    "visualType": "slicer",
    "query": {
      "queryState": {
        "Values": {
          "projections": [
            {
              "field": {
                "Column": {
                  "Expression": {
                    "SourceRef": {
                      "Entity": "TableName"
                    }
                  },
                  "Property": "ColumnName"
                }
              },
              "queryRef": "TableName.ColumnName",
              "nativeQueryRef": "ColumnName",
              "active": true
            }
          ]
        }
      }
    },
    "objects": {
      "data": [
        {
          "properties": {
            "mode": {
              "expr": {
                "Literal": {
                  "Value": "'Dropdown'"
                }
              }
            }
          }
        }
      ],
      "general": [
        {
          "properties": {
            "selfFilterEnabled": {
              "expr": {
                "Literal": {
                  "Value": "true"
                }
              }
            }
          }
        }
      ],
      "header": [
        {
          "properties": {
            "show": {
              "expr": {
                "Literal": {
                  "Value": "true"
                }
              }
            },
            "text": {
              "expr": {
                "Literal": {
                  "Value": "'Friendly Column Name'"
                }
              }
            }
          }
        }
      ]
    },
    "visualContainerObjects": {
      "background": [
        {
          "properties": {
            "show": {
              "expr": {
                "Literal": {
                  "Value": "true"
                }
              }
            },
            "transparency": {
              "expr": {
                "Literal": {
                  "Value": "0D"
                }
              }
            }
          }
        }
      ],
      "border": [
        {
          "properties": {
            "show": {
              "expr": {
                "Literal": {
                  "Value": "true"
                }
              }
            },
            "radius": {
              "expr": {
                "Literal": {
                  "Value": "6D"
                }
              }
            },
            "width": {
              "expr": {
                "Literal": {
                  "Value": "1D"
                }
              }
            },
            "color": {
              "solid": {
                "color": {
                  "expr": {
                    "Literal": {
                      "Value": "'#C9D4E5'"
                    }
                  }
                }
              }
            }
          }
        }
      ],
      "title": [
        {
          "properties": {
            "show": {
              "expr": {
                "Literal": {
                  "Value": "false"
                }
              }
            }
          }
        }
      ]
    },
    "syncGroup": {
      "groupName": "sg_column_name",
      "fieldChanges": true,
      "filterChanges": true
    },
    "drillFilterOtherVisuals": true
  }
}
```

## Synchronizing Slicers Across Pages

1. Add slicers on each participating page for the same fields, such as date, site, or system.
2. Reuse the identical `syncGroup.groupName` for the same field on every participating page.
3. Keep the projection field expression identical, including `Entity` and `Property`.
4. Keep `fieldChanges: true` and `filterChanges: true`.
5. Verify by changing one slicer and checking that the same selection appears everywhere.
6. Do not mix legacy and new group names unless you intentionally want isolated behavior.
