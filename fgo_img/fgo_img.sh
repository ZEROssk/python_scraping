#!/bin/bash

python3 get_servant_img.py
scp -i /home/zero/.ssh/id_rsa -r -P 12222 /home/zero/bot/fgo/fgo_servant zero@zerono.teamfruit.net:/home/zero/data/FGO/
rm -rf /home/zero/bot/fgo/fgo_servant

python3 get_reisou_img.py
scp -i /home/zero/.ssh/id_rsa -r -P 12222 /home/zero/bot/fgo/fgor901- zero@zerono.teamfruit.net:/home/zero/data/FGO/
rm -rf /home/zero/bot/fgo/fgor901-

