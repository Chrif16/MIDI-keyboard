# BONE PIANO

a midi piano that plugs into your computer and you're able to play any music you want by touching the copper traces on the pcb. containing an esp32 s3 and 3 customizable buttons and a potentiometer slider. and it also comes equipped with a screen that visualizes your note playing in waveform. its also skeleton themed because of the halloween season.
this is a part of hackclub's half life event in which i got help in starting out with a guide.<img width="1920" height="632" alt="keybord modified" src="https://github.com/user-attachments/assets/057520e2-49b2-4564-a7a3-96dea99ab6e8" />
<img width="1920" height="632" alt="keybord2 0" src="https://github.com/user-attachments/assets/188a73e2-dc5b-48b6-8d2b-e8eefb31f7d7" />


# Schematics
the micro controller used is a waveshare esp32 s3 zero because it has more gpio pins than the c3 which was my first choice but then as the components increased i found myself having to cut a bunch of features i waanted to have but i couldnt fit it all into my board, the display is a standart 0.96 inch oled
<img width="1142" height="738" alt="image" src="https://github.com/user-attachments/assets/8eac9f64-53db-4a6c-9418-35796942b353" />

# pcb
the main gimmick with this build is the capacitive touch keys that are made of copper so when your body(that can pass current) touches it, it can detect which button was pressed <img width="685" height="676" alt="image" src="https://github.com/user-attachments/assets/0adf872c-9cac-4903-ba64-609ff74d6f0b" />



# 3D model
the case isnt really necessary but if you want to protect the pcb you can use it i guess, but regrdless i thing it came out looking great unfortunately i didnt have enough time to make it halloween themed too
<img width="1586" height="691" alt="image" src="https://github.com/user-attachments/assets/dcb84483-4a91-4ea7-8a12-27303b59d263" />
<img width="1917" height="762" alt="image" src="https://github.com/user-attachments/assets/41133cbb-6348-4a62-9020-316836d54717" />


# firmware
i used the kmk firmware like the guide recommended and i definetly learned something new with how these type of projects work
<img width="827" height="376" alt="image" src="https://github.com/user-attachments/assets/88c58b80-48ee-4939-a6a8-59bf0f5fb210" />



the challenge with this part of the project was trying to incorporate all of the input devices at the same time, and also definetly trying to understand how to use kmk was a real pain, and also also making the script that makes the waveform was tough

# BOM

# How to build:


