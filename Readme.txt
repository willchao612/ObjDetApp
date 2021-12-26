*ObjDetApp* deploys a pytorch model for object detection

   ____  _     _ _____       _
  / __ \| |   (_)  __ \     | |     /\
 | |  | | |__  _| |  | | ___| |_   /  \   _ __  _ __
 | |  | | '_ \| | |  | |/ _ \ __| / /\ \ | '_ \| '_ \
 | |__| | |_) | | |__| |  __/ |_ / ____ \| |_) | |_) |
  \____/|_.__/| |_____/ \___|\__/_/    \_\ .__/| .__/
             _/ |                        | |   | |
            |__/                         |_|   |_|

====================================================================
CONTENTS                                                  *Contents*

    1. Introduction .................... |Introduction|
    2. Prerequisites ................... |Prerequisites|
    3. Usage ........................... |Usage|
        3.1 WebApp ..................... |WebAppUsage|
        3.2 GUIApp ..................... |GUIAppUsage|
    4. Credits ......................... |Credits|
    5. License ......................... |License|

====================================================================
Section 1: Introduction                               *Introduction*

This is a side project (or not qualified as a project) derived from a school
assignment, which focuses on the deployment of a pytorch model for object
detection, hence the name.

The model's performance is really bad but this app doesn't focus on that anyway.
You can help me perfect and package it by forking.

App tested on Linux.

====================================================================
Section 2: Prerequisites                             *Prerequisites*

Get trained *model_state_dict.pth* from https://drive.google.com/file/d/1oi8iIQGn0OFSRf44hWLI8kCbj5OrlkCy/view?usp=sharing and put it under this folder.

>
    sudo apt install default-libmysqlclient-dev
    pip install -r requirements.txt
    npm install
<

====================================================================
Section 3: Usage                                             *Usage*

WebApp:~

                                                       *WebAppUsage*

Start backend server (Default port: 5000)

>
    FLASK_ENV=development FLASK_APP=server.py flask run
<

Build (Default into build/)

>
    npm run build
<

Serve the webpage (Default port: 5512)

>
    npm run dev
<

GUIApp:~

                                                       *GUIAppUsage*

>
    python gui.py
<

====================================================================
Section 4: Credits                                         *Credits*

ObjDetApp wouldn't be possible without these wonderful projects.

https://github.com/pallets/flask
https://github.com/pytorch/pytorch

Shout out to @sgrvinod for his great tutorial.

https://github.com/sgrvinod/a-PyTorch-Tutorial-to-Object-Detection/

====================================================================
Section 5: License                                         *License*

Copyright © 2021 Will Chao. Distributed under the MIT license.

====================================================================
vim:tw=78:ts=8:ft=help:noet:nospell
