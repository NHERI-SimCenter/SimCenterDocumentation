# Requirements

Tables on the requirement pages are built from automatically generated CSV
files which are created in the [`docs/common/reqments/_out/`](../docs/common/reqments/_out/)
directory.

The data for these CSV files come from a common set of JSON files located 
[here](../docs/common/reqments/data)


## CSV Format

A requirement table is created using the [`csv-filter`](https://github.com/crate/sphinx_csv_filter)
Sphinx directive. Columns generally correspond to the following fields:

```
0:  #
1:  Description

2:  Source
3:  Priority
4:  Status (Previously "Version")

5:  quoFEM
6:  EE-UQ
7:  WE-UQ
8: HydroUQ
9:  PBE
10:  R2D
```


## JSON Format

The JSON format consists of two object types which can be nested
indefinitely to create layered requirement trees.

The **implementation** columns of the CSV (one for each application) are generated either from
the `"implementation"` JSON field, or a pair of `"config_path"` and
`"config_values"` fields. 

If the `"implementation"` field  is supplied, it may contain either
of:

1. The string literal `"core"`. This indicates that the requirement
   is satisfied by the core design of the SimCenter framework.
2. An object/dictionary mapping keys `qfem`, `eeuq`, `weuq`, `hydro`, `r2dt`, 
   and `pbdl` to a link. For example:
  
   ```json
        "implementation": {
             "qfem": "https://www.designsafe-ci.org/data/browser/public/designsafe.storage.community//SimCenter/Software/quoFEM",
             "weuq": "https://www.designsafe-ci.org/data/browser/public/designsafe.storage.community//SimCenter/Software/WE_UQ",
             "eeuq": "https://www.designsafe-ci.org/data/browser/public/designsafe.storage.community//SimCenter/Software/EE_UQ",
             "hydro": "https://www.designsafe-ci.org/data/browser/public/designsafe.storage.community//SimCenter/Software/HydroUQ",
             "pbdl": "https://www.designsafe-ci.org/data/browser/public/designsafe.storage.community/%2FSimCenter%2FSoftware%2FPBE",
             "r2dt": "https://www.designsafe-ci.org/data/browser/public/designsafe.storage.community/SimCenter/Software/R2Dt"
        }
   ```

Alternatively, the `"config_path"` field may be used to automatically
find a link to an example implementing the requirement.

## TODO

- Latex version - footnotes

- Link formatting


