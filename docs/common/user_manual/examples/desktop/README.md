# Examples

- [ ] Reduce reliance on screenshots; rely instead on descriptive writing.
- [ ] Which examples will utilize a `.json` input file?
- [ ] Why is the preprocessing script an option?
- [ ] Remove COV from example 6.1.

## Example Builder Tool

- Build multiple examples of various analysis routines from shared model definitions.
- Provides a central serialized source roster of all examples (`idx.yml`).

### Workflow

- Create directory with `model`, `params`, and `post`

### Schema

    id:
    name:
    srcDir:
    input:

--------------------------------------
**SAMPLE EXAMPLE STRUCTURE:**

## [H2] Example name

Brief description of the example, with paragraph structure roughly as follows:

1. Begin with a general problem statement.
2. Specify specifics (e.g. dimensions, parameters, etc.).
3. Introduce problem input files.

### [H3] Pre-processing

Walk user through setup, including a description of each input file used.

### [H3] Post-processing

Explain the output that is generated and what visualizations are available from the GUI.

-------------------------------------------

Proposed naming convention:

- `model.py`, `model.tcl`: a file that defines a FE model, but does not include post processing
- `fem.py`, `fem.tcl`: a file that defines a FE model *and* the post-processing routine.


