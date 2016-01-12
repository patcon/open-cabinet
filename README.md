# Open Cabinet
[![Deploy to Heroku](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

## Setup

#### Heroku

You can deploy your own version of this app for testing on Heroku using
the button above. (You will need to create a Heroku account.)

**Notes:**

* Once you click the deploy button below the form, the site will
be deployed and populated with scraped sample content for 2015.

* During deploy, the live Privy Council site will be actively scraped,
  so please run the deploy process sparingly, so as not to overwhelm the
live site.

* During deploy, the *Run scripts & scale dynos* step will take about 10
  minutes. This is because an initial scrape is happening here. You may
view sites as it is populated with data. To do this, scroll back up to
the top of the form, and notice that the 'App Name' field has been
populated. You can now access your demo site at:

        https://<app-name>.herokuapps.com

#### Local

1. Ensure you've got the Python dependencies in requirements.txt

2. Flesh out the CONFIG files. DBCONFIG.py in the /openorders folder and the /scraper. ALERTSCONFIG.py in the /openorders/alerts (has MailGun creds). FLASKCONFIG.py in /openorders. Remember to set DEBUG here to false in prod. 

3. Ensure your db is created w/ unicode encoding. Restore the db from the dump or... rescrape the site from scratch loool. (see README.md in /scraper)

4. Running python __init__.py (in /openorders) will get the Flask server running.

5. Search Page JS
   a) Install Node.
   b) Go into /openorders/static/js and run 'npm install' to get all the js dependencies.
   c) Running 'npm run dev' will get a webpack server to serve a bundle.js for dev purposes, ensure you're linking to the dev bundle.js at the bottom search.html file and escape the prod bundle.js and vice versa for dev purposes. (Alternatively branch dev & prod) Running 'webpack search.jsx bundle.js' will spit out a bundle.js for prod. 
All this is just for that search page's UI. If you can't find someone comfortable w/ React; get someone to do it in Angular or JQuery. Should be trivial.

6. Run a daily cron on dailyscrape.py. At the bottom I have an email sent for basic logging. Furbish your own Mailgun/mailer creds.

## TODO
1. The views in the alerts blueprint & associated Unsubscribe & confirmation page templates. (alerts/views.py)
2. Confirmation email template 
3. Daily digest email template & associated dailymailer script. (+cron)
4. A signup box on the homepage that posts to the subscribe view in alerts.
5. Categorization & viz.
