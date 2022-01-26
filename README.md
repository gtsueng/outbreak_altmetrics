### Dummy BioThings parser for altmetrics data

The real altmetrics parser takes awhile to run and is dependent on the outbreak.info resources API. It is undesirable to have this process hold up the other parsers. For this reason, the altmetrics parser will save the data to a specified location, where this dummy parser will access and serve it up to the outbreak hub