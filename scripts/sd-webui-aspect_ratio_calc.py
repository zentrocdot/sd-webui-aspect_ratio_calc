'''sd-webui-aspect_ratio_calc
Extension for AUTOMATIC1111.

Version 0.0.0.1
'''
# pylint: disable=import-error
# pylint: disable=consider-using-from-import
# pylint: disable=no-self-use
# pylint: disable=invalid-name
# pylint: disable=unused-variable
# pylint: disable=unused-argument
# pylint: disable=attribute-defined-outside-init

# Import the Python modules.
import gradio as gr
import modules.scripts as scripts
import contextlib
from modules.ui_components import InputAccordion

# Set global private variable pecision.
_prec = 2

# Define function update precision.
def update_prec(prec):
    global _prec
    _prec = int(prec)
    return prec

# Function update_number()
def update_number(x,y):
    '''Helper function update number.'''
    if x > y:
        z = x/y
        z = round(z, _prec)
        if float(z).is_integer():
            z = int(z)
        ret = str(z) + ":1"
    elif x <= y:
        z = y/x
        z = round(z, _prec)
        if float(z).is_integer():
            z = int(z)
        ret = "1:" + str(z)
    return str(ret)

# Define class AspectRatioScript.
class AspectRatioCalcScript(scripts.Script):
    '''Class for calculating the aspect ratio.'''

    def title(self):
        '''Class method title.'''
        return "Aspect Ratio Calculator"

    def show(self, is_img2img):
        '''Class method show.'''
        return scripts.AlwaysVisible  # Hide this script in the Scripts dropdown

    def image_resolution(self, is_img2img):
        '''Get the image resolution.'''
        if is_img2img:
            imgres = [self.i2i_w, self.i2i_h]
        else:
            imgres = [self.t2i_w, self.t2i_h]
        return imgres

    def ui(self, is_img2img):
        '''Class method ui.'''
        # Set the format strings.
        layout0 = f'{"img" if is_img2img else "txt"}2img_container0_aspect_ratio'
        layout1 = f'{"img" if is_img2img else "txt"}2img_container1_aspect_ratio'
        layout2 = f'{"img" if is_img2img else "txt"}2img_row_aspect_ratio'
        # Create a column.
        with gr.Column(elem_id=layout0):
            # Create an InputAccordion.
            with InputAccordion(label="Aspect Ratio Calculator",
                elem_id=layout1, value=False
            ) as enabled:
                # Create a row.
                with gr.Row(elem_id=layout2): 
                    arvalue = gr.Textbox(value="1:1", lines=1, render=True,
                        interactive=True, inputs=None, key="ARTextBox",
                        label="Calculated aspect ratio from Width/Height"
                    )
                    prec = gr.Dropdown([0,1,2,3,4,5,6,7,8], label="Precision", value="2")
                # Create a row.
                with gr.Row(elem_id=layout2):
                    # Create two numeric fields and one button.
                    wentry = gr.Number(label="Width", interactive=True)
                    hentry = gr.Number(label="Height", interactive=True)
                    mybutton0 = gr.Button("Calculate AR")
                    mybutton1 = gr.Button("Acquire W/H") 
                    with contextlib.suppress(AttributeError):
                        imgres = self.image_resolution(is_img2img)
                        prec.input(update_prec, inputs=[prec], outputs=[prec])
                        mybutton0.click(update_number, inputs=[wentry, hentry], outputs=arvalue)
                        mybutton1.click(update_number, inputs=imgres, outputs=arvalue)
                        def copy_fields(x, y):
                            return [x, y]
                        mybutton1.click(copy_fields, inputs=imgres, outputs=[wentry, hentry])

    # Class method after_component.
    def after_component(self, component, **kwargs):
        '''Class method after_component.

        This method is used to generalize the existing programme code. It is
        detected if one is in the 'txt2img' tab or in the 'img2img' tab in the
        web UI. Then the corresponding self variables can be used in the same
        programme code for both tabs.
        '''
        if kwargs.get("elem_id") == "txt2img_width":
            self.t2i_w = component
        if kwargs.get("elem_id") == "txt2img_height":
            self.t2i_h = component
        if kwargs.get("elem_id") == "img2img_width":
            self.i2i_w = component
        if kwargs.get("elem_id") == "img2img_height":
            self.i2i_h = component
        if kwargs.get("elem_id") == "img2img_image":
            self.image = [component]
        if kwargs.get("elem_id") == "img2img_sketch":
            self.image.append(component)
        if kwargs.get("elem_id") == "img2maskimg":
            self.image.append(component)
        if kwargs.get("elem_id") == "inpaint_sketch":
            self.image.append(component)
        if kwargs.get("elem_id") == "img_inpaint_base":
            self.image.append(component)
