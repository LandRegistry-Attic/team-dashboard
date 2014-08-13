# Team Dashboard

[![Build Status](https://travis-ci.org/LandRegistry/team-dashboard.svg)](https://travis-ci.org/LandRegistry/team-dashboard)

Dashboard and other pages for presenting whereabouts, cards and other information about a team.

The data itself is stored elsewhere, fetched as Tab Separated Values (TSV).

# Run locally

    mkvirtualenv team-dashboard
    pip install -r requirements.txt
    
Export all the variables required in [config.py](config.py) (especially ```TEAM_TSV_URL``` and ```WHEREABOUTS_TSV_URL```), and then run with:

    ./run.sh
    
    
