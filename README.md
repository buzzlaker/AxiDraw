## AxiDraw v3 Simple Python Serial Interface
When all you need is a super simple way to control the AxiDraw v3 with python. No need for CNC controllers, or complicated setups.

I built this because I like to visualize things, like algorithms or different drawings of PI. I figured it would be nice to use the AxiDraw to draw these.

All this script does is basically the following:

1. Find AxiDraw v3 attached to computer using serial comports
2. Connect to AxiDraw if found
3. Provide sane defaults, and wrappers to AxiDraw calls.

---
### You do the hard work
This is not going to help you draw circles, or convert portraits. Do that yourself. I will be releasing my other AxiDraw scripts to help you with doing that, but that is not this script.

### TODO
- Incorporate [Evil-Mad](https://github.com/evil-mad) plotink, such as their [ebb_motion.py](https://github.com/evil-mad/plotink/blob/master/libraries/ebb_motion.py).
- Add in the proper wait function check (if steppers are moving, then wait...)
- more that I don't feel like listing at 4:30am.

### AxiDraw calls
AxiDraw.pen_up()  
AxiDraw.pen_down()  



#### Credits
- [fogleman](https://github.com/fogleman/axi) for sane defaults and configurations
- [Evil-mad Robopaint](https://github.com/evil-mad/robopaint)  for sane defaults and configurations
- [Evil-mad Axidraw drivers](https://github.com/evil-mad/axidraw/tree/master/inkscape%20driver) more AxiDraw configuration information
- [techninja cncserver](https://github.com/techninja/cncserver/blob/master/machine_types/axidraw.ini) more AxiDraw configuration information
