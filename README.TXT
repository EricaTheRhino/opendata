Very basic docs so people who aren't me know what's going on here.

There are two files in this directory:

download
--------

This downloads a lot of JSON from my home space on users. It takes
a path as an argument, and drops the JSON files in there. It's
currently running in a cron job on the Brain so that gets data
every 10 minutes or so and puts it in the data directory for the
screens.

The final line in 'download' actually uploads! It's responsible
for uploading Erica's brain state to data.soton where a script
running there can convert it into RDF.


weather
-------

This downloads another JSON file from my home space, which contains
the weather info for Southampton, taken from the BBC's RSS feed.
Again, it puts it into the screen's data directory where it can be
acted upon, but it also checks the temperature against the
previous value, and if it's different, it sends an event to the
brain.

