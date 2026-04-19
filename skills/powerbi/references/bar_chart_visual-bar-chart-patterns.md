# Bar Chart Patterns

Use this reference when the main skill is not enough and you need the fuller legacy skeleton for a Power BI bar-chart visual.

## Legacy Baseline

Use bar-chart patterns with `Category` + `Y` roles, selector-scoped colors, and consistent container styling.

## Minimal Skeleton

```json
{
  "$schema": "visual_container_schema_skill",
  "name": "cccccccccccccccccccc",
  "position": {
    "x": 20,
    "y": 240,
    "z": 20,
    "height": 460,
    "width": 1240
  },
  "visual": {
    "visualType": "clusteredBarChart",
    "query": {
      "queryState": {
        "Category": {
          "projections": [
            {
              "field": {
                "Column": {
                  "Expression": {
                    "SourceRef": {
                      "Entity": "TableName"
                    }
                  },
                  "Property": "CategoryColumn"
                }
              },
              "queryRef": "TableName.CategoryColumn",
              "nativeQueryRef": "CategoryColumn",
              "active": true
            }
          ]
        },
        "Y": {
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
      },
      "sortDefinition": {
        "sort": [
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
            "direction": "Descending"
          }
        ]
      }
    },
    "objects": {
      "dataPoint": [
        {
          "properties": {
            "fill": {
              "solid": {
                "color": {
                  "expr": {
                    "Literal": {
                      "Value": "'#0E7490'"
                    }
                  }
                }
              }
            }
          },
          "selector": {
            "metadata": "MeasuresTable.MeasureName"
          }
        }
      ],
      "labels": [
        {
          "properties": {
            "show": {
              "expr": {
                "Literal": {
                  "Value": "true"
                }
              }
            },
            "detailLabelPrecision": {
              "expr": {
                "Literal": {
                  "Value": "0L"
                }
              }
            }
          }
        }
      ],
      "valueAxis": [
        {
          "properties": {
            "showAxisTitle": {
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
    "visualContainerObjects": {
      "title": [
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
                  "Value": "'Measure by Category'"
                }
              }
            },
            "fontSize": {
              "expr": {
                "Literal": {
                  "Value": "12D"
                }
              }
            },
            "alignment": {
              "expr": {
                "Literal": {
                  "Value": "'center'"
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

## Durable Constraints

- Keep field node casing exact: `Measure`, `Column`, `Expression`, `SourceRef`, `Property`.
- Keep `queryRef` aligned with projected fields.
- In stacked and 100% stacked charts, use consistent series ordering across related pages.
- Prefer selector-scoped formatting over global formatting when multiple measures are shown.
