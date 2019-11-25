# RSS reader
RSS reader is a command-line utility that retrieves the RSS URL and prints the results in a human-readable format.

## Distribution
The program is located in module rssreader. When unpacking, it is installed in the system. After installation, to start using the program, write rss-reader to the terminal.

## Specification
The program works with command line arguments. Their description:

**usage:** rss-reader \[-h] \[--version] \[--json] \[--verbose] \[--limit *LIMIT*] source

+ Positionalarguments:
    + source => RSS URL

+ Optional arguments:
    + -h, --help => Show help message and exit. Сan be used as a single argument.
    + --version => Print version info. Сan be used as a single argument.
    + --json => Print result as JSON in stdout.
    + --verbose => Outputs verbose status messages.
    + --limit LIMIT => Limit news topics if this parameter is provided. LIMIT

+ Additional description:
    + --limit => can be used with --json.
    + --json => the description of the circuit is in the file **parsing_json_schema.json**
