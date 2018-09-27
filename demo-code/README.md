### Start Locust:

You can run [Locust](https://locust.io/) on the web interface or the CLI tool.

**No-Web/CLI**:

```
locust -f [*.py file] --host=[url] --no-web -c 10 -r 1
```

**Web**:

```
locust -f [*.py file] --host=[url]
```

To see all available options type `locust --help`.


**Taurus**

Ensure you have [taurus](https://gettaurus.org/) installed. This assumes [locust](https://docs.locust.io/en/stable/installation.html) is already installed.

```
bzt [YAML file] -report
```



Build with :heart: in the [+254](https://www.wikiwand.com/en/Kenya)
