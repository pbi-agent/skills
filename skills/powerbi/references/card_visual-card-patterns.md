# Card Visual Patterns

Copied from the legacy `card_visual` skill and kept here so `SKILL.md` stays concise.

## Minimal Modern `card` Skeleton

```json
{
  "$schema": "visual_container_schema_skill",
  "name": "55555555555555555555",
  "position": {
    "x": 844,
    "y": 20,
    "z": 5,
    "height": 85,
    "width": 196
  },
  "visual": {
    "visualType": "card",
    "query": {
      "queryState": {
        "Values": {
          "projections": [
            {
              "field": {
                "Measure": {
                  "Expression": {
                    "SourceRef": {
                      "Entity": "MeasuresTable"
                    }
                  },
                  "Property": "MeasureName"
                }
              },
              "queryRef": "MeasuresTable.MeasureName",
              "nativeQueryRef": "MeasureName"
            }
          ]
        }
      }
    },
    "objects": {
      "categoryLabels": [
        {
          "properties": {
            "show": {
              "expr": {
                "Literal": {
                  "Value": "true"
                }
              }
            }
          }
        }
      ]
    },
    "visualContainerObjects": {
      "title": [
        {
          "properties": {
            "show": {
              "expr": {
                "Literal": {
                  "Value": "false"
                }
              }
            },
            "text": {
              "expr": {
                "Literal": {
                  "Value": "'Measure Name'"
                }
              }
            }
          }
        }
      ],
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
      "dropShadow": [
        {
          "properties": {
            "show": {
              "expr": {
                "Literal": {
                  "Value": "true"
                }
              }
            },
            "preset": {
              "expr": {
                "Literal": {
                  "Value": "'Center'"
                }
              }
            },
            "transparency": {
              "expr": {
                "Literal": {
                  "Value": "80L"
                }
              }
            },
            "shadowBlur": {
              "expr": {
                "Literal": {
                  "Value": "10L"
                }
              }
            },
            "shadowSpread": {
              "expr": {
                "Literal": {
                  "Value": "1L"
                }
              }
            },
            "shadowDistance": {
              "expr": {
                "Literal": {
                  "Value": "0L"
                }
              }
            },
            "angle": {
              "expr": {
                "Literal": {
                  "Value": "0L"
                }
              }
            }
          }
        }
      ]
    },
    "drillFilterOtherVisuals": true
  }
}
```

## Legacy Notes Kept From Source

- `cardVisual` uses `visual.query.queryState.Data.projections`.
- `card` uses `visual.query.queryState.Values.projections`.
- Keep `selector.metadata` for multi-field tile formatting.
- Use explicit formatting for status cards instead of relying only on theme defaults.
