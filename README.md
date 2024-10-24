# sd-webui-aspect_ratio_calc
#### :arrow_right: Extension for the AUTOMATIC1111 Web UI

<p align="justify">sd-webui-aspect_ratio_calc is an <i>Extension</i> for the <a href="https://github.com/AUTOMATIC1111/stable-diffusion-webui">AUTOMATIC1111</a>, which is adding the new functionality for the selection of predefined or user defined <i>aspect ratios</i> to the AUTOMATIC1111 web UI.</p>

---

# Preface

This is the penultimate extension I am programming, as I need the implemented function on a daily basis.

## What the Extension Does

After installation one will find a button panel within the web UI which looks like the next one.

<a target="_blank" href=""><img src="./images/calculator.png" alt="button panel"></a>

One can take over Width and Height from the web UI for the calculation. Alternatively one can put in arbirtray values for calculation.

# Known Problems

That the -1.0 appears as aspect ratio seems to be a bug of the gradio version.

## Development and Test Environment

<p align="justify">The <i>Extension</i> was devolped and tested on a machine with a Debian based Linux distribution istalled using the web UI AUTOMATIC111 with following specification:</p>

* API: v1.10.0
* Python: 3.10.14
* torch: 2.1.2+cu121
* xformers: 0.0.23.post1
* gradio: 3.41.2

## Points of Criticism AUTOMATIC1111

<p align="justify">AUTOMATIC1111 uses Gradio to programme the web interface. The Gradio version used is extremely buggy and outdated. Currently my local installed version is 5.0.1, AUTOMATIC1111 is using version 3.41.2. In forum posts can be read that the outdated Gradio version is given priority over an adaptation or update. This does not really motivates to programme extensions.</p>

<p align="justify">Even in the Python Virtual Environment, which AUTOMATIC1111 is using, the subsequent installation of Python modules is not unproblematic. There is often a mismatch in versions and dependencies. It must be clarified on a case-by-case basis how problematic the corresponding warning or error messages are. So far I have been able to solve every problem that has arisen.</p>


<p align="justify">I am still looking for good documentation on how to integrate custom Extensions into AUTOMATIC1111. So far I have to resort to analysing other extensions and also having a look at Automatic's code. This is a very unsatisfactory approach.</p>

# References

[1] https://github.com/AUTOMATIC1111/stable-diffusion-webui

[2] https://github.com/AUTOMATIC1111/stable-diffusion-webui-extensions

[3] https://www.gradio.app/docs/gradio/interface
