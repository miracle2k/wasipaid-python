-----------------------------------------------------------
Commandline Tool to simulate wasipaid.com URL notifications
-----------------------------------------------------------

Send a payment notification to your app. This just uses a stati template,
so we modify the amount:

    $ wasipaid notify payment http://localhost:5000 --amount 12.00/USD


Installation
------------

    $ sudo easy_install wasipaid
