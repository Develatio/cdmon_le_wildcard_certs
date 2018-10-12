# Scripts for getting Let's Encrypt wildcard certs and cdmon.com

Let's Encrypt has a tool called `certbot-auto`, which you can use to obtain
wildcard certificates. There is only one problem: you need to use DNS challenge,
which involves creating a TXT record at runtime, which means that your DNS
registrar must have an API in order for you to be able to control it
programmatically.

These scripts will help you get wildcard LE certs if you have a domain at
cdmon.com

Just clone and project, create the required `.env` file (make sure to read
the [README.md of cdmon_automator](https://github.com/Develatio/cdmon_automator)) and then run the required commands:

```bash
git clone git@github.com:Develatio/cdmon_le_wildcard_certs.git
cd cdmon_le_wildcard_certs
pip3 install -r requirements.txt
```

```bash
certbot-auto certonly
    --server https://acme-v02.api.letsencrypt.org/directory
    --manual
    --preferred-challenges dns
    --manual-auth-hook "./auth.py"
    --manual-cleanup-hook "./clean.py"
    -d '*.yourdomain.tld'
```

You can also use this, if you just want to test things out:

```bash
certbot-auto certonly
    --server https://acme-staging-v02.api.letsencrypt.org/directory
    --manual
    --preferred-challenges dns
    --manual-auth-hook "./auth.py"
    --manual-cleanup-hook "./clean.py"
    -d '*.yourdomain.tld'
    --dry-run
```