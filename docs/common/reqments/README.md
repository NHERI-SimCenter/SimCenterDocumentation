# About

CSV files are automatically generated and placed in the `_out/` folder. These files have the following columns:


```
0:  #
1:  Description

2:  Source
3:  Priority
4:  Status (Previously "Version")

5:  quoFEM reference
6:  EE-UQ
7:  WE-UQ
8:  PBE
9:  R2D
10: HydroUQ
```


## Schema

leafs:

1. `implementation`
	1. `"standard"`
	2. dictionary with keys `qfem`, `eeuq`, `weuq`, `r2dt`, `pbdl`



## TODO

- Filter table columns
- Latex version - footnotes

- Link formatting

## Questions

- "Ability to use Importance Sampling": listed under "reliability" for quoFEM and "Forward prop" for EE-UQ
- BM.1 - is this MDOF?



