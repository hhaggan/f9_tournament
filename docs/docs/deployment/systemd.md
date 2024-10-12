# Systemd

This section describes how to deploy Forte9 (frontend and backend) as a Systemd service on Linux.

This assumes:

- You have installed `yarn` and `pipenv`.
- You have a PostgreSQL cluster running.
- You have cloned Forte9 in `/var/lib/bracket`.
- You have created a new user called Forte9 with the permissions to read
and write in `/var/lib/bracket`.

Now, You can run the application using `systemd.service` files.
Below is a simple example of the service files for the backend and frontend:

## Backend

```systemd
[Unit]
Description=Forte9 backend
After=syslog.target
After=network.target

[Service]
Type=simple
User=bracket
WorkingDirectory=/var/lib/bracket/backend
ExecStart=pipenv run gunicorn -k uvicorn.workers.UvicornWorker bracket.app:app --bind localhost:8400 --workers 1
Environment=ENVIRONMENT=PRODUCTION
TimeoutSec=15
Restart=always
RestartSec=2s

[Install]
WantedBy=multi-user.target
```

## Frontend

```systemd
[Unit]
Description=Forte9 frontend
After=syslog.target
After=network.target

[Service]
Type=simple
User=bracket
WorkingDirectory=/var/lib/bracket/frontend
ExecStart=/usr/local/bin/yarn start
Environment=NODE_ENV=production
TimeoutSec=15
Restart=always
RestartSec=2s

[Install]
WantedBy=multi-user.target
```
