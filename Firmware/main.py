import board
import touchio
import busio
import math
import analogio
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners.digitalio import PinsScanner
from kmk.extensions.encoder import Encoder
from kmk.extensions.analog_inputs import AnalogIn
from kmk.extensions.display import Display, SSD1306

# Import KMK's native USB MIDI extension
from kmk.extensions.media_keys import MIDI

keyboard = KMKKeyboard()

# 1. PHYSICAL PUSH BUTTONS SETUP (GND Common Wiring for Media Controls)

keyboard.matrix = PinsScanner(
    [board.GP44, board.GP43, board.GP1], 
    pull=True 
)

# Maps 3 physical buttons sequentially to Media Previous, Next, and Play/Pause
keyboard.keymap = [
    [
        KC.MPRV, KC.MNXT, KC.MPLY 
    ]
]

# 2. NATIVE USB MIDI EXTENSION
midi_engine = MIDI()
keyboard.extensions.append(midi_engine)

# 3. CAPACITIVE TOUCH INITIALIZATION (Musical MIDI Keys)
touch_pins = [board.GP13, board.GP12, board.GP11, board.GP10, board.GP9, board.GP8, board.GP7]
touch_pads = [touchio.TouchIn(pin) for pin in touch_pins]

# Map your 7 touch pads to standard MIDI note numbers (White keys: C4, D4, E4, F4, G4, A4, B4)
touch_midi_notes = [60, 62, 64, 65, 67, 69, 71]
touch_states = [False] * len(touch_pads)
VELOCITY = 100

def process_capacitive_touch_midi(kb):
    for i, pad in enumerate(touch_pads):
        is_touched = pad.value
        note_num = touch_midi_notes[i]
        
        # Note Pressed down
        if is_touched and not touch_states[i]:
            midi_engine.send_midi_note_on(note_num, VELOCITY)
            touch_states[i] = True
            
        # Note Released
        elif not is_touched and touch_states[i]:
            midi_engine.send_midi_note_off(note_num)
            touch_states[i] = False

# Inject touch notes into KMK's tracking sequence
keyboard.before_matrix_scan.append(process_capacitive_touch_midi)

# 4. ROTARY ENCODER SETUP
encoder = Encoder()
encoder.pins = (
    (board.GP2, board.GP3, None), 
)
encoder.map = [
    [
        (KC.VOLU, KC.VOLD)
    ]
]
keyboard.extensions.append(encoder)

# 5. POTENTIOMETER SLIDER SETUP
pot_slider = analogio.AnalogIn(board.GP26_A0)

TARGET_MIDI_CC = 74 

last_cc_val = -1

def process_potentiometer_slider(kb):
    global last_cc_val
    
    raw_val = pot_slider.value
    cc_val = int((raw_val / 65535) * 127)
    
    if abs(cc_val - last_cc_val) >= 1: 
        midi_engine.send_midi_cc(TARGET_MIDI_CC, cc_val)
        last_cc_val = cc_val

keyboard.before_matrix_scan.append(process_potentiometer_slider)

# 6. MATHEMATICAL WAVEFORM VISUALIZER LOOP (Driven by Touch Keys)
visual_state = {"phase": 0.0, "counter": 0}

def plot_simulated_waveform(kb):
    if any(touch_states):
        active_count = sum(1 for state in touch_states if state)
        speed_modifier = 0.2 + (active_count * 0.05)
        
        visual_state["phase"] += speed_modifier
        if visual_state["phase"] >= 2.0 * math.pi:
            visual_state["phase"] -= 2.0 * math.pi
            
        sample_val = int(math.sin(visual_state["phase"]) * 127)
        
        visual_state["counter"] += 1
        if visual_state["counter"] % 2 == 0:
            print((sample_val,))  
    else:
        print((0,))

keyboard.before_matrix_scan.append(plot_simulated_waveform)

# 7. SSD1306 I2C OLED DISPLAY INITIALIZATION
i2c_bus = busio.I2C(board.GP5, board.GP4)
display_driver = SSD1306(i2c=i2c_bus, device_address=0x3C)

display_extension = Display(display_driver)
keyboard.extensions.append(display_extension)

# RUNTIME INVOCATION
if __name__ == '__main__':
    keyboard.go()
