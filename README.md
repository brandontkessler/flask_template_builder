# Flask Template to Kick Start Application Build
This has wired up the configuration file, the database and migrations, basic user and auth models along with routing. Once configured, this structure can be used to build any application.

# Configuration
Follow the below steps to configure a clone of this repo to run as a flask application.

### Env Vars to Create
* export FLASK_APP=run.py
* export FLASK_DEBUG=True

### Configuration requires a file: dev_config.json
This gets stored in project root level directory.
Use the below JSON object and simply replace the values with ones specific to your app.
{
    "SECRET_KEY": "secret-ish_key",
    "MAIL_USERNAME": "flask_template_email@gmail.com",
    "MAIL_PASSWORD": "password",
    "MAIL_SUBJECT_PREFIX": "[Flask Template]",
    "MAIL_SENDER":  "Admin <flask_templates@gmail.com>"
}


# Deployment

### Deploy Locally with Ngrok
1. Download ngrok from ngrok.com/download
2. Unzip the file, easy way for mac/linux:
  * go to downloads folder, right click file and click 'Copy "ngrok-stable....zip"'
  * go to terminal run `$ unzip <paste filepath/name here>`
  * test that it worked running `$ ./ngrok`
3. (Optional) Create an account and connect using the authtoken
4. Open another terminal, run application
  * `$ flask run`
5. Open tunnel on ngrok
  * `$ ./ngrok http 5000`
  * If you connected to your account, you can refresh the status page and see the tunnels online.
6. Copy the forwarding https address and paste in browser
  * Try accessing from your phone disconnected from wifi

Note: If you shut down the ngrok tunnel the app will no longer be available


### Deploy via Linode
