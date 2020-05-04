# What is public-ip-lists

Format public meta API's into a format readable by Firewall's.

# Accept header

public-ip-lists can format the output in new-line seperated and JSON format. The output is determined by the `Accept` header.

# Current supported Firewall's:

- PfSense

# Run container

Docker command to run container:

```
$ docker run -p 5000:5000 --name public-ip-lists -d nextpertise/public-ip-lists
```

# Providers:

- atlassian (https://ip-ranges.atlassian.com/)
